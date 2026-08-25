"""Live object registry: what is currently in the scene, refreshed in background.

This is what makes fully-automatic operation possible. Nothing is pre-registered
and no config file is needed: the detector scans the scene periodically, and the
gaze stage is matched against whatever it found.

The detector costs ~5 s on CPU, so it cannot run per frame. It runs on a
background thread instead, while the gaze stage keeps running at full speed on
the main thread against the most recent object list. Two consequences:

  * the object list is always slightly stale, which is fine because bedside
    objects move rarely and slowly
  * a camera knock or a moved object self-heals within one refresh interval,
    which manual registration can never do
"""

from __future__ import annotations

import threading
import time
from dataclasses import dataclass, field

import numpy as np

from .object_detector import ObjectDetection, OpenVocabDetector
from .targets import Target, TargetSet

# Broad default vocabulary for a bedside / desk scene. Prompt count is nearly
# free: measured 5313 ms for 18 prompts vs 5491 ms for 2, because the vision
# encoder dominates and text queries are cheap.
DEFAULT_VOCAB: list[str] = [
    "water bottle",
    "drinking glass",
    "cup",
    "mobile phone",
    "laptop computer",
    "book",
    "bowl of food",
    "plate of food",
    "fruit",
    "medicine strip",
    "pill bottle",
    "tissue box",
    "remote control",
    "spectacles",
    "bell",
    "towel",
]

# Detected but never offered as a communication target.
BLOCKLIST = {
    "person", "hand", "face", "arm", "head", "hair", "bed", "wall",
    "window", "curtain", "door", "floor", "ceiling", "table", "chair",
}


@dataclass
class ObjectRegistry:
    """Thread-safe, periodically-refreshed view of the objects in the scene."""

    detector: OpenVocabDetector
    vocab: list[str] = field(default_factory=lambda: list(DEFAULT_VOCAB))
    score_threshold: float = 0.18
    refresh_seconds: float = 6.0
    max_objects: int = 6

    def __post_init__(self) -> None:
        self._lock = threading.Lock()
        self._objects: list[ObjectDetection] = []
        self._latest_frame: np.ndarray | None = None
        self._last_refresh: float = 0.0
        self._scan_count: int = 0
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None

    # ------------------------------------------------------------------ access

    @property
    def objects(self) -> list[ObjectDetection]:
        with self._lock:
            return list(self._objects)

    @property
    def scan_count(self) -> int:
        with self._lock:
            return self._scan_count

    @property
    def seconds_since_refresh(self) -> float:
        with self._lock:
            return time.time() - self._last_refresh if self._last_refresh else float("inf")

    def as_target_set(self, frame_size: tuple[int, int] | None = None) -> TargetSet:
        """Expose the current objects in the form the gaze scorer expects.

        Labels are made unique ("cup", "cup #2") because the posterior is keyed
        by label and duplicates would otherwise silently collide.
        """
        seen: dict[str, int] = {}
        targets: list[Target] = []
        for obj in self.objects:
            seen[obj.label] = seen.get(obj.label, 0) + 1
            n = seen[obj.label]
            targets.append(
                Target(label=obj.label if n == 1 else f"{obj.label} #{n}", box=obj.box)
            )
        return TargetSet(targets=targets, frame_size=frame_size)

    # ------------------------------------------------------------------ update

    def submit_frame(self, frame_bgr: np.ndarray) -> None:
        """Offer the newest frame for the next background scan."""
        with self._lock:
            self._latest_frame = frame_bgr

    def scan_now(self, frame_bgr: np.ndarray) -> list[ObjectDetection]:
        """Run detection synchronously. Blocks for seconds -- use for setup."""
        dets = self.detector.detect(
            frame_bgr, self.vocab, score_threshold=self.score_threshold
        )
        dets = [d for d in dets if d.label.lower() not in BLOCKLIST][: self.max_objects]
        with self._lock:
            self._objects = dets
            self._last_refresh = time.time()
            self._scan_count += 1
        return dets

    # ------------------------------------------------------------- background

    def start(self) -> None:
        if self._thread is not None:
            return
        self._stop.clear()
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        self._stop.set()
        if self._thread is not None:
            self._thread.join(timeout=15.0)
            self._thread = None

    def _loop(self) -> None:
        while not self._stop.is_set():
            with self._lock:
                frame = None if self._latest_frame is None else self._latest_frame.copy()
            if frame is None:
                self._stop.wait(0.2)
                continue
            try:
                self.scan_now(frame)
            except Exception:  # noqa: BLE001 - a failed scan must not kill the loop
                with self._lock:
                    self._last_refresh = time.time()
            self._stop.wait(self.refresh_seconds)

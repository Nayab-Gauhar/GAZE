"""End-to-end Option-3 pipeline: frame -> target label or NONE.

    frame
      -> head detection            (DEIMv2 Wholebody34, class 7)
      -> gaze heatmap + in/out     (distilled Gaze-LLE)
      -> heatmap-to-target scoring (posterior over targets + NONE)
      -> sticky HMM + dwell        (temporal evidence, abstention)
      -> emitted label

Nothing here is calibrated to a specific person, which is the whole point of
Option 3: it runs on a newly admitted patient with no setup beyond registering
where the targets are.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

from .detector import Detection, HeadDetector
from .gazelle import GazelleONNX, GazeResult
from .targets import NONE_LABEL, TargetSet, TargetScore
from .temporal import GazeStateFilter, TemporalConfig, TemporalDecision


@dataclass
class FrameResult:
    head: Detection | None
    gaze: GazeResult | None
    posterior: dict[str, float]
    detail: list[TargetScore]
    decision: TemporalDecision | None

    @property
    def emitted(self) -> str | None:
        return self.decision.emitted if self.decision else None


class GazeTargetPipeline:
    def __init__(
        self,
        target_set: TargetSet,
        gazelle_model: str | Path,
        detector_model: str | Path,
        temporal_config: TemporalConfig | None = None,
        providers: list[str] | None = None,
        detect_every_n: int = 1,
    ) -> None:
        """
        detect_every_n:
            Run head detection only every Nth frame and reuse the cached box in
            between. Head detection measured at ~28% of the CPU frame budget,
            and a bed-bound patient's head barely moves between frames, so this
            is close to free accuracy-wise and a large throughput win. Set to 1
            to detect on every frame.
        """
        self.targets = target_set
        self.detector = HeadDetector(detector_model, providers=providers)
        self.gazelle = GazelleONNX(gazelle_model, providers=providers)
        self.filter = GazeStateFilter(
            labels=target_set.labels,
            config=temporal_config or TemporalConfig(),
        )
        self.detect_every_n = max(1, int(detect_every_n))
        self._frame_no = 0
        self._cached_head: Detection | None = None

    def reset(self) -> None:
        self.filter.reset()
        self._frame_no = 0
        self._cached_head = None

    def _get_head(self, frame_bgr: np.ndarray) -> Detection | None:
        """Detect, or reuse the cached box on skipped frames."""
        due = (self._frame_no % self.detect_every_n == 0) or self._cached_head is None
        self._frame_no += 1
        if due:
            found = self.detector.primary_head(frame_bgr)
            # Only overwrite the cache on a positive detection, so a single
            # dropped detection doesn't blank the tracked head.
            if found is not None:
                self._cached_head = found
            else:
                self._cached_head = None
            return self._cached_head
        return self._cached_head

    def process(self, frame_bgr: np.ndarray, use_temporal: bool = True) -> FrameResult:
        head = self._get_head(frame_bgr)
        if head is None:
            # No head means no evidence. Feed certain-NONE so belief decays
            # toward NONE instead of freezing on a stale target.
            decision = (
                self.filter.update({NONE_LABEL: 1.0}, inout=0.0) if use_temporal else None
            )
            return FrameResult(None, None, {NONE_LABEL: 1.0}, [], decision)

        results = self.gazelle(frame_bgr, [head.box])
        if not results:
            decision = (
                self.filter.update({NONE_LABEL: 1.0}, inout=0.0) if use_temporal else None
            )
            return FrameResult(head, None, {NONE_LABEL: 1.0}, [], decision)

        gaze = results[0]
        posterior = self.targets.score(gaze.heatmap, gaze.inout, gaze.peak_xy)
        detail = self.targets.detail(gaze.heatmap, gaze.inout, gaze.peak_xy)
        decision = (
            self.filter.update(posterior, inout=gaze.inout) if use_temporal else None
        )
        return FrameResult(head, gaze, posterior, detail, decision)

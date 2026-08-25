"""Target registration and heatmap-to-target scoring.

A `TargetSet` is the registered layout: the communication targets (symbol cards
or physical objects) as boxes in frame coordinates. Because the camera and the
layout are fixed for an installation, this is configured once and reused.

Scoring turns a Gaze-LLE heatmap into a posterior over {targets} + NONE:

    p_in          = model's in/out-of-frame score
    mass_i        = heatmap mass inside target i
    mass_total    = heatmap mass over the whole frame
    P(target_i)   = p_in * mass_i / mass_total
    P(NONE)       = 1 - sum_i P(target_i)

NONE therefore absorbs three distinct failure modes, which is exactly what the
clinical requirement needs:
  1. gaze target outside the frame            -> low p_in
  2. gaze inside frame but on nothing registered (ceiling, caregiver, TV)
                                              -> mass concentrated outside all boxes
  3. gaze ambiguous between two targets       -> handled downstream by the margin
                                                 test in `temporal.py`
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

NONE_LABEL = "NONE"

# Gaze-LLE emits a fixed 64x64 heatmap regardless of input size.
HEATMAP_SIDE = 64

# Below this many heatmap cells a target cannot be reliably discriminated.
# 3x3 cells is the practical floor for a stable argmax.
MIN_RELIABLE_CELLS = 9.0


@dataclass
class Target:
    label: str
    box: tuple[int, int, int, int]  # x1, y1, x2, y2 in frame pixels

    @property
    def center(self) -> tuple[float, float]:
        x1, y1, x2, y2 = self.box
        return ((x1 + x2) / 2.0, (y1 + y2) / 2.0)


@dataclass
class TargetScore:
    label: str
    probability: float
    mass: float
    peak_inside: bool


@dataclass
class TargetSet:
    targets: list[Target] = field(default_factory=list)
    frame_size: tuple[int, int] | None = None  # (width, height) at registration
    pad_ratio: float = 0.15
    """Targets are dilated by this fraction of their size before scoring.

    Gaze heatmaps routinely peak slightly off an object rather than dead-centre
    on it, and the 64x64 grid is coarse. A modest dilation recovers that mass.
    Set to 0.0 to score the literal boxes.
    """

    @property
    def labels(self) -> list[str]:
        return [t.label for t in self.targets]

    # ---------------------------------------------------------------- config io

    @classmethod
    def from_json(cls, path: str | Path) -> TargetSet:
        data = json.loads(Path(path).read_text())
        fs = data.get("frame_size")
        return cls(
            targets=[
                Target(label=t["label"], box=tuple(int(v) for v in t["box"]))
                for t in data["targets"]
            ],
            frame_size=(int(fs[0]), int(fs[1])) if fs else None,
            pad_ratio=float(data.get("pad_ratio", 0.15)),
        )

    def to_json(self, path: str | Path) -> None:
        Path(path).write_text(
            json.dumps(
                {
                    "frame_size": list(self.frame_size) if self.frame_size else None,
                    "pad_ratio": self.pad_ratio,
                    "targets": [{"label": t.label, "box": list(t.box)} for t in self.targets],
                },
                indent=2,
            )
        )

    # ---------------------------------------------------------------- geometry

    def _padded_box(
        self, target: Target, frame_w: int, frame_h: int
    ) -> tuple[int, int, int, int]:
        x1, y1, x2, y2 = target.box
        if self.pad_ratio <= 0:
            return x1, y1, x2, y2
        dx = (x2 - x1) * self.pad_ratio
        dy = (y2 - y1) * self.pad_ratio
        return (
            int(max(0, x1 - dx)),
            int(max(0, y1 - dy)),
            int(min(frame_w, x2 + dx)),
            int(min(frame_h, y2 + dy)),
        )

    # ---------------------------------------------------------------- scoring

    def score(
        self, heatmap: np.ndarray, inout: float, peak_xy: tuple[int, int]
    ) -> dict[str, float]:
        """Return a posterior over target labels plus NONE. Sums to 1.0."""
        frame_h, frame_w = heatmap.shape[:2]
        mass_total = float(heatmap.sum())
        if mass_total <= 1e-9:
            return {**{lb: 0.0 for lb in self.labels}, NONE_LABEL: 1.0}

        p_in = float(np.clip(inout, 0.0, 1.0))

        raw: dict[str, float] = {}
        for t in self.targets:
            x1, y1, x2, y2 = self._padded_box(t, frame_w, frame_h)
            raw[t.label] = float(heatmap[y1:y2, x1:x2].sum()) / mass_total

        claimed = sum(raw.values())
        # Registered boxes may overlap after dilation; renormalize so the
        # target block can never exceed the total available probability.
        if claimed > 1.0:
            raw = {k: v / claimed for k, v in raw.items()}
            claimed = 1.0

        posterior = {k: p_in * v for k, v in raw.items()}
        posterior[NONE_LABEL] = max(0.0, 1.0 - sum(posterior.values()))

        total = sum(posterior.values())
        if total > 0:
            posterior = {k: v / total for k, v in posterior.items()}
        return posterior

    def detail(
        self, heatmap: np.ndarray, inout: float, peak_xy: tuple[int, int]
    ) -> list[TargetScore]:
        """Per-target breakdown, for debugging and for the verification report."""
        frame_h, frame_w = heatmap.shape[:2]
        posterior = self.score(heatmap, inout, peak_xy)
        mass_total = max(1e-9, float(heatmap.sum()))
        px, py = peak_xy
        out: list[TargetScore] = []
        for t in self.targets:
            x1, y1, x2, y2 = self._padded_box(t, frame_w, frame_h)
            out.append(
                TargetScore(
                    label=t.label,
                    probability=posterior[t.label],
                    mass=float(heatmap[y1:y2, x1:x2].sum()) / mass_total,
                    peak_inside=(x1 <= px < x2 and y1 <= py < y2),
                )
            )
        out.sort(key=lambda s: s.probability, reverse=True)
        return out

    # ------------------------------------------------------- feasibility check

    def resolution_report(self, frame_w: int, frame_h: int) -> dict:
        """Quantify whether this layout is resolvable at 64x64 heatmap resolution.

        This is the Option-3-specific feasibility gate. It is deliberately run
        *before* trusting any prediction: if targets occupy too few heatmap cells,
        or sit too close together in the camera projection, no amount of model
        quality will separate them.
        """
        cell_w = frame_w / HEATMAP_SIDE
        cell_h = frame_h / HEATMAP_SIDE

        per_target = []
        for t in self.targets:
            x1, y1, x2, y2 = t.box
            cells_x = (x2 - x1) / cell_w
            cells_y = (y2 - y1) / cell_h
            cells = cells_x * cells_y
            per_target.append(
                {
                    "label": t.label,
                    "box_px": [x1, y1, x2, y2],
                    "cells_x": round(cells_x, 2),
                    "cells_y": round(cells_y, 2),
                    "cells_total": round(cells, 1),
                    "reliable": cells >= MIN_RELIABLE_CELLS,
                }
            )

        pairs = []
        for i in range(len(self.targets)):
            for j in range(i + 1, len(self.targets)):
                a, b = self.targets[i], self.targets[j]
                (ax, ay), (bx, by) = a.center, b.center
                dist_px = float(np.hypot(ax - bx, ay - by))
                dist_cells = float(np.hypot((ax - bx) / cell_w, (ay - by) / cell_h))
                pairs.append(
                    {
                        "pair": f"{a.label} <-> {b.label}",
                        "dist_px": round(dist_px, 1),
                        "dist_cells": round(dist_cells, 2),
                        # Peaks closer than ~3 cells are within the heatmap's
                        # own blur and cannot be separated.
                        "separable": dist_cells >= 3.0,
                    }
                )
        pairs.sort(key=lambda p: p["dist_cells"])

        warnings: list[str] = []
        for pt in per_target:
            if not pt["reliable"]:
                warnings.append(
                    f"target '{pt['label']}' covers only {pt['cells_total']} heatmap "
                    f"cells (need >= {MIN_RELIABLE_CELLS:.0f}) -- make it physically "
                    f"larger or move the camera closer"
                )
        for p in pairs:
            if not p["separable"]:
                warnings.append(
                    f"{p['pair']} are {p['dist_cells']} heatmap cells apart "
                    f"(need >= 3.0) -- move them further apart"
                )

        return {
            "frame_size": [frame_w, frame_h],
            "heatmap_cell_px": [round(cell_w, 2), round(cell_h, 2)],
            "targets": per_target,
            "pairs": pairs,
            "warnings": warnings,
            "layout_ok": not warnings,
        }

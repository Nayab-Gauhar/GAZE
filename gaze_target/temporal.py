"""Temporal evidence accumulation, dwell, and abstention.

Per-frame argmax is not usable for an assistive communication device. A patient's
gaze flickers, and treating every glance as a command is the classic Midas touch
failure (Jacob 1990) that makes gaze interfaces intolerable to live with.

This module uses a sticky HMM: states are the registered targets plus NONE, with
a high self-transition probability. One mechanism then yields three behaviours
that would otherwise need three hand-tuned thresholds:

  * temporal smoothing   - isolated bad frames are damped by the transition prior
  * dwell                - probability mass takes time to migrate between states
  * principled abstention - a diffuse belief simply never crosses the threshold

Emission uses the per-frame posterior directly as an observation likelihood.
That is a deliberate approximation (it skips dividing out the class prior), which
is standard practice and adequate here because the prior is near-uniform by
construction.

A selection is emitted only when all of the following hold:
  1. belief in a non-NONE state exceeds `commit_threshold`
  2. the margin over the runner-up exceeds `margin_threshold`
  3. conditions 1-2 have held for `dwell_frames` consecutive frames
and a refractory period then blocks immediate re-firing.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from .targets import NONE_LABEL


@dataclass
class TemporalConfig:
    stay_prob: float = 0.90
    """Self-transition probability. Higher = smoother and slower."""

    commit_threshold: float = 0.65
    """Minimum smoothed belief required to consider committing."""

    margin_threshold: float = 0.20
    """Minimum gap to the runner-up. Guards against adjacent-target ambiguity."""

    dwell_frames: int = 12
    """Consecutive qualifying frames before emitting. ~0.8 s at 15 fps."""

    refractory_frames: int = 30
    """Frames to suppress after an emission, to avoid repeat firing."""

    min_inout: float = 0.35
    """Frames whose in/out score falls below this are treated as NONE evidence."""


@dataclass
class TemporalDecision:
    belief: dict[str, float]
    top_label: str
    top_prob: float
    margin: float
    dwell_count: int
    emitted: str | None
    """Non-None only on the frame where a selection fires."""
    refractory: bool


@dataclass
class GazeStateFilter:
    labels: list[str]
    config: TemporalConfig = field(default_factory=TemporalConfig)

    def __post_init__(self) -> None:
        self.states: list[str] = [*self.labels, NONE_LABEL]
        n = len(self.states)
        if n < 2:
            raise ValueError("need at least one target plus NONE")

        stay = float(np.clip(self.config.stay_prob, 1e-3, 1 - 1e-3))
        off = (1.0 - stay) / (n - 1)
        self._trans = np.full((n, n), off, dtype=np.float64)
        np.fill_diagonal(self._trans, stay)

        # Start fully in NONE: the system must earn its first selection.
        self._belief = np.zeros(n, dtype=np.float64)
        self._belief[self.states.index(NONE_LABEL)] = 1.0

        self._dwell = 0
        self._dwell_label: str | None = None
        self._refractory = 0

    def reset(self) -> None:
        self.__post_init__()

    def update(self, posterior: dict[str, float], inout: float | None = None) -> TemporalDecision:
        obs = np.array(
            [max(1e-9, float(posterior.get(s, 0.0))) for s in self.states],
            dtype=np.float64,
        )

        # A low in/out score means the model believes the gaze target is not in
        # frame at all. Push that evidence toward NONE rather than trusting the
        # spatial distribution, which is meaningless in that case.
        if inout is not None and inout < self.config.min_inout:
            obs[:] = 1e-9
            obs[self.states.index(NONE_LABEL)] = 1.0

        # Forward filter: predict through the transition prior, then correct.
        predicted = self._trans.T @ self._belief
        updated = predicted * obs
        total = updated.sum()
        self._belief = updated / total if total > 0 else predicted

        order = np.argsort(self._belief)[::-1]
        top_label = self.states[order[0]]
        top_prob = float(self._belief[order[0]])
        runner_up = float(self._belief[order[1]]) if len(order) > 1 else 0.0
        margin = top_prob - runner_up

        if self._refractory > 0:
            self._refractory -= 1
            self._dwell = 0
            self._dwell_label = None
            return TemporalDecision(
                belief=dict(zip(self.states, self._belief)),
                top_label=top_label,
                top_prob=top_prob,
                margin=margin,
                dwell_count=0,
                emitted=None,
                refractory=True,
            )

        qualifies = (
            top_label != NONE_LABEL
            and top_prob >= self.config.commit_threshold
            and margin >= self.config.margin_threshold
        )

        if qualifies and top_label == self._dwell_label:
            self._dwell += 1
        elif qualifies:
            self._dwell_label = top_label
            self._dwell = 1
        else:
            self._dwell = 0
            self._dwell_label = None

        emitted: str | None = None
        if self._dwell >= self.config.dwell_frames and self._dwell_label is not None:
            emitted = self._dwell_label
            self._refractory = self.config.refractory_frames
            self._dwell = 0
            self._dwell_label = None

        return TemporalDecision(
            belief=dict(zip(self.states, self._belief)),
            top_label=top_label,
            top_prob=top_prob,
            margin=margin,
            dwell_count=self._dwell,
            emitted=emitted,
            refractory=False,
        )

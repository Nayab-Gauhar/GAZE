"""Option 3 (scene-heatmap) prototype for gaze-based assistive communication.

Detects which registered target a person is looking at from a single RGB camera,
with an explicit NONE class, using distilled Gaze-LLE ONNX models on CPU.
"""

from .detector import Detection, HeadDetector
from .gazelle import GazelleONNX, GazeResult
from .pipeline import FrameResult, GazeTargetPipeline
from .targets import NONE_LABEL, Target, TargetSet, TargetScore
from .temporal import GazeStateFilter, TemporalConfig, TemporalDecision

__all__ = [
    "Detection",
    "HeadDetector",
    "GazelleONNX",
    "GazeResult",
    "FrameResult",
    "GazeTargetPipeline",
    "NONE_LABEL",
    "Target",
    "TargetSet",
    "TargetScore",
    "GazeStateFilter",
    "TemporalConfig",
    "TemporalDecision",
]

# Open-vocabulary detection is optional: it needs the `tokenizers` package and
# the OWLv2 weights. Import lazily so the core pipeline works without them.
try:  # pragma: no cover
    from .object_detector import ObjectDetection, OpenVocabDetector
    from .registry import DEFAULT_VOCAB, ObjectRegistry

    __all__ += [
        "ObjectDetection",
        "OpenVocabDetector",
        "ObjectRegistry",
        "DEFAULT_VOCAB",
    ]
except ImportError:  # tokenizers not installed
    pass

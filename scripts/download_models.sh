#!/usr/bin/env bash
# Download the ONNX models. They are not committed: the 31M gaze model is 128 MB,
# above GitHub's 100 MB per-file limit.
#
#   ./scripts/download_models.sh          # pico gaze model + head detector (21 MB)
#   ./scripts/download_models.sh --all    # also the 31M model (128 MB, needs a GPU)
set -euo pipefail

BASE="https://github.com/PINTO0309/gazelle-dinov3/releases/download/weights"
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/models"
mkdir -p "$DIR"

fetch() {
  local name="$1" dest="$2"
  if [[ -f "$DIR/$dest" ]]; then
    echo "  exists, skipping: $dest"
    return
  fi
  echo "  downloading: $dest"
  curl -fL --progress-bar -o "$DIR/$dest" "$BASE/$name"
}

echo "Models -> $DIR"

# Head detector: DEIMv2 HGNetV2-Pico Wholebody34 (~6 MB). Class id 7 is head.
fetch "deimv2_hgnetv2_pico_wholebody34_340query_n_batch_640x640.onnx" \
      "deimv2_head.onnx"

# Gaze-LLE Pico distillation, 3.51 M params. The only variant usable on CPU
# (~112 ms/frame on 8 cores). GazeFollow AUC 0.9491.
fetch "gazelle_hgnetv2_pico_inout_distill_1x3x640x640_1xNx4.onnx" \
      "gazelle_hgnetv2_pico_inout_distill_1x3x640x640_1xNx4.onnx"

if [[ "${1:-}" == "--all" ]]; then
  # Gaze-LLE X distillation, 31.43 M params, GazeFollow AUC 0.9604.
  # ~924 ms/frame on CPU -- only worthwhile with onnxruntime-gpu or TensorRT.
  fetch "gazelle_dinov3_vits16plus_inout_1x3x640x640_1xNx4.onnx" \
        "gazelle_dinov3_vits16plus_inout_1x3x640x640_1xNx4.onnx"
fi

echo
echo "Done:"
ls -lh "$DIR" | awk 'NR>1 {printf "  %-70s %s\n", $9, $5}'

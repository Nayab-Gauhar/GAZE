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

# Gaze-LLE Atto distillation, 2.93 M params @ 320x320. The default: measured at
# 17 ms/frame on 8 CPU cores (35 FPS end-to-end) with GazeFollow AUC 0.9267.
fetch "gazelle_hgnetv2_atto_inout_distill_1x3x320x320_1xNx4.onnx" \
      "gazelle_hgnetv2_atto_inout_distill_1x3x320x320_1xNx4.onnx"

# Gaze-LLE Femto, 3.15 M @ 416x416. 26 ms, AUC 0.9391. Good accuracy/speed step up.
fetch "gazelle_hgnetv2_femto_inout_distill_1x3x416x416_1xNx4.onnx" \
      "gazelle_hgnetv2_femto_inout_distill_1x3x416x416_1xNx4.onnx"

if [[ "${1:-}" == "--all" ]]; then
  # Larger variants. On CPU these run at 1-12 FPS; the ViT ones need a GPU to be
  # practical. Latencies measured at 640x480 on 8 cores.
  fetch "gazelle_hgnetv2_pico_inout_distill_1x3x640x640_1xNx4.onnx" \
        "gazelle_hgnetv2_pico_inout_distill_1x3x640x640_1xNx4.onnx"   #  82 ms
  fetch "gazelle_hgnetv2_n_inout_distill_1x3x640x640_1xNx4.onnx" \
        "gazelle_hgnetv2_n_inout_distill_1x3x640x640_1xNx4.onnx"      #  86 ms
  fetch "gazelle_dinov3_vit_tiny_inout_1x3x640x640_1xNx4.onnx" \
        "gazelle_dinov3_vit_tiny_inout_1x3x640x640_1xNx4.onnx"        # 254 ms
  fetch "gazelle_dinov3_vit_tinyplus_inout_1x3x640x640_1xNx4.onnx" \
        "gazelle_dinov3_vit_tinyplus_inout_1x3x640x640_1xNx4.onnx"    # 293 ms
  fetch "gazelle_dinov3_vits16_inout_1x3x640x640_1xNx4.onnx" \
        "gazelle_dinov3_vits16_inout_1x3x640x640_1xNx4.onnx"          # 603 ms
  fetch "gazelle_dinov3_vits16plus_inout_1x3x640x640_1xNx4.onnx" \
        "gazelle_dinov3_vits16plus_inout_1x3x640x640_1xNx4.onnx"      # 957 ms
fi

echo
echo "Done:"
ls -lh "$DIR" | awk 'NR>1 {printf "  %-70s %s\n", $9, $5}'

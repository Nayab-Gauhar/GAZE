#!/usr/bin/env bash
# Download OWLv2 open-vocabulary detector (ONNX, quantized ~163 MB).
# Used only at setup time to find targets from text prompts, so its size and
# latency do not affect runtime throughput.
set -euo pipefail

BASE="https://huggingface.co/onnx-community/owlv2-base-patch16-ensemble-ONNX/resolve/main"
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/models/owlv2"
mkdir -p "$DIR"

fetch() {
  local url="$1" dest="$2"
  if [[ -f "$DIR/$dest" ]]; then
    echo "  exists, skipping: $dest"
    return
  fi
  echo "  downloading: $dest"
  curl -fL --progress-bar -o "$DIR/$dest" "$url"
}

echo "OWLv2 -> $DIR"
fetch "$BASE/config.json"               "config.json"
fetch "$BASE/preprocessor_config.json"  "preprocessor_config.json"
fetch "$BASE/tokenizer.json"            "tokenizer.json"
fetch "$BASE/onnx/model_quantized.onnx" "model_quantized.onnx"

echo
echo "Done:"
ls -lh "$DIR" | awk 'NR>1 {printf "  %-30s %s\n", $9, $5}'
echo
echo "Also needs the tokenizer library:  pip install tokenizers"

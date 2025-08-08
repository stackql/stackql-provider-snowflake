#!/usr/bin/env bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

set -e

VENV_DIR="$SCRIPT_DIR/.venv"

if [ ! -d "$VENV_DIR" ]; then
  echo "📦 Creating virtual environment..."
  python3 -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"

if ! pip show pyyaml > /dev/null 2>&1; then
  echo "📥 Installing PyYAML..."
  pip install pyyaml
fi

# Run the standalone pre_process.py script with absolute path
python3 "$SCRIPT_DIR/pre_process.py" "$1"

mv $1/stream.yaml $1/streams.yaml
#!/usr/bin/env bash

# Exit on error
set -e

VENV_DIR=".venv"

# Create virtualenv if not exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# Activate virtualenv
source "$VENV_DIR/bin/activate"

# Install dependencies
echo "Installing dependencies via pip..."
pip install -r requirements.txt

# Run the CLI with all arguments passed to the script
echo "Running command: python -m openapi_to_stackql.cli $@"
python -m openapi_to_stackql.cli "$@"

# Check if command succeeded
if [ $? -ne 0 ]; then
    echo "❌ Command failed with error code $?"
    exit 1
fi

echo "✅ Command completed successfully"
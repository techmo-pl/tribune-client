#!/bin/bash
# coding=utf-8

# This script sends request to tts service using python tts client 
# Before using this script, run 'setup.sh' to check dependencies and prepare virtual environment

set -euo pipefail
IFS=$'\n\t'

SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "${SCRIPT}")

source "$SCRIPTPATH/.env/bin/activate"
python3 "$SCRIPTPATH/tts_client.py" "$@"
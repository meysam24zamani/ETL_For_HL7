#!/bin/bash
set -euo pipefail

# Activate python environment
source env/bin/activate

# Set environment variables
export SAMPLE_DATE='2019-11-22T09:57:19'
export SAMPLE_ID='Z7183270'
export MAIN_SCRIPT="src/main.py"
export PYTHONPATH=$PWD/src:$PWD/src/tools

python src/launch.py \
    --sample-date ${SAMPLE_DATE} \
    --sample-id ${SAMPLE_ID} \
#! /usr/bin/env python3
import logging
import os
import sys
import subprocess
from argparse import Namespace

def _launch_script(cmd: str, args: Namespace):

    # Important things to remember about subprocess library:
    #   - subprocess.run(capture_output=True) will save STDOUT and STDERR and avoid showing it in terminal
    #   - if 'capture_output' is False and an error occurs, the only relevant thing to report is err.returncode
    #   - not sure if it's better subprocess.run() or subprocess.check_call()
    try:
        logging.info(f"Running command: {cmd}")
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        sys.exit(err.returncode)



def run_script(cmd: str, args: Namespace) -> None:
    """Run the command (cmd) provided as a subprocess execution.

    This allows to run any kind of binary (Python, R, bash, etc).

    """
    logging.basicConfig(
        level="INFO",
        format="%(asctime)s [%(levelname)s] -- %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="logs/log_main.log"
    )

    _launch_script(cmd=cmd, args=args)
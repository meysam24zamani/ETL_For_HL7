#! /usr/bin/env python3
import os
import argparse

parser = argparse.ArgumentParser(allow_abbrev=False)

parser.set_defaults(language_interpreter='python3')
parser.add_argument("--main-script", default=os.getenv('MAIN_SCRIPT'), type=str, help="Main Python script to execute")
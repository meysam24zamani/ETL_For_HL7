#! /usr/bin/env python3
from tools.launch_helpers import run_script
from tools.parser import parser

# App-specific parameters
parser.add_argument("--sample-id", type=str, help="Id of the patient")
parser.add_argument("--sample-date", type=str, help="date of the sample")
args = parser.parse_args()

cmd = (
    f"{args.language_interpreter} "
    f"{args.main_script} "
    f"--sample-date {args.sample_date} "
    f"--sample-id {args.sample_id} "
)

# Step 3: run script of application
run_script(cmd=cmd, args=args)

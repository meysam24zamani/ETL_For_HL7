#! /usr/bin/env python3
import argparse
import logging
import sys
from time import strftime, gmtime
from etl.etl_steps import EtlService


def parse_args():
    """Parse all input arguments.
    """
    parser = argparse.ArgumentParser(allow_abbrev=False)

    # ETL_FOR_HL7 parameters
    parser.add_argument("--sample-date", required=True,
                        type=str, help="date of the sample")
    parser.add_argument("--sample-id", required=True,
                        type=str, help="Id of the patient")
    parser.add_argument('--timestamp', default=strftime("%Y-%m-%dT%H-%M-%S", gmtime()),
                        type=str, help="timestamp")
    return parser.parse_args()


def run_tool(args:dict):

    # Receiving parameters and passing them to the paython object
    timestamp = args.timestamp
    sample_id = args.sample_id
    sample_date = args.sample_date
    sample_date_name = sample_date.replace(':' , '-')

    # Sending parameters to other methods
    importer = EtlService(timestamp, sample_id, sample_date, sample_date_name)
    importer.run()


# Main execution method
def main():    
    args = parse_args()
    logging.basicConfig(
        level="INFO",
        format="%(asctime)s [%(levelname)s] -- %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=sys.stdout)
    logging.info("ETL_for_HL7")
    run_tool(args)
    logging.info("Complete successfully")


if __name__ == "__main__":
    main()

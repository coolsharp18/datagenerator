import argparse
import sys
from generator import datagenerator


def getparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config-file', help='Path to config file')
    parser.add_argument('--output-file', help='Path to output file')
    parser.add_argument('--record-count', type=int, help='Number of records to be generated')
    return parser


def main(args):
    parser = getparser()
    parsed_args = parser.parse_args(args[1:])
    datagenerator.generate_data_from_schema(parsed_args.config_file,
                                            parsed_args.output_file,
                                            parsed_args.record_count)


if __name__ == '__main__':
    main(sys.argv)

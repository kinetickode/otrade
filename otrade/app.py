import sys
import pkg_resources
import argparse
import datetime

VERSION = pkg_resources.require("otrade")[0].version


def parse_command_line(args):
    parser = argparse.ArgumentParser(prog='otrade')
    parser.add_argument(
        "--version",
        dest="showVersion",
        action='store_true',
        help="""Show otrade version number.""",
    )
    return parser.parse_args(args)


def run():
    print()
    args = parse_command_line(sys.argv[1:])
    if args.showVersion:
        print()
        print(pkg_resources.require("otrade")[0].project_name, 'Version', VERSION)
        print()
        print()
        sys.exit(0)

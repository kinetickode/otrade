import argparse
from otrade import app


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='otrade')
    parser.add_argument(
        "--date",
        dest="reportDate",
        default=app.defaultReportDate(),
        help="Report Date in format YYYY-MM-DD",
    )
    parser.add_argument(
        "--type",
        dest='reportType',
        default='Daily',
        help="Report type: either Daily or Weekly - default Daily",
    )
    print()
    args = parser.parse_args()
    app.run(args)

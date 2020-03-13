#!/usr/bin/env python
import argparse
from otrade.utils.safe_robin_stocks import safe_robin_stocks


def get_quote(symbol):
    return "Not Implemented"


def run():
    parser = argparse.ArgumentParser(prog='get_quote')
    parser.add_argument(
        "--symbol",
        dest="symbol",
        default=None,
        help="Stock Ticker Symbol",
    )
    args = parser.parse_args()
    return get_quote(args.symbol)


if __name__ == "__main__":
    print()
    print(run())
    print()

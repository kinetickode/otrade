#!/usr/bin/env python
import argparse


def get_price_direction(symbol):
    return "Not Implemented"


def run():
    parser = argparse.ArgumentParser(prog='get_price_direction')
    parser.add_argument(
        "--symbol",
        dest="symbol",
        default=None,
        help="Stock Ticker Symbol",
    )
    args = parser.parse_args()
    return get_price_direction(args.symbol)


if __name__ == "__main__":
    print()
    print(run())
    print()

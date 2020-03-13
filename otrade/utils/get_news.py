#!/usr/bin/env python
import argparse


def get_news(symbol):
    return "Not Implemented"


def run():
    parser = argparse.ArgumentParser(prog='get_news')
    parser.add_argument(
        "--symbol",
        dest="symbol",
        default=None,
        help="Stock Ticker Symbol",
    )
    args = parser.parse_args()
    return get_news(args.symbol)


if __name__ == "__main__":
    print()
    print(run())
    print()

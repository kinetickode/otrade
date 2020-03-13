# tests
import pytest
from otrade.app import run, parse_command_line


def test_run():
    args = parse_command_line(['--version'])
    assert args.showVersion != None

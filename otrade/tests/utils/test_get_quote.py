# tests
import pytest
from otrade.utils.get_quote import get_quote


def test_get_quote():
    result = get_quote('IBM')
    assert result == 'Not Implemented'

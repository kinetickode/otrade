# tests
import pytest
from otrade.utils.get_price_direction import get_price_direction


def test_get_price_direction():
    result = get_price_direction('IBM')
    assert result == 'Not Implemented'

# tests
import pytest
from otrade.utils.get_news import get_news


def test_get_news():
    result = get_news('IBM')
    assert result == 'Not Implemented'

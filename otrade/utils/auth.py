#!/usr/bin/env python
from otrade.utils.safe_robin_stocks import safe_robin_stocks
from otrade.config.config import  RH_USERNAME, RH_PASS


def login(read_only=True):
    try:
        result = safe_robin_stocks.login(RH_USERNAME, RH_PASS)
        return result['detail']
    except Exception as e:
        print('\nLogin Failed:', e, '\n')
        return False


def logout(read_only=True):
    try:
        result = safe_robin_stocks.logout()
        return result
    except Exception as e:
        print('\nLogout Failed', e, '\n')
        return False

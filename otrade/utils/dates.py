from datetime import datetime, timedelta, timezone


def yesterdaysDate():
    return (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")


def todaysDate():
    return (datetime.today()).strftime("%Y-%m-%d")



from getTickerList import getTickerList
from get_no_days_falling import get_no_days_falling


def create_list_days_falling():
    Dict = {}
    tickers = getTickerList("united states")

    for ticker in tickers:
        print(ticker)
        Dict[ticker] = get_no_days_falling(ticker)

    print(Dict)

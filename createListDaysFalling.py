import json
import time

from getTickerList import getTickerList
from get_no_days_falling import get_no_days_falling


def create_list_days_falling():
    Dict = {}
    tickers = getTickerList("united states")

    for ticker in tickers:
        print(ticker)
        Dict[ticker] = get_no_days_falling(ticker)
        time.sleep(5)

        dict_single = {ticker: get_no_days_falling(ticker)}
        a_file = open("data.json", "a")
        json.dump(dict_single, a_file, indent=2)
        a_file.close()

    print(Dict)



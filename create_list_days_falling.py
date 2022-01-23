import csv
import json
import time

from get_no_days_falling import get_no_days_falling
from get_tickers_list import get_tickers_list


def create_list_days_falling():
    start_time = time.time()

    Dict = {}
    tickers = get_tickers_list("united states")
    w = csv.writer(open("output.csv", "a", newline=''))

    for ticker in tickers:
        print(ticker)

        try:
            no_days_falling = get_no_days_falling(ticker)
        except:
            print('get_no_days_falling excpetion')

        Dict[ticker] = no_days_falling
        time.sleep(1)

        w.writerow([ticker, no_days_falling])


    print("--- %s seconds ---" % (time.time() - start_time))

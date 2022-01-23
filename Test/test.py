import csv
import time

import investpy

from get_no_days_falling import get_no_days_falling

start_time = time.time()


def get_tickers_list(country: str):
    tickers: list = investpy.stocks.get_stocks_list(country)
    w = csv.writer(open("../tickers.csv", "a", newline=''))
    for ticker in tickers:
        w.writerow([ticker])
    return tickers


try:
    print(get_no_days_falling("CAKFF"))
except:
    print('Linux function was not executed')
    print(get_no_days_falling("KO"))

get_tickers_list("united states")

print("--- %s seconds ---" % (time.time() - start_time))

# Saves single dict to each line
# dict_single = {ticker: get_no_days_falling(ticker)}
# a_file = open("data.json", "a")
# json.dump(dict_single, a_file, indent=2)
# a_file.close()
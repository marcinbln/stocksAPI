import investpy


def getTickerList(country: str):
    tickers: list = investpy.stocks.get_stocks_list(country)
    return tickers

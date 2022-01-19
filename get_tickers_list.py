import investpy


def get_tickers_list(country: str):
    tickers: list = investpy.stocks.get_stocks_list(country)
    return tickers

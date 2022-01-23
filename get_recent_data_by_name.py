import investpy


def get_recent_data_by_name(stockname: str):
    search_result = investpy.search_quotes(text=stockname, products=['stocks'],
                                           countries=['united states'], n_results=1)
    recent_data = search_result.retrieve_recent_data()
    return recent_data

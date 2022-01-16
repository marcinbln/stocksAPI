from fastapi import FastAPI, Response
import investpy
import pandas as pd

app = FastAPI()
pd.set_option("display.max_rows", None, "display.max_columns", None)

df = investpy.get_stock_historical_data(stock='AAPL',
                                        country='United States',
                                        from_date='01/01/2020',
                                        to_date='10/01/2020')

js = df.to_json(orient = 'table')

@app.get("/")
async def root():
    return {get_no_days_falling("jpm")}

@app.get("/dupa")
async def getItems():
    return Response(js)

@app.get("/dupa2")
async def getItems():
    return Response(js)


def get_no_days_falling(stockname: str):
    recent_data = get_recent_data_by_name(stockname)
    print(recent_data)
    number = 0
    for tuple in recent_data[::-1].itertuples(index=False):
        if tuple._5 > 0:
            break  # break here
        number += 1
    return number


def get_recent_data_by_name(stockname: str):
    search_result = investpy.search_quotes(text=stockname, products=['stocks'],
                                           countries=['united states'], n_results=1)
    recent_data = search_result.retrieve_recent_data()
    return recent_data

    print()








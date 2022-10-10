from fastapi import FastAPI, Response
import investpy
import pandas as pd

import create_list_days_falling
from get_no_days_falling import get_no_days_falling
from get_performance_streak import get_performance_streak

app = FastAPI()
pd.set_option("display.max_rows", None, "display.max_columns", None)

df = investpy.get_stock_historical_data(stock='AAPL',
                                        country='United States',
                                        from_date='01/01/2020',
                                        to_date='10/01/2020')

js = df.to_json(orient='table')

@app.get("/")
async def root():
    dc = get_performance_streak("GOOGL")
    return dc

@app.get("/streak")
async def getItems():
    return Response(js)


# uvicorn main:app --reload

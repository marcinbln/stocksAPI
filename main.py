from fastapi import FastAPI, Response
import investpy
import pandas as pd

import createListDaysFalling
from get_no_days_falling import get_no_days_falling

app = FastAPI()
pd.set_option("display.max_rows", None, "display.max_columns", None)

df = investpy.get_stock_historical_data(stock='AAPL',
                                        country='United States',
                                        from_date='01/01/2020',
                                        to_date='10/01/2020')

js = df.to_json(orient='table')

@app.get("/")
async def root():
    return {get_no_days_falling("jpm")}

@app.get("/dupa")
async def getItems():
    return Response(js)


@app.get("/dupa2")
async def getItems():
    return Response()

createListDaysFalling.create_list_days_falling()

# uvicorn main:app --reload

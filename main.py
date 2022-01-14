import json

from fastapi import FastAPI
import investpy

app = FastAPI()

df = investpy.get_stock_historical_data(stock='AAPL',
                                        country='United States',
                                        from_date='01/01/2020',
                                        to_date='05/01/2020')
print(df.head())

result = df.to_json(orient="split")
parsed = json.loads(result)
json.dumps(parsed, indent=2)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/dupa")
async def getItems():
    return {tuple(parsed)}
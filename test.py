import json
import investpy


df = investpy.get_stock_historical_data(stock='AAPL',
                                        country='United States',
                                        from_date='01/01/2021',
                                        to_date='05/01/2021')


print(df.head())

result = df.to_json(orient="split")
parsed = json.loads(result)
json.dumps(parsed, indent=4)

print(parsed)

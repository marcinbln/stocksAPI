import json
import investpy
import time

# Filter dataframe to only one column

search_result = investpy.search_quotes(text='apple', products=['stocks'],
                                       countries=['united states'], n_results=1)
recent_data = search_result.retrieve_recent_data()
filtered=recent_data[['Change Pct']]

for tuple in filtered.itertuples(index=False):
    print(tuple._0)

start_time = time.time()

df = investpy.get_stock_historical_data(stock='AAPL',
                                        country='United States',
                                        from_date='01/01/2020',
                                        to_date='10/01/2020')

js = df.to_json(orient='table')


print("--- %s seconds ---" % (time.time() - start_time))
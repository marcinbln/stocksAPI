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

print("--- %s seconds ---" % (time.time() - start_time))
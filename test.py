import json
import investpy
import time

# Don't filter columns first

search_result = investpy.search_quotes(text='JPM', products=['stocks'],
                                       countries=['united states'], n_results=1)
recent_data = search_result.retrieve_recent_data()

for tuple in recent_data.itertuples(index=False):
    print(tuple._5)

start_time = time.time()
print(recent_data)
print("--- %s seconds ---" % (time.time() - start_time))
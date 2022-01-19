import json
import investpy
import time

# Don't filter columns first
import pandas as pd

search_result = investpy.search_quotes(text='JPM', products=['stocks'],
                                       countries=['united states'], n_results=1)
recent_data = search_result.retrieve_recent_data()


def create_list():
    data = {'Name': ['Tom'], 'Age': [20]}
    dflist = pd.DataFrame(data)
    print(dflist)


create_list()

for tuple in recent_data.itertuples(index=False):
    print(tuple._5)

start_time = time.time()
print(recent_data)
print("--- %s seconds ---" % (time.time() - start_time))



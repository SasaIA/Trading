import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient
from alpha_vantage.timeseries import TimeSeries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (20,8)

ALPHA_VANTAGE_API_KEY = open('key.txt', 'r').read()
ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')


try:
    server = MongoClient('mongodb://localhost:27017/')
    print('Connected successfully :D')
except:
    print('Could not connect to MongoDB :(')

db = server['trading']
companies = server['companies']

df = pd.DataFrame(list(db.companies.find({})))
df = df.drop('_id', axis=1)
df = df.sort_values('Date', ignore_index=True)

ibm = pd.DataFrame(list(db.companies.find({ 'Company': 'IBM' })))
ibm = ibm.drop('_id', axis=1)
ibm = ibm.sort_values('Date', ignore_index=True)


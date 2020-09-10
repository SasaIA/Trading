import pandas as pd
from pymongo import MongoClient
import json
import requests

def data():
    key = open('key.txt', 'r').read()
    companies = ['IBM', 'AAPL', 'MSFT'] #IBM, Apple, Microsoft
    for company in companies:
        data = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+company+'&apikey={}'.format(key))
        data = data.json()
        
        company = data["Meta Data"]["2. Symbol"]
        daily = data['Time Series (Daily)']
        list_daily = []
        for date, value in daily.items():
            d = {}
            d['Company'] = company
            d['Date'] = date
            d['Open'] = value['1. open']
            d['High'] = value['2. high']
            d['Low'] = value['3. low']
            d['Close'] = value['4. close']
            d['Volume'] = value['5. volume']
            list_daily.append(d)

        # print(list_daily)

        try:
            server = MongoClient('mongodb://localhost:27017/')
            print('Connected successfully :D')
        except:
            print('Could not connect to MongoDB :(')
        
        # db = server['trading']
        # companies = server['companies']

        server['trading']['companies'].insert_many(list_daily)
        print("Data inserted")

        server.close()
        print("Disconnected!")
        
        # print(server.list_database_names())
        
        # df = pd.DataFrame(list_daily)
        # df = df.to_csv('data.csv', date_format="iso", encoding='utf-8')        
        # df = df.to_json('data.json', date_format="iso", orient="records")
        # print(df)

data()
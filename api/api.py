import pandas as pd
from pymongo import MongoClient
import json
import requests
import os
import re

def data():
    key = open('../apiKey.txt', 'r').read()
    companies = ['IBM', 'AAPL', 'MSFT'] #IBM, Apple, Microsoft
    for company in companies:
        data = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+company+'&outputsize=full&apikey={}'.format(key))
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

        # pd.DataFrame(list_daily).to_csv('{}.csv'.format(company), index=False)
        pd.DataFrame(list_daily).to_json('{}.json'.format(company), orient='records', date_format="iso")

        # ****Connect to MongoDB Atlas****
        key = open('../mongoKey.txt', 'r').readlines()
        username = key[0].rstrip()
        psswd = key[1].rstrip()
        link = key[2].rstrip()
        accessDB = 'mongodb+srv://{}:{}@{}'.format(username, psswd, link)
        server = MongoClient(accessDB)
        db = server.trading

        # ****Connect to MongoDB with localhost****
        # try:
            # server = MongoClient('mongodb://localhost:27017/')
            # print('Connected successfully :D')
        # except:
        #     print('Could not connect to MongoDB :(')
        
        # ****To find a CSV file****
        # csv = re.search(r'{}.csv'.format(company), str(os.listdir()))
        # df = pd.read_csv(csv.group())
        
        # ****To find a JSON file****
        jsonFile = re.search(r'{}.json'.format(company), str(os.listdir()))
        with open(jsonFile.group()) as f:
            data = json.load(f)
        
        server['trading'][company].insert_many(data)
        print("Data inserted")

        server.close()
        print("Disconnected!")

data()
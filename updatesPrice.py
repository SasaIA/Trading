import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient
from alpha_vantage.timeseries import TimeSeries
import datetime

server = MongoClient("localhost", 27017)
db = server.trading
companies = db.companies

ALPHA_VANTAGE_API_KEY = open('key.txt', 'r').read()
ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')

server = MongoClient("localhost", 27017)
db = server['trading']

lstCompanies = ['IBM', 'AAPL', 'MSFT']

def update():
    yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
    for company in lstCompanies:
        companies = db.company
        if not companies.find({ "Company": str(company), 'Date': yesterday }):
            data, meta_data = ts.get_daily(symbol=company)
            historic = data[['1. open', '4. close']].reset_index()
            lastHistoric = historic['date'].iloc[0]
            if lastHistoric != yesterday:
                companies.insert_one({ "Company" : company, "Date" : yesterday, "Open": historic['1. open'], "High": historic['2. high'], "Low": historic['3. low'], "Close": historic['4. close'], "Volume": historic['5. volume'] })
        print(yesterday)

update()
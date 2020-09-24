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

def updatePrice():
    for company in lstCompanies:
        data, meta_data = ts.get_daily(symbol=company)
        historic = data.reset_index()
        lastHistoric = historic['date'].iloc[0]
        if lastHistoric != db[company].find({ 'Date': datetime.datetime.timedelta(day=1) }):
            db[company].insert_one( { "Company" : company , "Date" : historic.iloc[0][0].strftime("%Y-%m-%d"), "Open": historic.iloc[0][1], "High": historic.iloc[0][2], "Low": historic.iloc[0][3], "Close": historic.iloc[0][4], "Volume": historic.iloc[0][5] })

updatePrice()
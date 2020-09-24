import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient
import datetime

from darts import TimeSeries
from darts.models import RNNModel
from darts.utils.missing_values import auto_fillna

# ****Connect to MongoDB with localhost****
# server = MongoClient("localhost", 27017)
# db = server.trading

# ****Connect to MongoDB Atlas****
key = open('mongoKey.txt', 'r').readlines()
username = key[0].rstrip()
psswd = key[1].rstrip()
link = key[2].rstrip()
accessDB = 'mongodb+srv://{}:{}@{}'.format(username, psswd, link)
server = MongoClient(accessDB)
db = server.trading

lstCompanies = ['IBM', 'AAPL', 'MSFT']

def lstm():
    for company in lstCompanies:
        df = pd.DataFrame(list(db.companies.find({ 'Company': company})))
        df = df.drop('_id', axis=1)
        df = df.sort_values('Date', ignore_index=True)
        series = TimeSeries.from_dataframe(df, 'Date', ['Close'], freq='B', fill_missing_dates=True) # 'B' = Business day
        series = auto_fillna(series)

        model = RNNModel(
            model='LSTM', # Either a string specifying the RNN module type (“RNN”, “LSTM” or “GRU”)
            output_length=1, # Number of time steps to be output by the forecasting module
            hidden_size=25, # Size for feature maps for each hidden RNN layer (hn)
            n_rnn_layers=1, # Number of layers in the RNN module
            input_length=12, # The dimensionality of the TimeSeries instances that will be fed to the fit function
            batch_size=16, # The batch size is a hyperparameter that defines the number of samples to work through before updating the internal model parameters
            n_epochs=200, # The number of epochs is a hyperparameter that defines the number times that the learning algorithm will work through the entire training dataset
            optimizer_kwargs={'lr': 1e-3}, 
            model_name= '{}_RNN'.format(company)
        )

        model.fit(series)
        lstmPred = model.predict(1).values()[0][0]
        db.prediction.insert_one({ "Date": datetime.datetime.today(), "Company": company, "Prediction": round(float(lstmPred), 2) })
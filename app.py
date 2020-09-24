import streamlit as st
from pymongo import MongoClient
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import ColumnDataSource, figure, show
from bokeh.io import show, output_notebook
import pandas_bokeh

server = MongoClient("localhost", 27017)
db = server.trading

lstCompanies = ['IBM', 'MSFT', 'AAPL']

def loadData():
    
    page = st.sidebar.selectbox("Choose a page", ['Stock Market', 'Data Viz', 'LSTM - Prediction'])

    if page == 'Homepage':
        st.title("Stock Market Predictions with LSTM")
        st.write("This project aims to predict whether a company's stock price will rise or fall the next day to find out whether we can buy a stock or not. We selected three companies and collected data from 1999 to present.")
        st.title("Discover data from Alpha Vantage API")
        for company in lstCompanies:
            if st.checkbox(company):
                df = pd.DataFrame(list(db[company].find({})))
                df = df.drop('_id', axis=1)
                st.dataframe(df)
        
    elif page == 'Data Viz':
        st.title('Data Visualization')
        st.subheader('Price history since 1999')
        for company in lstCompanies:
            if st.checkbox(company):
                df = pd.DataFrame(list(db[company].find({})))
                df = df.drop('_id', axis=1)
                # df['High'] = df['High'].apply(lambda x: float(x))
                # df['Low'] = df['Low'].apply(lambda x: float(x))

                # source = ColumnDataSource(data=dict(
                #     date = df['Date'],
                #     open = df['Open'],
                #     close = df['Close'],
                #     label = ['Open', 'Close']
                # ))

                openPrice = df['Open']
                closePrice = df['Close']

                # TOOLTIPS = [( 'Date', '@date{%F}'),
                #             ( 'Open', '$@{adj open}{%0.2f}'),
                #             ( 'Close', '$@{adj close}{%0.2f}')
                #         ]

                fig = figure(title="Open & Close", x_axis_label='Date', y_axis_label='Price')
                fig.line(openPrice, closePrice)

                # fig.line(df['Open'], df['Close'])
                # fig = figure(figsize = (15,10))
                # plt.plot(range(df.shape[0]),(df['Low']+df['High'])/2.0)
                # plt.xticks(range(0,df.shape[0],500),df['Date'].loc[::500],rotation=45)
                # plt.xlabel('Date',fontsize=18)
                # plt.ylabel('Mid Price',fontsize=18)
                # fig.canvas.mpl_connect()

                st.bokeh_chart(fig)
            
    else:
        st.title('LSTM')
        st.subheader('We are going to predict the stock price with LSTM network')

loadData()
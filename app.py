import streamlit as st
from pymongo import MongoClient
import pandas as pd
import numpy as np
import plotly.express as px

server = MongoClient("localhost", 27017)
db = server.trading

lstCompanies = ['IBM', 'MSFT', 'AAPL']

def loadData():
    st.title("Welcome to Stock Market Predictions App!")
    st.write("This project aims to predict whether a company's stock price will rise or fall the next day to find out whether we can buy a stock or not. We selected three companies and collected data from 1999 to present.")

    st.sidebar.subheader("Please choose a field to view company data!")

    if st.sidebar.checkbox("Stock Market"):    
        st.title("Discover data from Alpha Vantage API")
        st.subheader('Please select a company!')
        for company in lstCompanies:
            if st.checkbox(company):
                df = pd.DataFrame(list(db[company].find({})))
                df = df.drop('_id', axis=1)
                st.dataframe(df)

    elif st.sidebar.checkbox("Data Viz"):
        st.title('Data Visualization')
        st.subheader('Stock Price history since 1999!')
        st.subheader('Please select a company!')
        for company in lstCompanies:
            if st.checkbox(company):
                df = pd.DataFrame(list(db[company].find({})))
                df = df.drop('_id', axis=1)

                st.write('Hover your mouse over the graph to view the stock price for each day.')
                # Plotly
                plotOpen = px.line(df, x='Date', y='Open', title="Open Stock Price since 99'", hover_data={"Date": "|%B %d, %Y"})
                plotClose = px.line(df, x='Date', y='Close', title="Close Stock Price since 99'", hover_data={"Date": "|%B %d, %Y"})
                st.plotly_chart(plotOpen)
                st.plotly_chart(plotClose)

    elif st.sidebar.checkbox("LSTM"):
        st.title('LSTM')
        st.subheader('We are going to predict the stock price with LSTM network')

    # page = st.sidebar.selectbox("Choose a page", ['Stock Market', 'Data Viz', 'LSTM - Prediction'])

    # if page == 'Stock Market':
    #     st.title("Stock Market Predictions with LSTM")
    #     st.write("This project aims to predict whether a company's stock price will rise or fall the next day to find out whether we can buy a stock or not. We selected three companies and collected data from 1999 to present.")
    #     st.title("Discover data from Alpha Vantage API")
    #     for company in lstCompanies:
    #         if st.checkbox(company):
    #             df = pd.DataFrame(list(db[company].find({})))
    #             df = df.drop('_id', axis=1)
    #             st.dataframe(df)

        
    # elif page == 'Data Viz':
    #     st.title('Data Visualization')
    #     st.subheader('Stock Price history since 1999!')
    #     st.subheader('Hover your mouse over the graph to view data for each day.')
    #     for company in lstCompanies:
    #         if st.checkbox(company):
    #             df = pd.DataFrame(list(db[company].find({})))
    #             df = df.drop('_id', axis=1)

    #             # Plotly
    #             plotOpen = px.line(df, x='Date', y='Open', title="Open Stock Price since 99'", hover_data={"Date": "|%B %d, %Y"})
    #             plotClose = px.line(df, x='Date', y='Close', title="Close Stock Price since 99'", hover_data={"Date": "|%B %d, %Y"})
    #             st.plotly_chart(plotOpen)
    #             st.plotly_chart(plotClose)



    # else:
    #     st.title('LSTM')
    #     st.subheader('We are going to predict the stock price with LSTM network')
    

loadData()
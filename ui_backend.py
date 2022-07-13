from collections import namedtuple
from multiprocessing.dummy import current_process
import altair as alt
import math
import pandas as pd
import streamlit as st
import pickle

from pathlib import Path

@st.cache(suppress_st_warning=True)
def start_tickers_func(): 
    #Imports Data from Data Folder and puts all the data into a dataframe called df. 
    data = Path("data/FS_sp500_merged_cleaned_stats.csv")
    df = pd.read_csv(data, delimiter=",").rename(columns={"Unnamed: 0":"Ticker"})
    
    df = df.set_index("Ticker")
    #Prints the columns of the df Dataframe 
    #print(list(df.columns))
    #Index gets the index of the df and prints the index 
    index = df.index
    #print(index)
    #Creates a new DF 
    tickers = pd.DataFrame(columns=["Ticker"])

    #For loop to add the ticker names into the ticker datafrmae 
    for i in index:
        tickers.loc[len(tickers.index)] = [i]
    # print (tickers)
    return tickers
    #, df

#tickers, df=start()


@st.cache(suppress_st_warning=True)
def start_df_func(): 
    #Imports Data from Data Folder and puts all the data into a dataframe called df. 
    data = Path("data/FS_sp500_merged_cleaned_stats.csv")
    df = pd.read_csv(data, delimiter=",").rename(columns={"Unnamed: 0":"Ticker"})
    
    df = df.set_index("Ticker")
    #Prints the columns of the df Dataframe 
    #print(list(df.columns))
    #Index gets the index of the df and prints the index 
    index = df.index
    #print(index)
    #Creates a new DF 
    tickers = pd.DataFrame(columns=["Ticker"])

    #For loop to add the ticker names into the ticker datafrmae 
    for i in index:
        tickers.loc[len(tickers.index)] = [i]
    # print (tickers)
    return df

df = start_df_func()

@st.cache(suppress_st_warning=True)
def chosen_ticker_func(chosen_ticker): 
    chosen_ticker_df = df.loc[chosen_ticker,:]
    st.dataframe(data=chosen_ticker_df, width=None, height=None)
    chosen_ticker_array = chosen_ticker_df.to_numpy()
    return chosen_ticker_array

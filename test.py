from collections import namedtuple
from multiprocessing.dummy import current_process
#import altair as alt
import math
import pandas as pd
import streamlit as st
import pickle

from pickle import load
from math import log, floor
from pathlib import Path
from ui_backend import * 

def start(): 
    #Imports Data from Data Folder and puts all the data into a dataframe called df. 
    data = Path("data/sp_500_merged_wsectors_data.csv")
    df = pd.read_csv(data, delimiter=",").rename(columns={"Unnamed: 0":"Ticker"})
    df = df.set_index("Ticker")
    df = df.drop(columns=["0"], inplace=True)
    df.head()

    #Index gets the index of the df and prints the index 
    index = df.index
   
    #Creates a new DF 
    tickers = pd.DataFrame(columns=["Ticker"])

    #For loop to add the ticker names into the ticker datafrmae 
    for i in index:
        tickers.loc[len(tickers.index)] = [i]
    # print (tickers)
    return tickers, df
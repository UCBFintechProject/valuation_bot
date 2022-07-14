from collections import namedtuple
from multiprocessing.dummy import current_process
import altair as alt
import math
import pandas as pd
import streamlit as st
import pickle 

#from sklearn.model_selection import train_test_split
from pickle import load
from math import log, floor
from pathlib import Path

from ui_backend import chosen_ticker_func
#from ui_backend import * 

st.header("Machine Learning Market Cap Prediction Bot", anchor=None)
st.subheader("UC Berkeley Fintech Course Group 2 Project 2")
st.caption("This Bot is a Random Forest Regressor trained ML model. Its trained on the latest financial reports from the S&P 500. It allows you to provide potential financial inputs for a specified ticker and predict a future market cap.", unsafe_allow_html=False)


#@st.cache(allow_output_mutation=True)

if st.button('Start Predicting'):
    #Imports Data from Data Folder and puts all the data into a dataframe called df. 
    data = Path("data/FS_sp500_merged_cleaned_stats.csv")
    if_df = pd.read_csv(data, delimiter=",").rename(columns={"Unnamed: 0":"Ticker"})
    if_df = if_df.set_index("Ticker")
    #df = df.drop(columns=["0"], inplace=True)
    #df.head()

    #Index gets the index of the df and prints the index 
    index = if_df.index
    #index = pd.DataFrame(columns=["Ticker"])

    #Creates a new DF 
    if_tickers = pd.DataFrame(columns=["Ticker"])

    #For loop to add the ticker names into the ticker datafrmae 
    for i in index:
        if_tickers.loc[len(if_tickers.index)] = [i]
    # print (tickers)

global tickers 
global df 
tickers = if_tickers 
df = if_df


# BEGIN UI IN STREAMLIT 
# Drop down box to select the ticker the user would like to predict. 

# tickers = start_tickers_func()
# df = start_df_func()

chosen_ticker = st.selectbox(
    'Which ticker would you like to predict the market cap of?',
    (tickers))

st.write('You selected:', chosen_ticker)


chosen_ticker_df = df.loc[chosen_ticker,:]
st.dataframe(data=chosen_ticker_df, width=None, height=None)
chosen_ticker_array = chosen_ticker_df.to_numpy()

#chosen_ticker_array = chosen_ticker_func(chosen_ticker)
#print(numpy_array)

#use to get the other data from the df dataframe 
#df.loc[row_indexer,column_indexer] - 

st.header("Predicted Values", anchor=None)
st.caption("Use the sliders below to predict the market cap based on changes in the companies financial reporting.", unsafe_allow_html=False)

#Phoebe to add DF to list for the selected ticker 

# Profit Margin
st.subheader("Profit Margin")
profit_margin = chosen_ticker_array[5]
profit_margin_upper = profit_margin * 5
profit_margin_lower = profit_margin * 0.1
st.write("The current profit margin of ticker " + chosen_ticker + " is " + "{:.0%}".format((profit_margin/100)))
predicted_profit_margin = st.slider("Use the slider to choose a profit margin value for prediction of " + chosen_ticker + " market cap.", int(profit_margin_lower), int(profit_margin_upper), int(profit_margin) )


#Cash 
st.subheader("Cash")
# current_cash = df.loc[chosen_ticker].iat[6]
current_cash = chosen_ticker_array[6]
current_cash_upper = current_cash * 3
current_cash_lower = current_cash * 0.1
st.write("The current cash of ticker " + chosen_ticker + " is "  + "${:0,.0f}".format(current_cash))
predicted_cash = st.slider("Use the slider to choose a cash value for prediction of " + chosen_ticker + " market cap.", int(current_cash_lower), int(current_cash_upper), int(current_cash) )



predict_list = list(chosen_ticker_array)
predict_list.pop(0)
# = chosen_ticker_array.delete([0])


#with open('model/RFR_model.sav', 'r') as f: 
model = load(open('model/RFR_model_nosect.pkl', 'rb'))



if st.button('Predict'):
    #using to test 
    print(predict_list)
    predict_list[5] = predicted_profit_margin
    predict_list[6] = predicted_cash
    predict_list_scaled = predict_list
    scaler = load(open('model/RFR_scaler_nosect.pkl', 'rb'))
    predict_list_scaled = scaler.transform([predict_list])
    prediction = model.predict(predict_list_scaled)
    prediction = prediction.astype(int)
    prediction_int = prediction[0]
    st.write('The predicted market cap of ' + str(chosen_ticker) + ' based on the selections above is ' + str(prediction_int) )


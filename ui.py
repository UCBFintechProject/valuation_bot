from collections import namedtuple
from multiprocessing.dummy import current_process
import altair as alt
import math
import pandas as pd
import streamlit as st

from pathlib import Path

"""
# Welcome to the UC Berkeley Fintech Bootcamp Project 2 Group 2 Valuation Bot!

Provide input values for the following financial results for a company to predict their share price. 

"""

#To-Do List 
#Drop down for ticker - DONE
# Cash 
# Net receivables
# longTerm Debt 
# Short Long Term Debt
# Income before Tax
# Net Income
# Dividends paid 
# Other current assets 
# Ebit 
# totalRevenue
# totalOperatingExpenses
# depreciation
# dividendsPaid
# Market cap? 



#Imports Data from Data Folder and puts all the data into a dataframe called df. 
data = Path("data/FS_sp500_merged_cleaned_stats.csv")
df = pd.read_csv(data, delimiter=",").rename(columns={"Unnamed: 0":"Ticker"})
df = df.set_index("Ticker")
#Prints the columns of the df Dataframe 
print(list(df.columns))
#Index gets the index of the df and prints the index 
index = df.index
print(index)
#Creates a new DF 
tickers = pd.DataFrame(columns=["Ticker"])

#For loop to add the ticker names into the ticker datafrmae 
for i in index:
    tickers.loc[len(tickers.index)] = [i]
print (tickers)


#BEGIN UI IN STREAMLIT 
#Drop down box to select the ticker the user would like to predict. 
chosen_ticker = st.selectbox(
    'Which Ticker would you like to predict the share price of?',
    (tickers))
st.write('You selected:', chosen_ticker)

chosen_ticker_df = df.loc[chosen_ticker,:]
st.dataframe(data=chosen_ticker_df, width=None, height=None)

#print(df.loc[chosen_ticker,:])

#use to get the other data from the df dataframe 
#df.loc[row_indexer,column_indexer] - 

#Get existing values for each of the variables 

#current_net_receivables = 
#current_longTerm_Debt = 
#current_Short_Long_Term_Debt = 
# Income before Tax
# Net Income
# Dividends paid 
# Other current assets 
# Ebit 
# totalRevenue
# totalOperatingExpenses
# depreciation
# dividendsPaid
# Market cap? 

 #Slider for user to choose the input for cash 
 # num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

st.header("Default Values ", anchor=None)
# OutstandingShares
# Depreciation
# sellingGeneralAdministrative
# Interest Expense
# incomeTaxExpense
# costOfRevenue
# netIncomeFromContinuingOps
# netIncomeApplicableToCommonShares
# investments
# changeToLiabilities
# totalCashflowsFromInvestingActivities
# totalCashFromFinancingActivities
# changeToOperatingActivities
# repurchaseOfStock
# effectOfExchangeRate
# totalCashFromOperatingActivities
# changeToAccountReceivables
# changeToNetincome
# capitalExpenditures

st.header("Predicted Values", anchor=None)
#Cash 
st.subheader("Cash")
current_cash = df.loc[chosen_ticker].iat[6]
current_cash_upper = current_cash * 1.5
current_cash_lower = current_cash * 0.5
st.write("The current cash of the chosen ticker is " + str(current_cash))
predicted_cash = st.slider("Predicted cash reported by " + chosen_ticker + ".", int(current_cash_lower), int(current_cash_upper), int(current_cash) )
# Net receivables
st.subheader("Net Receivables")
net_receivables = df.loc[chosen_ticker].iat[6]
net_receivables_upper = net_receivables * 1.5
net_receivables_lower = net_receivables * 0.5
st.write("The current net receivables of the chosen ticker is " + str(net_receivables))
predicted_cash = st.slider("Predicted net_receivables reported by " + chosen_ticker + ".", int(net_receivables_lower), int(net_receivables_upper), int(net_receivables) )
# longTerm Debt 
st.subheader("Long Term Debt")
# Short Long Term Debt
st.subheader("Short Long Term Debt")
# Income before Tax
st.subheader("Income Before Taz")
# Net Income
st.subheader("Net Income")
# Dividends paid 
st.subheader("Dividends Paid")
# Other current assets 
st.subheader("Other Current Assets")
# Ebit 
st.subheader("Ebit")
# totalRevenue
st.subheader("Total Revenue")
# totalOperatingExpenses
st.subheader("Total Operating Expenses")

# depreciation
st.subheader("Depreciation")
# dividendsPaid
st.subheader("Dividends")
# Market cap? 
st.subheader("The Resulting Market Cap")


st.header("Final Stock Price Prediction", anchor=None)
#INCOMPLETE - Need to add variable for the current share price of the selected stock. 
st.write('Current Share Price is' )
st.write('The predicted value of the share price based on the selections above is ' )


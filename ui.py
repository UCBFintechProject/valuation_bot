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

#get static values for
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
current_cash = df.iat[0,7]
#df.get_value(1, 7)
#f[chosen_ticker].values[7]
#2['col_name'].values[0]
st.write("The current cash of the chosen ticker is" + str(current_cash))
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

with st.echo(code_location='below'):

    #Slider for user to choose the input for cash 
    predicted_cash = st.slider("Predicted cash reported by " + chosen_ticker + ".", 1, 5000, 2000)




    #num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

#INCOMPLETE - Need to add variable for the current share price of the selected stock. 
st.write('Current Share Price is' )
st.write('The predicted value of the share price based on the selections above is' )

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))


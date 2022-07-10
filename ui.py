from collections import namedtuple
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

#Drop down box to select the ticker the user would like to predict. 
chosen_ticker = st.selectbox(
    'Which Ticker would you like to predict the share price of?',
    (tickers))
st.write('You selected:', chosen_ticker)

print(df.loc[chosen_ticker,:])

#use to get the other data from the df dataframe 
#df.loc[row_indexer,column_indexer] - 


#Slider for user to choose the input for cash 
predicted_cash = st.slider("Predicted cash reported by " + chosen_ticker + ".", 1, 5000, 2000)


num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

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


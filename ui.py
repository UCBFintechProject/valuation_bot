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


#use to get the other data from the df dataframe 
#df.loc[row_indexer,column_indexer] - 

st.header("Predicted Values", anchor=None)

#Cash 
st.subheader("Cash")
current_cash = df.loc[chosen_ticker].iat[6]
current_cash_upper = current_cash * 1.5
current_cash_lower = current_cash * 0.5
st.write("The current cash of the chosen ticker is " + str(current_cash))
predicted_cash = st.slider("Predicted cash reported by " + chosen_ticker + ".", int(current_cash_lower), int(current_cash_upper), int(current_cash) )

# Net receivables
# st.subheader("Net Receivables")
# net_receivables = df.loc[chosen_ticker].iat[6]
# net_receivables_upper = net_receivables * 1.5
# net_receivables_lower = net_receivables * 0.5
# st.write("The current net receivables of the chosen ticker is " + str(net_receivables))
# predicted_net_receivables = st.slider("Predicted net_receivables reported by " + chosen_ticker + ".", int(net_receivables_lower), int(net_receivables_upper), int(net_receivables) )

# longTerm Debt 
# st.subheader("Long Term Debt")
# long_term_debt = df.loc[chosen_ticker].iat[29]
# long_term_debt_upper = long_term_debt * 1.5
# long_term_debt_lower = long_term_debt * 0.5
# st.write("The current long_term_debt of the chosen ticker is " + str(long_term_debt))
# predicted_long_term_debt = st.slider("Predicted long_term_debt reported by " + chosen_ticker + ".", int(long_term_debt_lower), int(long_term_debt_upper), int(long_term_debt) )

# Short Long Term Debt
# st.subheader("Short Long Term Debt")
# short_long_term_debt = df.loc[chosen_ticker].iat[6]
# short_long_term_debt_upper = short_long_term_debt * 1.5
# short_long_term_debt_lower = short_long_term_debt * 0.5
# st.write("The current short_long_term_debt of the chosen ticker is " + str(short_long_term_debt))
# predicted_short_long_term_debt = st.slider("Predicted short_long_term_debt reported by " + chosen_ticker + ".", int(short_long_term_debt_lower), int(short_long_term_debt_upper), int(short_long_term_debt) )

# Income before Tax
# st.subheader("Income Before Tax")
# income_before_tax = df.loc[chosen_ticker].iat[6]
# income_before_tax_upper = income_before_tax * 1.5
# income_before_tax_lower = income_before_tax * 0.5
# st.write("The current income_before_tax of the chosen ticker is " + str(income_before_tax))
# predicted_income_before_tax = st.slider("Predicted income_before_tax reported by " + chosen_ticker + ".", int(income_before_tax_lower), int(income_before_tax_upper), int(income_before_tax) )

# Net Income
# st.subheader("Net Income")
# net_income = df.loc[chosen_ticker].iat[6]
# net_income_upper = net_income * 1.5
# net_income_lower = net_income * 0.5
# st.write("The current net_income of the chosen ticker is " + str(net_income))
# predicted_net_income = st.slider("Predicted net_income reported by " + chosen_ticker + ".", int(net_income_lower), int(net_income_upper), int(net_income) )

# Dividends paid 
# st.subheader("Dividends Paid")
# dividends_paid = df.loc[chosen_ticker].iat[6]
# dividends_paid_upper = dividends_paid * 1.5
# dividends_paid_lower = dividends_paid * 0.5
# st.write("The current dividends_paid of the chosen ticker is " + str(dividends_paid))
# predicted_dividends_paid = st.slider("Predicted dividends_paid reported by " + chosen_ticker + ".", int(dividends_paid_lower), int(dividends_paid_upper), int(dividends_paid) )

# Other current assets 
# st.subheader("Other Current Assets")
# other_current_assets = df.loc[chosen_ticker].iat[6]
# other_current_assets_upper = other_current_assets * 1.5
# other_current_assets_lower = other_current_assets * 0.5
# st.write("The current other_current_assets of the chosen ticker is " + str(other_current_assets))
# predicted_other_current_assets = st.slider("Predicted other_current_assets reported by " + chosen_ticker + ".", int(other_current_assets_lower), int(other_current_assets_upper), int(other_current_assets) )

# Ebit 
# st.subheader("Ebit")
# ebit = df.loc[chosen_ticker].iat[6]
# ebit_upper = 1
# ebit_lower = 0
# st.write("The current ebit of the chosen ticker is " + str(net_receivables))
# predicted_ebit = st.slider("Predicted ebit reported by " + chosen_ticker + ".", int(ebit_lower), int(ebit_upper), int(ebit) )

# totalRevenue
# st.subheader("Total Revenue")
# total_revenue = df.loc[chosen_ticker].iat[6]
# total_revenue_upper = total_revenue * 1.5
# total_revenue_lower = total_revenue * 0.5
# st.write("The current total_revenue of the chosen ticker is " + str(total_revenue))
# predicted_total_revenue = st.slider("Predicted total_revenue reported by " + chosen_ticker + ".", int(total_revenue_lower), int(total_revenue_upper), int(total_revenue) )

# totalOperatingExpenses
#st.subheader("Total Operating Expenses")
# total_operating_expenses = df.loc[chosen_ticker].iat[6]
# total_operating_expenses_upper = total_operating_expenses * 1.5
# total_operating_expenses_lower = total_operating_expenses * 0.5
# st.write("The current total_operating_expenses of the chosen ticker is " + str(total_operating_expenses))
# predicted_total_operating_expenses = st.slider("Predicted total_operating_expenses reported by " + chosen_ticker + ".", int(total_operating_expenses_lower), int(total_operating_expenses_upper), int(total_operating_expenses) )

# depreciation
st.subheader("Depreciation")
depreciation = df.loc[chosen_ticker].iat[6]
depreciation_upper = depreciation * 1.5
depreciation_lower = depreciation * 0.5
st.write("The current depreciation of the chosen ticker is " + str(depreciation))
predicted_cash = st.slider("Predicted depreciation reported by " + chosen_ticker + ".", int(depreciation_lower), int(depreciation_upper), int(depreciation) )

# dividendsPaid
#st.subheader("Dividends")
#dividends = df.loc[chosen_ticker].iat[6]
#dividends_upper = dividends * 1.5
#dividends_lower = dividends * 0.5
#st.write("The current dividends of the chosen ticker is " + str(dividends))
#predicted_dividends = st.slider("Predicted dividends reported by " + chosen_ticker + ".", int(dividends_lower), int(dividends_upper), int(dividends) ) 

# Market cap? 
st.subheader("The Resulting Market Cap")


# st.header("Default Values ", anchor=None)
# st.write("These are the default values for the existing ticker that will be incorporated into the model")
# # OutstandingShares
# # Depreciation
# # sellingGeneralAdministrative
# # Interest Expense
# # incomeTaxExpense
# # costOfRevenue
# # netIncomeFromContinuingOps
# # netIncomeApplicableToCommonShares
# # investments
# # changeToLiabilities
# # totalCashflowsFromInvestingActivities
# # totalCashFromFinancingActivities
# # changeToOperatingActivities
# # repurchaseOfStock
# # effectOfExchangeRate
# # totalCashFromOperatingActivities
# # changeToAccountReceivables
# # changeToNetincome
# # capitalExpenditures

st.header("Final Stock Price Prediction", anchor=None)
#INCOMPLETE - Need to add variable for the current share price of the selected stock. 
current_price = df.loc[chosen_ticker].iat[0]
current_price = int(current_price)
st.write('Current Share Price is' + str(current_price) )

#predicted_price
st.write('The predicted value of the share price based on the selections above is ' )


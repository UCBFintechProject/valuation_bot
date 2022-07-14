from collections import namedtuple
from multiprocessing.dummy import current_process
import altair as alt
import math
import pandas as pd
import streamlit as st
import pickle

from pathlib import Path
from sqlalchemy import create_engine


@st.experimental_memo(suppress_st_warning=True)
@st.experimental_memo(ttl=600)
def start():
    engine = create_engine('sqlite://', echo=False)
    data = Path("data/FS_sp500_merged_cleaned_stats.csv")
    df = pd.read_csv(data, delimiter=",").rename(columns={"Unnamed: 0":"Ticker"})
    df = df.set_index("Ticker")
    df.to_sql('merged_cleaned', con=engine)

    #engine.execute("ALTER TABLE merged_cleaned RENAME COLUMN [0] TO TICKER")
    #list = engine.execute("SHOW columns FROM merged_cleaned")

    dfsql = engine.execute("SELECT * FROM merged_cleaned").fetchall()

    st.dataframe(data=dfsql, width=None, height=None)
    #st.dataframe(data=list, width=None, height=None)

    index = df.index
    #index = pd.DataFrame(columns=["Ticker"])

    #Creates a new DF 
    tickers = pd.DataFrame(columns=["Ticker"])

    #For loop to add the ticker names into the ticker datafrmae 
    for i in index:
        tickers.loc[len(tickers.index)] = [i]
    # print (tickers)
    return tickers, df

tickers, df=start()

chosen_ticker = st.selectbox(
    'Which ticker would you like to predict the market cap of?',
    (tickers))
st.write('You selected:', chosen_ticker)


# query_name_columns = "CREATE TABLE data_table (`Ticker` VARCHAR(255) PRIMARY KEY, `RecentPrice` FLOAT(10,7) NOT NULL, `Beta` FLOAT(10,7) NOT NULL,`AnnualDividendRate` FLOAT(10,7) NOT NULL, `ROE(%)` FLOAT(10,7) NOT NULL, `ROA(%)` FLOAT(10,7) NOT NULL,
#     `ProfitMargin(%)` FLOAT(10,7) NOT NULL,
#     `TotalCash` FLOAT(10,7) NOT NULL,
#     `TotalDebt` FLOAT(10,7) NOT NULL,
#     `OutstandingShares` FLOAT(10,7) NOT NULL,
#     `intangibleAssets` FLOAT(10,7) NOT NULL,
#     `capitalSurplus` FLOAT(10,7) NOT NULL,
#     `totalLiab` FLOAT(10,7) NOT NULL,
#     `totalStockholderEquity` FLOAT(10,7) NOT NULL,
#     `otherCurrentLiab` FLOAT(10,7) NOT NULL,
#     `totalAssets` FLOAT(10,7) NOT NULL,
#     `commonStock` FLOAT(10,7) NOT NULL,
#     `otherCurrentAssets` FLOAT(10,7) NOT NULL,
#     `retainedEarnings` FLOAT(10,7) NOT NULL,
#     `otherLiab` FLOAT(10,7) NOT NULL,
#     `goodWill` FLOAT(10,7) NOT NULL,
#     `treasuryStock` FLOAT(10,7) NOT NULL,
#     `otherAssets` FLOAT(10,7) NOT NULL,
#     `cash` FLOAT(10,7) NOT NULL,
#     `totalCurrentLiabilities` FLOAT(10,7) NOT NULL,
#     `otherStockholderEquity` FLOAT(10,7) NOT NULL,
#     `propertyPlantEquipment` FLOAT(10,7) NOT NULL,
#     `totalCurrentAssets` FLOAT(10,7) NOT NULL,
#     `longTermInvestments` FLOAT(10,7) NOT NULL,
#     `netTangibleAssets` FLOAT(10,7) NOT NULL,
#     `netReceivables` FLOAT(10,7) NOT NULL,
#     `longTermDebt` FLOAT(10,7) NOT NULL,
#     `inventory` FLOAT(10,7) NOT NULL,
#     `accountsPayable` FLOAT(10,7) NOT NULL,
#     `shortLongTermDebt` FLOAT(10,7) NOT NULL,
#     `incomeBeforeTax` FLOAT(10,7) NOT NULL,
#     `netIncome` FLOAT(10,7) NOT NULL,
#     `sellingGeneralAdministrative` FLOAT(10,7) NOT NULL,
#     `grossProfit` FLOAT(10,7) NOT NULL,
#     `ebit` FLOAT(10,7) NOT NULL,
#     `operatingIncome` FLOAT(10,7) NOT NULL,
#     `interestExpense` FLOAT(10,7) NOT NULL,
#     `incomeTaxExpense` FLOAT(10,7) NOT NULL,
#     `totalRevenue`FLOAT(10,7) NOT NULL,
#     `totalOperatingExpenses` FLOAT(10,7) NOT NULL,
#     `costOfRevenue` FLOAT(10,7) NOT NULL,
#     `totalOtherIncomeExpenseNet` FLOAT(10,7) NOT NULL,
#     `netIncomeFromContinuingOps` FLOAT(10,7) NOT NULL,
#     `netIncomeApplicableToCommonShares` FLOAT(10,7) NOT NULL,
#     `investments` FLOAT(10,7) NOT NULL,
#     `changeToLiabilities` FLOAT(10,7) NOT NULL,
#     `totalCashflowsFromInvestingActivities` FLOAT(10,7) NOT NULL,
#     `totalCashFromFinancingActivities` FLOAT(10,7) NOT NULL,
#     `changeToOperatingActivities` FLOAT(10,7) NOT NULL,
#     `issuanceOfStock` FLOAT(10,7) NOT NULL,
#     `netIncome.1` FLOAT(10,7) NOT NULL,
#     `changeInCash` FLOAT(10,7) NOT NULL,
#     `repurchaseOfStock` FLOAT(10,7) NOT NULL,
#     `effectOfExchangeRate` FLOAT(10,7) NOT NULL,
#     `totalCashFromOperatingActivities` FLOAT(10,7) NOT NULL,
#     `depreciation` FLOAT(10,7) NOT NULL,
#     `otherCashflowsFromInvestingActivities` FLOAT(10,7) NOT NULL,
#     `dividendsPaid` FLOAT(10,7) NOT NULL,
#     `changeToAccountReceivables` FLOAT(10,7) NOT NULL,
#     `changeToNetincome` FLOAT(10,7) NOT NULL,
#     `capitalExpenditures` FLOAT(10,7) NOT NULL,
#     `netBorrowings` FLOAT(10,7) NOT NULL,
#     `otherCashflowsFromFinancingActivities` FLOAT(10,7) NOT NULL,
#     `MarketCap` FLOAT(10,7) NOT NULL
#     );"

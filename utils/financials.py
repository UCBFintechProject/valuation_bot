"""

NOTE: This is a modified version of an object class that inports data and also performs calculations that we need for valuation.
The MarketCap was missing too much data in teh stats file.  So we added OutstandingShare to the collectiuon process and calculated MarketCap afterwards right in the notebook.

SRC: https://www.kaggle.com/code/hanseopark/prediction-of-price-for-ml-with-finance-stats?scriptVersionId=67455884&cellId=5

"""
import json
import pandas as pd
import numpy as np


class VBot:
    def __init__(self, url, etfname):
        self.url = url
        self.etfname = etfname
        
    def get_ticker_list(self):
        df = self.get_stats()
        list_ticker = sorted(list(set(df['Ticker'].to_list())))

        return list_ticker

    def get_price_data(self, etf_list=[], OnlyRecent=False):
        self.etf_list = etf_list
        url_price = self.url+'/data_origin/FS_'+self.etfname+'_Value.json'
        combined_price = pd.read_json(url_price)
        df_price = pd.DataFrame({'Recent_price': []})

        if OnlyRecent == True:
            for symbol in self.etf_list:
                temp_df = combined_price[combined_price.Ticker.str.contains(symbol)].copy()
                res = temp_df.loc[temp_df.index[-1], 'Adj Close']
                df_price.loc[symbol, 'Recent_price'] =res
            return df_price
        else:
            df_price = combined_price.copy()
            return df_price
       
    def get_stats(self, preprocessing = False):
        url_stats = self.url+'/data_origin/FS_'+self.etfname+'_stats.json'
        df = pd.read_json(url_stats)
        if preprocessing == True:
            """
            NOTE: There are far too many missing values. 15:151 had values.
                  We'll simply recalculate MarketCap outside of this function.
                  
            """
            df_per = self.get_PER() # PER
            df_psr = self.get_PSR() # Price/Sales
            df_pbr = self.get_PBR() # Price/Book
            df_peg = self.get_PEG() # Price/Earning growth
            df_forper = self.get_FORPER() # Forward PER
            df_cap = self.get_CAP() # Market Cap

            # Concat mulit dataframe
            df = pd.concat([df_per, df_psr, df_pbr, df_peg, df_forper, df_cap], axis=1)
            
        return df

    def get_addstats(self, preprocessing = False):
        url_addstats = self.url+'/data_origin/FS_'+self.etfname+'_addstats.json'
        df = pd.read_json(url_addstats)
        if preprocessing == True:
            df_beta = self.get_Beta()
            df_divr = self.get_DivRate() # Annual diviend rate
            df_roe = self.get_ROE() # ROE
            df_roa = self.get_ROA() # ROA
            df_pm = self.get_PM() # Profit Margin
            df_cash = self.get_Cash() # Total Cash
            df_debt = self.get_Debt() # Total Debt
            ### Added
            df_outstanding = self.get_Out() # Get outstanding shares needed to calculate MCap
            # df_cap = self.get_CAP() # Market Cap
            
            # Concat mulit dataframe
            df = pd.concat([df_beta, df_divr, df_roe, df_roa, df_pm, df_cash, df_debt, df_outstanding], axis=1)

        return df   

    def get_balsheets(self, preprocessing = False):
        url_balsheets = self.url+'/data_origin/FS_'+self.etfname+'_balsheets.json'
        df = pd.read_json(url_balsheets)
        if preprocessing == True:
            df_ta = self.get_TA() # Total Assets

            df = pd.concat([df_ta], axis=1)

        return df
    
    def get_income(self, preprocessing = False):
        url_income = self.url+'/data_origin/FS_'+self.etfname+'_income.json'
        df = pd.read_json(url_income)
        if preprocessing == True:
            df_tr = self.get_TR() # Total revenue

            df = pd.concat([df_tr], axis=1)

        return df

    def get_flow(self, preprocessing = False):
        url_flow = self.url+'/data_origin/FS_'+self.etfname+'_flow.json'
        df = pd.read_json(url_flow)
        if preprocessing == True:
            df_div = self.get_DIV() # Dividends paid across companies
            df_iss = self.get_ISS() # Issuance information

            df = pd.concat([df_div, df_iss], axis=1)

        return df    
    
  ################################## get_stats()    
    
    def get_PER(self):
        df = self.get_stats()
        df_per = df[df.Attribute.str.contains('Trailing P/E')].copy()
        df_per['PER'] = df_per.loc[:, 'Recent']
        df_per = df_per.drop(['Attribute', 'Recent'], axis=1)
        df_per = df_per.set_index('Ticker')
        df_per = df_per.fillna(value=np.nan)
        df_temp = pd.DataFrame()
        for col in df_per.columns:
            df_temp[col] = pd.to_numeric(df_per[col], errors='coerce')
            
        return df_temp.astype(float)

    def get_PSR(self):
        df = self.get_stats()
        df_psr = df[df.Attribute.str.contains('Price/Sales')].copy()
        df_psr['PSR'] = df_psr.loc[:, 'Recent']
        df_psr = df_psr.drop(['Attribute', 'Recent'], axis=1)
        df_psr = df_psr.set_index('Ticker')
        df_psr = df_psr.fillna(value=np.nan)
        df_temp = pd.DataFrame()
        for col in df_psr.columns:
            df_temp[col] = pd.to_numeric(df_psr[col], errors='coerce')

        return df_temp.astype(float)

    def get_PBR(self):
        df = self.get_stats()
        df_pbr = df[df.Attribute.str.contains('Price/Book')].copy()
        df_pbr['PBR'] = df_pbr.loc[:, 'Recent']
        df_pbr = df_pbr.drop(['Attribute', 'Recent'], axis=1)
        df_pbr = df_pbr.set_index('Ticker')

        return df_pbr.astype(float)

    def get_PEG(self):
        df = self.get_stats()
        df_peg = df[df.Attribute.str.contains('PEG')].copy()
        df_peg['PEG'] = df_peg.loc[:, 'Recent']
        df_peg = df_peg.drop(['Attribute', 'Recent'], axis=1)
        df_peg = df_peg.set_index('Ticker')

        return df_peg.astype(float)

    def get_FORPER(self):
        df = self.get_stats()
        df_forper = df[df.Attribute.str.contains('Forward P/E')].copy()
        df_forper['forPER'] = df_forper.loc[:, 'Recent']
        df_forper = df_forper.drop(['Attribute', 'Recent'], axis=1)
        df_forper = df_forper.set_index('Ticker')
        df_temp = pd.DataFrame()
        for col in df_forper.columns:
            df_temp[col] = pd.to_numeric(df_forper[col], errors='coerce')

        return df_temp
    def get_CAP(self):
        df = self.get_stats()
        df_cap = df[df.Attribute.str.contains('Cap')].copy()
        df_cap['marketCap'] = df_cap.loc[:, 'Recent']
        df_cap = df_cap.drop(['Attribute', 'Recent'], axis=1)
        df_cap = df_cap.set_index('Ticker')
        # df_outstanding = self.get_Out() # Get outstanding shares needed to calculate MCap
        # df_cap['MarketCap'] = get_Out()
        df_cap = df_cap.fillna(value=np.nan)
        for ticker in df_cap.index:
            value = df_cap.loc[ticker, 'marketCap']
            if type(value) == str:
                value = float(value.replace('.','').replace('T','0000000000').replace('B','0000000'). replace('M','0000').replace('k','0'))
            df_cap.loc[ticker, 'marketCap'] = value

        return df_cap.astype(float)
    
    

    
############################## get_addstats()
    
    def get_Beta(self):
        df = self.get_addstats()
        df_beta = df[df.Attribute.str.contains('Beta')].copy()
        df_beta['Beta'] = df_beta.loc[:, 'Value']
        df_beta = df_beta.drop(['Attribute', 'Value'], axis=1)
        df_beta = df_beta.set_index('Ticker')

        return df_beta.astype(float)
    
    def get_DivRate(self):
        df = self.get_addstats()
        df_divr = df[df.Attribute.str.contains('Trailing Annual Dividend Rate')].copy()
        df_divr['AnnualDividendRate']= df_divr.loc[:, 'Value']
        df_divr = df_divr.drop(['Attribute', 'Value'], axis=1)
        df_divr = df_divr.set_index('Ticker')

        return df_divr.astype(float)

    def get_ROE(self):
        df = self.get_addstats()
        df_roe = df[df.Attribute.str.contains('Return on Equity')].copy()
        df_roe['ROE(%)'] = df_roe.loc[:, 'Value']
        df_roe = df_roe.drop(['Attribute', 'Value'], axis=1)
        df_roe = df_roe.set_index('Ticker')
        df_roe = df_roe.fillna(value=np.nan)
        for ticker in df_roe.index:
            value = df_roe.loc[ticker, 'ROE(%)']
            if type(value) == str:
                value = float(value[:-1].replace(',',''))
            df_roe.loc[ticker, 'ROE(%)'] = value

        return df_roe.astype(float)

    def get_ROA(self):
        df = self.get_addstats()
        df_roa = df[df.Attribute.str.contains('Return on Assets')].copy()
        df_roa['ROA(%)'] = df_roa.loc[:, 'Value']
        df_roa = df_roa.drop(['Attribute', 'Value'], axis=1)
        df_roa = df_roa.set_index('Ticker')
        df_roa = df_roa.fillna(value=np.nan)
        for ticker in df_roa.index:
            value = df_roa.loc[ticker, 'ROA(%)']
            if type(value) == str:
                value = float(value[:-1])
            df_roa.loc[ticker, 'ROA(%)'] = value

        return df_roa.astype(float)

    def get_PM(self):
        df = self.get_addstats()
        df_pm = df[df.Attribute.str.contains('Profit Margin')].copy()
        df_pm['ProfitMargin(%)'] = df_pm.loc[:, 'Value']
        df_pm = df_pm.drop(['Attribute', 'Value'], axis=1)
        df_pm = df_pm.set_index('Ticker')
        df_pm = df_pm.fillna(value=np.nan)
        for ticker in df_pm.index:
            value = df_pm.loc[ticker, 'ProfitMargin(%)']
            if type(value) == str:
                value = float(value[:-1])
            df_pm.loc[ticker, 'ProfitMargin(%)'] = value

        return df_pm.astype(float)
    
    def get_Cash(self):
        df = self.get_addstats()
        df_cash = df[df.Attribute.str.contains('Total Cash Per Share')].copy()
        df_cash['TotalCash'] = df_cash.loc[:, 'Value']
        df_cash = df_cash.drop(['Attribute', 'Value'], axis=1)
        df_cash = df_cash.set_index('Ticker')

        return df_cash.astype(float)

    def get_Debt(self):
        df = self.get_addstats()
        df_debt = df[df.Attribute.str.contains('Total Debt/Equity')].copy()
        df_debt['TotalDebt'] = df_debt.loc[:, 'Value']
        df_debt = df_debt.drop(['Attribute', 'Value'], axis=1)
        df_debt = df_debt.set_index('Ticker')

        return df_debt.astype(float)    
    
    def get_Out(self):
        df = self.get_addstats()
        df_outstanding = df[df.Attribute.str.contains('Shares Outstanding 5')].copy()
        df_outstanding['OutstandingShares'] = df_outstanding.loc[:, "Value"]
        df_outstanding = df_outstanding.drop(['Attribute', 'Value'], axis=1)
        df_outstanding = df_outstanding.set_index('Ticker')
        
        for ticker in df_outstanding.index:
            value = df_outstanding.loc[ticker, 'OutstandingShares']
            if type(value) == str:
                value = float(value.replace('.','').replace('T','0000000000').replace('B','0000000'). replace('M','0000').replace('k','0'))
            df_outstanding.loc[ticker, 'OutstandingShares'] = value
            
        return df_outstanding.astype(float)

##########################################################    
    def get_TA(self):
        df = self.get_balsheets()
        df_ta = df[df.Breakdown == 'totalAssets'].copy()
        df_ta['TotalAssets'] = df_ta.loc[:, 'Recent']
        df_ta = df_ta.drop(['Breakdown', 'Recent'], axis=1)
        df_ta = df_ta.set_index('Ticker')

        return df_ta
    
    def get_TR(self):
        df = self.get_income()
        df_tr = df[df.Breakdown == 'totalRevenue'].copy()
        df_tr['TotalRevenue'] = df_tr.loc[:, 'Recent']
        df_tr = df_tr.drop(['Breakdown', 'Recent'], axis=1)
        df_tr = df_tr.set_index('Ticker')

        return df_tr
    
    def get_DIV(self):
        df = self.get_flow()
        df_div = df[df.Breakdown == 'dividendsPaid'].copy()
        df_div['DividendsPaid'] = df_div.loc[:, 'Recent']
        df_div = df_div.drop(['Breakdown', 'Recent'], axis=1)
        df_div = df_div.set_index('Ticker')

        return df_div

    def get_ISS(self):
        df = self.get_flow()
        df_iss = df[df.Breakdown == 'issuanceOfStock'].copy()
        df_iss['Issuance'] = df_iss.loc[:, 'Recent']
        df_iss = df_iss.drop(['Breakdown', 'Recent'], axis=1)
        df_iss = df_iss.set_index('Ticker')

        return df_iss

    ############################## Callable per element (Ticker or list)
  
    def get_stats_element(self, etf_list =['AAPL']):
        df_stats = self.get_stats()
        self.etf_list = etf_list
        temp_df = df_stats[df_stats.Ticker == etf_list[0]].copy()
        list_df = temp_df['Attribute'].to_list()
        df = pd.DataFrame(columns=list_df, index = self.etf_list)
        for ticker in self.etf_list:
            temp_df = df_stats[df_stats.Ticker == ticker].copy()
            list_df = temp_df['Attribute'].to_list()
            for att in list_df:
                temp_df_stats = df_stats[df_stats.Attribute == att].copy()
                temp_df_stats = temp_df_stats.set_index('Ticker')
                df.loc[ticker, att] = temp_df_stats.loc[ticker, 'Recent']

        return df
    
    def get_addstats_element(self, etf_list =['AAPL']):
        df_stats = self.get_addstats()
        self.etf_list = etf_list
        temp_df = df_stats[df_stats.Ticker == etf_list[0]].copy()
        list_df = temp_df['Attribute'].to_list()
        df = pd.DataFrame(columns=list_df, index = self.etf_list)
        for ticker in self.etf_list:
            temp_df = df_stats[df_stats.Ticker == ticker].copy()
            list_df = temp_df['Attribute'].to_list()
            for att in list_df:
                temp_df_stats = df_stats[df_stats.Attribute == att].copy()
                temp_df_stats = temp_df_stats.set_index('Ticker')
                df.loc[ticker, att] = temp_df_stats.loc[ticker, 'Value']

        return df
   
    def get_balsheets_element(self, etf_list =['AAPL']):
        df_stats = self.get_balsheets()
        self.etf_list = etf_list
        temp_df = df_stats[df_stats.Ticker == etf_list[0]].copy()
        list_df = temp_df['Breakdown'].to_list()
        df = pd.DataFrame(columns=list_df, index = self.etf_list)
        for ticker in self.etf_list:
            temp_df = df_stats[df_stats.Ticker == ticker].copy()
            list_df = temp_df['Breakdown'].to_list()
            for att in list_df:
                temp_df_stats = df_stats[df_stats.Breakdown == att].copy()
                temp_df_stats = temp_df_stats.set_index('Ticker')
                df.loc[ticker, att] = temp_df_stats.loc[ticker, 'Recent']

        return df.astype(float)
    
    def get_income_element(self, etf_list =['AAPL']):
        df_stats = self.get_income()
        self.etf_list = etf_list
        temp_df = df_stats[df_stats.Ticker == etf_list[0]].copy()
        list_df = temp_df['Breakdown'].to_list()
        df = pd.DataFrame(columns=list_df, index = self.etf_list)
        for ticker in self.etf_list:
            temp_df = df_stats[df_stats.Ticker == ticker].copy()
            list_df = temp_df['Breakdown'].to_list()
            for att in list_df:
                temp_df_stats = df_stats[df_stats.Breakdown == att].copy()
                temp_df_stats = temp_df_stats.set_index('Ticker')
                df.loc[ticker, att] = temp_df_stats.loc[ticker, 'Recent']

        return df.astype(float)
    
    
    def get_flow_element(self, etf_list =['AAPL']):
        df_stats = self.get_flow()
        self.etf_list = etf_list
        temp_df = df_stats[df_stats.Ticker == etf_list[0]].copy()
        list_df = temp_df['Breakdown'].to_list()
        df = pd.DataFrame(columns=list_df, index = self.etf_list)
        for ticker in self.etf_list:
            temp_df = df_stats[df_stats.Ticker == ticker].copy()
            list_df = temp_df['Breakdown'].to_list()
            for att in list_df:
                temp_df_stats = df_stats[df_stats.Breakdown == att].copy()
                temp_df_stats = temp_df_stats.set_index('Ticker')
                df.loc[ticker, att] = temp_df_stats.loc[ticker, 'Recent']

        return df.astype(float)

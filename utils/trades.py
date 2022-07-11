"""
NOTE: Something something


"""
import json
import pandas as pd
import numpy as np

class VBotTrade:
    def __init__(self, url, etfname):
        self.url = url
        self.etfname = etfname

    def get_tickers(self, preprocessing = False):
        url_stats = self.url+'/data_origin/FS_'+self.etfname+'_stats.json'
        df = pd.read_json(url_stats)            
        return df
    
    def get_ticker_list(self):
        df = self.get_tickers()
        list_ticker = sorted(list(set(df['Ticker'].to_list())))
        return list_ticker
    
    def get_trades(self):        
        url_trades = self.url+'/data_origin/FS_'+self.etfname+'_Value.json'
        df = pd.read_json(url_trades).rename(columns={"Recent_price":"RecentPrice"})
        return df

    
    def get_trades_element(self, etf_list =['AAPL']):
        df = self.get_trades()
        df = df.loc[df['Ticker'].isin(etf_list)]
        return df
   

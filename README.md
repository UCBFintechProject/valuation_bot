# valuation_bot

Valuebot allows users to conduct valuation predictions based on fundamental analysis in seconds. 
The Application uses public financial statement data to train machine learning models which return solid valuation  predictions. The goal of the program is to reduce the time spent on fundamental analysis by both financial professionals and the end investor. 
 
Functionality:
The program starts by importing financial statement data located in csv files(located under data folder). Then, it utilizes this data to train a Random Forest Regression ML model(located in 2_analysis_RFR_model.ipynb). Subsequently, the training data is passed through by Standard scaler function which improves the quality of the end predictions. The App is programmed to calculate/predict "Market Cap" value yet this figure can be replaced by any of the categories contained in the data set.  

CUI:

In order to provide full functionality, the app can be ran through Streamlit(Code under ui_2.py). The interface will prompt the user to enter a stock Symbol. It will then return a list of financial figures some of them can be adjusted according to the user's forecast and generate predictions based on these numbers.


## Technologies

This project leverages python 3.9

CUI(Command User Interface) Streamlit highly recommended.  


## Installation Guide

os
json
pandas 
numpy 
hvplot
seaborn
matplotlib.pyplot
%matplotlib inline
pathlib
sklearn.
pickle 

import warnings
# Custom classes for interfacing with this dataset
from utils.financials import VBot
from utils.trades import VBotTrade


## Contributors

Abhi Banerjee
Phoebe Gunter
Harry Oestreicher
Javier Leon


![Regressor_Estimators](https://user-images.githubusercontent.com/101846233/179379779-fbe88eb2-32e7-498f-92f6-570eeeb01f20.png)



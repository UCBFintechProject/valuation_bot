# Executive Summary
To explore the tricky problem of Valuing public companies by applying Machine Learning techniques to all reported Financial results, instead of traditional metrics like Price to Earnings Ratio etc.

Combine Stock trading data with key Financial Statement results for each publicly traded company, to achieve:
1. Classification: discover similarities between companies' financial performance and Valuation multiples.
2. Prediction: forecast Valuation metrics like Free Cash Flow and changes in Market Capitalization.
3. Back-testing: compare various trading strategies using all non-derived financial reporting metrics.

The predictive gain from using quarterly data is larger for asset-heavy industries and industries with higher levels of earnings smoothness.  This is why we selected S&P500 stocks.

Applying Time series / Moving averages modelling techniques to historical Financial Statements data, to find direct evidence on the usefulness of quarterly data in predicting future operating cash flows. This in turn, can provide a better Machine Learning model for implementing Robo-Advisers that can suggest Buy, Sell or Hold recommendations based on whether  a current Stock Price is UnderValued, OverValued or Fairly Valued, according to the model that crunches through historical financial reports along with trading price data.


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
xgboost


## Contributors

Abhi Banerjee
Phoebe Gunter
Harry Oestreicher
Javier Leon


![Data](https://user-images.githubusercontent.com/101846233/179379873-9471d465-12aa-4f86-b702-a0214e47fd99.png)


![Regressor1](https://user-images.githubusercontent.com/101846233/179379844-ab616b11-d825-4941-8116-34bcf690c445.png)



![Regressor_Estimators](https://user-images.githubusercontent.com/101846233/179379779-fbe88eb2-32e7-498f-92f6-570eeeb01f20.png)



![Regressor_Pred](https://user-images.githubusercontent.com/101846233/179379852-8b9f2fed-5eaf-41c2-be90-0d4dce9e3990.png)


![Regressor_chart](https://user-images.githubusercontent.com/101846233/179379862-3fed4ec0-c601-4153-a550-2ce851fd3675.png)



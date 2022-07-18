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

## Technologeis Used

* Python (Anaconda)
* Jupyterlab
* Pandas
* sklearn (KMeans, PCA, StandardScaler)
* HvPlot

## Getting Started & Running the code...

1. Create a conda environment and activate it

**(base)**
```bash
conda create -n value_bot python=3.7 anaconda -y
conda activate value_bot

```
2. Install the required packages (make sure `crypto_investments` is activated first)

**(value_bot)**
```bash
python -m ipykernel install --user --name value_bot
conda install -c conda-forge nodejs -y
conda install -c pyviz hvplot -y
pip install -U scikit-learn
pip install matplotlib
pip install pickle-mixin

```

3. Clone this repository, then clone and run the Jupyter notebook.

**(value_bot)**
```bash
git clone git@github.com:UCBFintechProject/valuation_bot.git
cd valuation_bot/
jupyter lab

```

Notebook Reference: 
1. Data Retrieval
2. Analysis - Neural Network
3. Analysis - Random Forest Regressor
4. Analysis - XGBoost

Presentation of Data Analysis:

**(value_bot)**
```bash
streamlit run ui.py

```
![screenshot](https://github.com/UCBFintechProject/valuation_bot/tree/main/images/file.png)

## Conclusions:



## Contributors

- Abhi Banerjee
- Phoebe Gunter
- Harry Oestreicher
- Javier Leon


![Data](https://user-images.githubusercontent.com/101846233/179379873-9471d465-12aa-4f86-b702-a0214e47fd99.png)


![Regressor1](https://user-images.githubusercontent.com/101846233/179379844-ab616b11-d825-4941-8116-34bcf690c445.png)



![Regressor_Estimators](https://user-images.githubusercontent.com/101846233/179379779-fbe88eb2-32e7-498f-92f6-570eeeb01f20.png)



![Regressor_Pred](https://user-images.githubusercontent.com/101846233/179379852-8b9f2fed-5eaf-41c2-be90-0d4dce9e3990.png)


![Regressor_chart](https://user-images.githubusercontent.com/101846233/179379862-3fed4ec0-c601-4153-a550-2ce851fd3675.png)



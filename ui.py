from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

from pathlib import Path

"""
# Welcome to the UC Berkeley Fintech Bootcamp Project 2 Group 2 Valuation Bot!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

"""


data = Path("data/FS_sp500_merged_cleaned_stats.csv")
df = pd.read_csv(data, delimiter=",").rename(columns={"Unnamed: 0":"Ticker"})
df = df.set_index("Ticker")

print(list(df.columns))

index = df.index
print(index)

tickers = pd.DataFrame(columns=["Ticker"])

#df=pd.DataFrame(columns=['a'])

for i in index:
    tickers.loc[len(tickers.index)] = [i]
    #tickers.append(i)


#df = pd.DataFrame(data)


print (tickers)


#list_of_tickers_df = df["Ticker"]

option = st.selectbox(
    tickers)

 #st.write('You selected:', option)

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


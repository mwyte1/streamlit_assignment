import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

top_five = pd.read_excel("Final Spreadsheet Compilation.xlsx")

st.write(top_five)

st.sidebar.header("Please choose 2 variable to compare.")
x_val = st.sidebar.selectbox("Pick your x-axis", list(top_five.columns))
y_val = st.sidebar.selectbox("Pick your y-axis", list(top_five.columns))
selection = st.sidebar.selectbox("Choose your filter criteria", list(top_five.columns))

scatter = alt.Chart(top_five, title=f"Correlation between {x_val} and {y_val}").mark_point().encode(
    alt.X(x_val,title=f'{x_val}', scale = alt.Scale(zero=False)),
    alt.Y(y_val,title=f'{y_val}', scale = alt.Scale(zero=False, padding=1)),
    color = selection
    )
st.altair_chart(scatter, use_container_width=True)

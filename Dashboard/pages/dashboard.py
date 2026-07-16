import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px

#page configuration

st.title("Car Crashes Dashboard")

st.set_page_config(
    page_title= "Car Crashes Dashboard",
    page_icon= "🏎️",
    layout= "wide"
)

df = sns.load_dataset("car_crashes")
df["State"] = df["abbrev"]

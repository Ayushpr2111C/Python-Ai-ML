from pandas import col
import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px

#page configuration

st.set_page_config(
    page_title= "Car Crashes Dashboard",
    page_icon= "🏎️",
    layout= "wide"
)

# Load the car crashes 
df = sns.load_dataset("car_crashes")
df["State"] = df["abbrev"]

# Create a sidebar for user input
st.sidebar.title("User Input Features")
selected_states = st.sidebar.multiselect(
    label="Select States",
    options=df["State"].unique(),
    default=df["State"].unique()
)

#Title for the dashboard
st.title("Car Crashes Dashboard")
st.dataframe(df)

#KPI cards
col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Total Crashes", 
    round(df['total'].mean()),"%"
)

col2.metric(
    "Average Alcohol Crashes",
    round(df['alcohol'].mean()),"%"
)

col3.metric(
    "Average Speeding Crashes",
    round(df['speeding'].mean()), "%"
)


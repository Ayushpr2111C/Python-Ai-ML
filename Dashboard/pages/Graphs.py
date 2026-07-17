import streamlit as st
import plotly.express as px
import seaborn as sns

df = sns.load_dataset("car_crashes")
df["State"] = df["abbrev"]

st.set_page_config(
    page_title= "Car Crashes Graphs",
    page_icon= "🏎️",
    layout= "wide"
)

options = st.selectbox(
    label="Select Graph Type",
    options=["Bar Chart","Line Chart","Scatter Plot"]
)
x_terminal = st.selectbox(
    label="Select X-axis", 
    options=df.columns
)

if options == "Bar Chart":
    fig = px.bar(df, x=x_terminal, y="total", color_continuous_scale="Viridis", template="plotly_dark", title=f"Total Car Crashes by {x_terminal}")
    st.plotly_chart(fig)
elif options == "Line Chart":
    fig = px.line(df, x=x_terminal, y="total", template="plotly_dark", title=f"Total Car Crashes by {x_terminal}")
    st.plotly_chart(fig)
elif options == "Scatter Plot":
    fig = px.scatter(df, x=x_terminal, y="total",color_continuous_scale="Viridis", size="total", template="plotly_dark", title=f"Total Car Crashes vs {x_terminal}")
    st.plotly_chart(fig)

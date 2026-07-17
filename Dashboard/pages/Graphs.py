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
    options=["Bar Chart","Line Chart","Scatter Plot","Pie Chart"]
)

if options == "Bar Chart":
    fig = px.bar(df, x='State', y="total",color="total", color_continuous_scale="Viridis", template="plotly_dark", title=f"Total Car Crashes by State")
    st.plotly_chart(fig)
elif options == "Line Chart":
    fig = px.line(df, x='State', y="total", template="plotly_dark", title=f"Total Car Crashes by State")
    st.plotly_chart(fig)
elif options == "Scatter Plot":
    fig = px.scatter(df, x='State', y="total",color="total", color_continuous_scale="Viridis", size="total", template="plotly_dark", title=f"Total Car Crashes vs State")
    st.plotly_chart(fig)
elif options == "Pie Chart":
    val= st.selectbox(
        label="Select Value for Pie Chart",
        options=["total","speeding","alcohol","not_distracted","no_previous"]
    )

    fig = px.pie(df, values=val, names='total', template="plotly_dark",color_discrete_sequence=px.colors.sequential.Viridis , title=f"Distribution of {val.replace('_', ' ').title()}")
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig)
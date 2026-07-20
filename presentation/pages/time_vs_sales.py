import streamlit as sns
import streamlit as st
import pandas as pd 
import plotly.express as px
import numpy as nm

df = pd.read_csv("sales_data.csv")

button = st.button("↩ Previous Page")
if button:
    st.switch_page("pages/region_vs_category.py")

st.markdown("<hr style='border:1px solid #eee; margin:20px 0;'>", unsafe_allow_html=True)

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_sales = (
    df.groupby(
        pd.Grouper(
            key="Order_Date",
            freq="ME"
        )
    )["Sales"]
    .sum()
    .reset_index()
)

top_month = monthly_sales.loc[
    monthly_sales["Sales"].idxmax()
]

low_month = monthly_sales.loc[
    monthly_sales["Sales"].idxmin()
]

average_sales = round(monthly_sales["Sales"].mean())

top_pct = round(
    ((top_month["Sales"] - average_sales)
    / average_sales) * 100,
    2
)

low_pct = round(
    ((average_sales - low_month["Sales"])
    / average_sales) * 100,
    2
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Top Month",
    top_month["Order_Date"].strftime("%B %Y"),
    f"+{top_pct}% above average"
)

col2.metric(
    "Low Month",
    low_month["Order_Date"].strftime("%b %Y"),
    f"-{low_pct}% below average"
)

col3.metric(
    "Average Sales",
    f"₹{average_sales}",
    "avg"
)


#graphs
fig = px.line(monthly_sales, x="Order_Date", y="Sales", title="Monthly Sales Over Time")
fig = px.line(monthly_sales,x="Order_Date",y="Sales",title="Monthly Sales Trend")
fig.update_traces(mode="lines+markers")
st.plotly_chart(fig)


st.write("""### Executive Summary

The Time vs Sales analysis highlights the monthly sales performance over the two-year period from January 2023 to December 2024. Sales exhibit noticeable fluctuations throughout the timeline, indicating the presence of seasonal trends and varying customer demand patterns.

The highest monthly sales were recorded in August 2023, reaching approximately ₹3.70 lakh, while November 2023 experienced the lowest sales at approximately ₹1.91 lakh. This represents a decline of nearly 48.4% between the peak and lowest-performing months.

A recurring pattern can be observed across both years, with sales generally increasing during the April–August period before declining toward the end of the year. This consistency suggests the existence of seasonal buying behavior within the customer base.

Furthermore, monthly sales remained relatively stable throughout 2024, with no extreme deviations from historical trends, indicating a healthy and predictable revenue stream.

Overall, the analysis demonstrates a well-maintained sales trajectory while identifying seasonal peaks that can be leveraged for future marketing campaigns, inventory planning, and business forecasting.""")


st.markdown("<hr style='border:1px solid #eee; margin:20px 0;'>", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col7:
    if st.button("Next page ↪", key="header_time_sales"):
        st.switch_page("pages/category_vs_sales.py")
        
st.markdown("<h3 style='text-align: center; color: white;'>Created by Ayush Pratap</h3>", unsafe_allow_html=True)
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

#useful for kpi cards
sales= df.groupby("Category")["Sales"].sum().sort_values(ascending= False)
top_category = sales.index[0]
top_category_sales = round(sales.iloc[0])
average_sales = round(sales.mean())
top_ = round(((top_category_sales - average_sales)/average_sales)*100)

#kpi cards
col1, col2, col3 = st.columns(3)

col1.metric(
    "Top Category", 
    top_category, 
)

col2.metric(
    "Top Category Sales", 
    top_category_sales,
    f"{top_}% above average" 
)

col3.metric(
    "Average Sales", 
    average_sales, 
    "avg."
)


fig = px.pie(df, values= 'Sales', names='Category', template="plotly_dark",color_discrete_sequence=px.colors.sequential.Viridis, title=f"Sales by Category")
fig.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig)    

st.write("""### Executive Summary

The Category vs Sales analysis demonstrates a significant imbalance in revenue contribution across the organization's product categories. Technology emerges as the dominant category, generating approximately ₹37.68 lakh in sales and accounting for nearly 61% of total category revenue.

Furniture ranks second with sales of ₹18.38 lakh, trailing Technology by approximately 51.2%, while Office Supplies contribute the least at ₹5.61 lakh. In fact, Technology generates approximately 571.5% more revenue than Office Supplies, highlighting the organization's strong dependence on technology-related products.

Additionally, Furniture records over three times the sales of Office Supplies, indicating that customer demand is heavily concentrated within the Technology and Furniture segments.

Overall, the findings suggest that while the Technology category remains the primary driver of business growth, Office Supplies present an opportunity for strategic expansion through targeted marketing initiatives, product diversification, and improved market positioning.""")


st.markdown("<hr style='border:1px solid #eee; margin:20px 0;'>", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col7:
    if st.button("Next page ↪", key="header_time_sales"):
        st.switch_page("pages/state_vs_sales.py")
        
st.markdown("<h3 style='text-align: center; color: white;'>Created by Ayush Pratap</h3>", unsafe_allow_html=True)
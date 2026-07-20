import streamlit as st
import pandas as pd 
import plotly.express as px
import numpy as nm

df = pd.read_csv("sales_data.csv")

button = st.button("↩ Previous Page")
if button:
    st.switch_page("pages/region_vs_sales.py")

st.markdown("<hr style='border:1px solid #eee; margin:20px 0;'>", unsafe_allow_html=True)

#useful for kpi cards
sales= df.groupby("Region")["Sales"].sum().sort_values(ascending= False)
top_region = sales.index[0]
top_region_sales = round(sales.iloc[0])
average_sales = round(sales.mean())
top_ = round(((top_region_sales - average_sales)/average_sales)*100)

#kpi cards
col1, col2, col3 = st.columns(3)

col1.metric(
    "Top Region", 
    top_region, 
)

col2.metric(
    "Top Region Sales", 
    top_region_sales,
    f"{top_}% above average"
)

col3.metric(
    "Average Sales", 
    average_sales,
    "avg"
)

fig = px.density_heatmap(df,x="Category", y="Region", z="Sales", color_continuous_scale="Viridis", template="plotly_dark", histfunc="sum", text_auto= ".2s")
st.plotly_chart(fig)

st.write("""### Executive Summary

- Technology is the dominant product category across all five regions, consistently outperforming Furniture and Office Supplies.

- The Central Region records the highest overall revenue at approximately ₹14.04 lakh, while the East Region generates the lowest revenue at ₹9.16 lakh, representing a performance gap of 34.8%.

- Central also leads Technology sales with ₹8.71 lakh, exceeding the East Region's Technology revenue by approximately 44.7%.

- Office Supplies remain the weakest category across every region, contributing less than 15% of total regional revenue in all cases.

- These findings indicate a strong dependence on Technology products while highlighting opportunities to strengthen Office Supplies and improve performance within the East Region.

- Technology is the highest-selling category in every region.
         
- However, the East Region records only ₹4.81 lakh in Technology sales, which is 44.7% lower than the Central Region.

- East is the lowest-performing region overall, suggesting untapped market potential.

- Office Supplies remain the weakest category across all five regions.

- The findings indicate strong demand for Technology products but highlight the need to strengthen sales performance in the East Region.                  """)

st.markdown("<hr style='border:1px solid #eee; margin:20px 0;'>", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col7:
    if st.button("Next page ↪", key="header_time_sales"):
        st.switch_page("pages/time_vs_Sales.py")
        
st.markdown("<h3 style='text-align: center; color: white;'>Created by Ayush Pratap</h3>", unsafe_allow_html=True)
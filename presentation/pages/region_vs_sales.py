import streamlit as sns
import streamlit as st
import pandas as pd 
import plotly.express as px
import numpy as nm

df = pd.read_csv("sales_data.csv")

button = st.button("↩ Home")
if button:
    st.switch_page("home.py")

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
    "avg."
)

fig = px.bar(df.sort_values('Sales', ascending=True), x='Region', y="Sales",color="Sales", color_continuous_scale="Viridis", template="plotly_dark", title=f"Region vs Sales")
st.plotly_chart(fig)

st.write("""### Executive Summary

The Region vs Sales analysis highlights significant variations in revenue generation across the five regions. The Central Region emerges as the top-performing market, recording total sales of ₹14.04 lakh, followed by the North Region (₹13.28 lakh) and the West Region (₹12.95 lakh).

While the top four regions maintain relatively comparable performance, the East Region records the lowest sales at ₹9.16 lakh, generating approximately 34.8% less revenue than the Central Region. This indicates a substantial performance gap and suggests the presence of untapped market potential within the East Region.

Furthermore, the difference between the Central and North Regions is only 5.4%, demonstrating healthy competition among the leading markets. The North, West, and South Regions all operate within a 13% range of the market leader, reflecting a well-distributed sales ecosystem.

Overall, the findings suggest that the organization benefits from a geographically diversified revenue stream, with the Central Region serving as the primary contributor while the East Region presents opportunities for targeted growth initiatives and strategic investment. """)

st.write('''### Key Takeaways

- Central is the highest-performing region with sales of ₹14.04 lakh.
- North and West closely follow, trailing the leader by 5.4% and 7.8%, respectively.
- East is the lowest-performing region, generating 34.8% less revenue than Central.
- Four out of five regions perform within 13% of the market leader, indicating balanced sales distribution.
- The East Region represents the strongest opportunity for future business expansion. ''')

st.markdown("<hr style='border:1px solid #eee; margin:20px 0;'>", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col7:
    if st.button("Next page ↪", key="header_time_sales"):
        st.switch_page("pages/region_vs_category.py")
        
st.markdown("<h3 style='text-align: center; color: white;'>Created by Ayush Pratap</h3>", unsafe_allow_html=True)
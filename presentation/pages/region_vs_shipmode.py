import streamlit as sns
import streamlit as st
import pandas as pd 
import plotly.express as px
import numpy as nm

df = pd.read_csv("sales_data.csv")

button = st.button("↩ Previous Page")
if button:
    st.switch_page("pages/age_vs_category.py")

st.markdown("<hr style='border:1px solid #eee; margin:20px 0;'>", unsafe_allow_html=True)

#useful for kpi cards
sales= df.groupby("Ship_Mode")["Sales"].sum().sort_values(ascending= False)
top_ShipMode = sales.index[0]
top_ShipMode_sales = round(sales.iloc[0])
low_ShipMode = sales.index[-1]
low_ShipMode_sales = round(sales.iloc[-1])
average_sales = round(sales.mean())
top_ = round(((top_ShipMode_sales - average_sales)/average_sales)*100)
low_ = round(((low_ShipMode_sales - average_sales)/average_sales)*100)

#kpi cards 
col1, col2= st.columns(2)
with col1:
    st.metric(
        "Highest in use",
        top_ShipMode,
        f"{top_}% higher"
    )

with col2:
    st.metric(
        "Lowest in use",
        low_ShipMode,
        f"{low_}% lesser"
    )

#graoh
fig = px.sunburst(df, path=["Region", "Category"],values="Sales",title="Region → Category → Sales", template= "plotly_dark",color="Sales", color_continuous_scale="Viridis_r")
st.plotly_chart(fig)

st.write("""### Executive Summary

The Region vs Ship Mode analysis reveals a consistent customer preference for Standard Class shipping across all regions. Standard Class dominates order volume in every market, with the South and West regions recording the highest usage at 352 orders each.

In contrast, Same Day delivery remains the least utilized shipping option throughout all regions, with order counts ranging from just 50 to 66. This suggests that customers generally prioritize cost-effectiveness over expedited delivery services.

The Central, North, South, and West regions exhibit relatively similar shipping patterns, indicating a stable and predictable distribution network. However, the East Region records the lowest order counts across all shipping methods, highlighting comparatively lower customer activity within that market.

Furthermore, Second Class consistently ranks as the second most popular shipping option, followed by First Class, demonstrating a clear hierarchy in customer shipping preferences.

Overall, the findings indicate that customer behavior remains highly consistent regardless of geographic location, with Standard Class serving as the preferred delivery method and Same Day shipping representing a niche service with limited demand.""")
st.write("""### Key Takeaways
- Standard Class is the most preferred shipping mode across all five regions.
- South and West lead Standard Class usage with 352 orders each.
- Same Day delivery is the least utilized shipping option in every region.
- East records the lowest order volume across all shipping methods.
- Customer shipping preferences remain highly consistent regardless of region.""")



st.markdown("<hr style='border:1px solid #eee; margin:20px 0;'>", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col7:
    if st.button("Next page ↪", key="header_time_sales"):
        st.switch_page("pages/state_vs_sales.py")
        
st.markdown("<h3 style='text-align: center; color: white;'>Created by Ayush Pratap</h3>", unsafe_allow_html=True)
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

#usefull for kpi cards 
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

#graph

fig = px.density_heatmap(df, x="Category", y="Ship_Mode", z= "Sales", color_continuous_scale="Viridis", template="plotly_dark", histfunc="sum", text_auto= ".2s",title="Sales in every Category by Each Shipment Method")
st.plotly_chart(fig)

st.write("""### Executive Summary

The Ship Mode vs Category analysis highlights a strong relationship between shipping preferences and product categories. Standard Class emerges as the most frequently utilized shipping method, generating the highest sales across all categories and contributing significantly to the organization's overall revenue.

Technology products shipped through Standard Class record the highest sales at approximately ₹20.0 lakh, emphasizing both the popularity of Technology products and the customer preference for cost-effective shipping options. In contrast, Same Day delivery remains the least utilized shipping method, indicating that customers are generally willing to trade delivery speed for lower shipping costs.

Across all four shipping methods, Technology consistently outperforms Furniture and Office Supplies, reinforcing its position as the primary revenue driver of the business. Furthermore, Standard Class contributes more than half of total sales, while Same Day shipping accounts for only a small fraction of overall revenue.

Overall, the findings suggest that customers prioritize affordability and convenience over expedited shipping, while also highlighting the continued dominance of Technology products across every shipping category.""")

st.write(""" ### Key Takeaways 
- Standard Class is the most preferred shipping method across all product categories.
- Same Day delivery is the least utilized shipping option.
- Technology products shipped via Standard Class generate the highest revenue (~₹20 lakh).
- Technology remains the top-selling category regardless of shipping method.
- Customer behavior indicates a preference for economical shipping over faster delivery options.""")



st.markdown("<hr style='border:1px solid #eee; margin:20px 0;'>", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col7:
    if st.button("Next page ↪", key="header_time_sales"):
        st.switch_page("pages/region_vs_shipmode.py")
        
st.markdown("<h3 style='text-align: center; color: white;'>Created by Ayush Pratap</h3>", unsafe_allow_html=True)
import streamlit as st
import pandas as pd 
import plotly.express as px
import numpy as nm
df = pd.read_csv("sales_data.csv")

button = st.button("↩ Return")
if button:
    st.switch_page("home.py")
st.markdown("<hr style='border:1px solid #eee; margin:20px 0;'>", unsafe_allow_html=True)

#useful for kpi cards
sales= df.groupby("State")["Sales"].sum().sort_values(ascending= False)
top_state = sales.index[0]
runner_up = sales.index[1]
last = sales.index[-1]

top_state_sales = round(sales.iloc[0])
runner_up_sales = round(sales.iloc[1])
last_sales = round(sales.iloc[-1])

average_sales = round(sales.mean())

top_ = round(((top_state_sales - average_sales)/average_sales)*100)
top_1 = round(((runner_up_sales - average_sales)/average_sales)*100)
low = round(((last_sales - average_sales)/average_sales)*100)

#kpi cards
col1, col2, col3= st.columns(3)

col1.metric("Leader", "Chhattisgarh",f"{top_}% above avg")
col2.metric("Runner Up", "Haryana", f"{top_1}% above avg")
col3.metric("Lowest", "Odisha", f"{low}% below avg")

#graph
fig = px.bar(df.sort_values('Sales', ascending= True),x='State', y='Sales', color = 'Sales',color_continuous_scale='Viridis',
                 template='plotly_dark',
                 title="Sales in each states")
st.plotly_chart(fig)

#analysis
st.write("""The State vs Sales analysis reveals a strong and relatively balanced sales distribution across the organization's leading markets. Chhattisgarh emerges as the top-performing state with total sales of ₹5.09 lakh, followed closely by Haryana (1.3% lower), Maharashtra (3.5% lower), Madhya Pradesh (7.3% lower), and Karnataka (8.0% lower).

The narrow variance among the top five states—each performing within approximately 10% of the market leader—indicates that revenue generation is not concentrated in a single region. Instead, the business benefits from a diversified and resilient sales footprint across multiple high-performing markets.

Conversely, the lower end of the distribution highlights significant performance gaps. Odisha records the lowest sales at ₹2.57 lakh, representing a decline of approximately 49.4% compared to Chhattisgarh. Similarly, Bihar and West Bengal trail the leading state by 36.2% and 34.3%, respectively.

From a strategic standpoint, these findings suggest two key priorities:

Protect and strengthen high-performing markets that consistently contribute significant revenue.
Investigate and improve underperforming regions through targeted marketing campaigns, enhanced customer outreach, and market-specific growth strategies.

Overall, the analysis demonstrates a well-diversified sales ecosystem, with the top five states contributing consistently while also highlighting opportunities for expansion in regions currently underperforming relative to the market leader.""")



st.markdown("<hr style='border:1px solid #eee; margin:20px 0;'>", unsafe_allow_html=True)
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col7:
    if st.button("Next page ↪", key="header_time_sales"):
        st.switch_page("pages/thankyou.py")
st.markdown("<h3 style='text-align: center; color: white;'>Created by Ayush Pratap</h3>", unsafe_allow_html=True)
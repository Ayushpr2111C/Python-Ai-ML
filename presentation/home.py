import streamlit as st 

def Header():
    st.markdown("<hr style='border:1px solid #eee; margin:20px 0;'>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        if st.button("Sales V/s Regions", key="header_sales_region"):
            st.switch_page("pages/region_vs_sales.py")

    with col2:
        if st.button("Category V/s Region", key="header_category_region"):
            st.switch_page("pages/region_vs_category.py")

    with col3:
        if st.button("Time V/s Sales", key="header_time_sales"):
            st.switch_page("pages/time_vs_Sales.py")

    with col4:
        if st.button("Category V/s Sales", key="header_category_sales"):
            st.switch_page("pages/category_vs_sales.py")

    with col5:
        if st.button("Ship V/s Category", key="header_age_category"):
            st.switch_page("pages/age_vs_category.py")

    with col6:
        if st.button("Region V/s ShipMode", key="header_region_shipmode"):
            st.switch_page("pages/region_vs_shipmode.py")

    with col7:
        if st.button("State V/s Sales", key="header_state_sales"):
            st.switch_page("pages/state_vs_sales.py")


def Explore_Dashboard():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 📊 Sales Across the regions")
        st.write("Distributions, correlations & category trends")
        if st.button("Open Sales Across Regions", key="explore_sales_region"):
            st.switch_page("pages/region_vs_sales.py")

    with col2:
        st.markdown("### 🌍 Per Category sales data across regions")
        st.write("Trends, top categories & demographics")
        if st.button("Open Category vs Region", key="explore_category_region"):
            st.switch_page("pages/region_vs_category.py")

    with col3:
        st.markdown("### 🕒 Sales with Time")
        st.write("Analyze sales over time")
        if st.button("Open Time vs Sales", key="explore_time_sales"):
            st.switch_page("pages/time_vs_Sales.py")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🛒 Category vs Sales")
        st.write("Trends, top categories & demographics")
        if st.button("Open Category vs Sales", key="explore_category_sales"):
            st.switch_page("pages/category_vs_sales.py")

    with col2:
        st.markdown("### 👥 Ship Mode vs Category")
        st.write("Trends, top categories & demographics")
        if st.button("Open Ship Mode vs Category", key="explore_age_category"):
            st.switch_page("pages/age_vs_category.py")

    with col3:
        st.markdown("### 🚚 Region vs Ship Mode")
        st.write("Trends, top categories & demographics")
        if st.button("Open Region vs Ship Mode", key="explore_region_shipmode"):
            st.switch_page("pages/region_vs_shipmode.py")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 📈 State vs Sales")
        st.write("Trends, top categories & demographics")
        if st.button("Open State vs Sales", key="explore_state_sales"):
            st.switch_page("pages/state_vs_sales.py")


                
st.markdown("<H1 style='text-align: center; color: white;'>Sales Analysis Dashboard</h1>", unsafe_allow_html=True)
Header()
st.markdown("<hr style='border:1px solid #eee; margin:20px 0;'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown('''Welcome to the Sales Analysis Dashboard, an interactive data visualization project developed using Streamlit and Plotly. This dashboard provides valuable insights into sales performance across different regions, states, product categories, customer demographics, and shipping methods. The primary objective of this project is to transform raw sales data into meaningful visualizations that help identify trends, patterns, and business opportunities.
''')

with col2:
    st.image("sales.png")

st.markdown('''
    Using powerful and interactive Plotly graphs, users can explore various aspects of the dataset to better understand customer behavior, regional performance, and product demand. The dashboard has been designed with a simple and user-friendly interface to make data exploration both efficient and engaging.
            
    The following analyses have been included in this project:

    - 🌍 Region v/s Product Category
    - 💰 Region v/s Sales
    - 🕒 Time v/s Sales
    - 📈 State vs Sales
    - 🛒 Category v/s Sales
    - 👥 Age v/s Category
    - 🚚 Region v/s Ship Mode

    Each section presents interactive visualizations and insights that contribute to a comprehensive understanding of the sales dataset. We hope this dashboard demonstrates the effectiveness of data analytics and visualization techniques in supporting informed business decisions.
    ''')


st.subheader("Explore the Dashboard")
Explore_Dashboard()


st.markdown("<hr style='border:1px solid #eee; margin:20px 0;'>", unsafe_allow_html=True)
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col7:
    if st.button("Next page ↪", key="header_time_sales_1"):
        st.switch_page("pages/region_vs_sales.py")
st.markdown("<h3 style='text-align: center; color: white;'>Created by Ayush Pratap</h3>", unsafe_allow_html=True)
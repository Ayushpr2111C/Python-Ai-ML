import streamlit as st


button = st.button("↩ Home")
if button:
    st.switch_page("home.py")


st.markdown("""
<style>
.title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: #4CAF50;
    margin-top: 100px;
}

.subtitle {
    text-align: center;
    font-size: 25px;
    color: white;
    margin-top: 20px;
}

.footer {
    text-align: center;
    font-size: 18px;
    color: gray;
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🎉 Thank You!</div>',
    unsafe_allow_html=True
)

st.markdown(
    '''
    <div class="subtitle">
        Thank you for exploring the Sales Analysis Dashboard.<br>
        This project demonstrates the power of Python, Streamlit, and Plotly
        in transforming raw sales data into meaningful business insights.
    </div>
    ''',
    unsafe_allow_html=True
)

st.markdown(
    '''
    <div class="footer">
        Presented by<br>
        <b>Ayush Pratap</b><br>
    </div>
    ''',
    unsafe_allow_html=True
)

st.balloons() 

st.markdown(
    "<center><i>'Without data, you're just another person with an opinion.' – W. Edwards Deming</i></center>",
    unsafe_allow_html=True
)
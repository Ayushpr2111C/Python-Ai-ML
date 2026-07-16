import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("Welcome to my Calulator")
st.markdown("Performs all the operation easily")

c1,c2=st.columns(2)
fnum = c1.number_input("Enter first number",value=0)
snum = c2.number_input("Enter second number", value=0)

operations = ["Add","Sub","Mul","Div"]
choice = st.radio("Select an operation",operations)

button = st.button("Calculate")

result = 0
if button:
    if choice=="Add":
        result = fnum+snum
    if choice=='sub':
        result = fnum-snum
    if choice=='Mul':
        result= fnum*snum
    if choice == 'Div':
        result= fnum/snum
st.success(f"Result is {result}")

st.balloons()
st.snow()
import streamlit as st
import numpy as np
import joblib

model = joblib.load("laptop_price_predictor_rf.pkl")

st.title("Laptop Price Prediction")
st.write("Enter Laptop Specifications: ")

ram = st.select_slider("Select RAM (GB):",
                       options=[2,4,6,8,12,16,24,32,64],
                       value = 8 # This will be default starting value
                       )
weight = st.select_slider("Select Weight(kg): ",
                          options=[1.0,1.5,2.0,2.5,3.0,3.5],
                          value= 1.0)

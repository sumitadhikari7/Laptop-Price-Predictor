import streamlit as st
import numpy as np
import joblib

model = joblib.load("laptop_price_predictor_rf.pkl")

st.title("Laptop Price Prediction")
st.write("Enter Laptop Specifications: ")
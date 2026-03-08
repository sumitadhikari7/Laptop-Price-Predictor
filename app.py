import streamlit as st
import numpy as np
import joblib

model = joblib.load("laptop_price_predictor_rf.pkl")
model_cols = joblib.load("model-columns.pkl")

st.title("Laptop Price Prediction")

features = np.zeros(len(model_cols))

def set_feature(name, value):
    if name in model_cols:
        features[model_cols.index(name)] = value

st.header("Enter Laptop Specifications: ")


inches = st.slider("Select Inches: ",
                    min_value=10.0,
                    max_value=18.0,
                    value=15.0,
                    step = 0.1 
                    )
ram = st.select_slider("Select RAM (GB):",
                       options=[2,4,6,8,12,16,24,32,64],
                       value = 8 # This will be default starting value
                       )
weight = st.select_slider("Select Weight(kg): ",
                          options=[1.0,1.5,2.0,2.5,3.0,3.5],
                          value= 1.0)
ssd = st.select_slider("Select SSD (GB)",
                       options=[0,8,16,32,64,128,180,240,256,512,1000],
                       value=0)
hdd = st.select_slider("Select HDD (GB)",
                       options=[0,32,128,500,1000,2000],
                       value=0)
touchscreen = st.selectbox("Touchscreen", options=["No", "Yes"])
ips = st.selectbox("IPS Display", options=["No", "Yes"])

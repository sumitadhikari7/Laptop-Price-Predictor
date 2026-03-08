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
touchscreen = 1 if touchscreen == "Yes" else 0

ips = st.selectbox("IPS Display", options=["No", "Yes"])
ips = 1 if ips == "Yes" else 0

x_res = st.select_slider("Resolution Width",
                    options= [1366,1440,1600,1920,2160,2256,2304,2400,2560,2736,2880,3200,3840],
                    value=1366)
y_res = st.select_slider("Resolution Height: ",
                         options=[768,900,1080,1200,1440,1504,1600,1800,1824,2160],
                         value=768)
ppi = np.sqrt(x_res**2 + y_res**2) / inches

set_feature("Inches", inches)
set_feature("Ram", ram)
set_feature("Weight", weight)
set_feature("SSD", ssd)
set_feature("HDD", hdd)
set_feature("Touchscreen", touchscreen)
set_feature("Ips", ips)
set_feature("X_res", x_res)
set_feature("Y_res", y_res)
set_feature("PPI", ppi)

st.header("Laptop Details")

def choose_option(prefix):
    options = [col.replace(prefix +"_","") for col in model_cols if col.startswith(prefix + "_")]
    selected = st.selectbox(prefix, options)
    set_feature(f"{prefix}_{selected}", 1)

choose_option("Company")
choose_option("TypeName")
choose_option("OpSys")
choose_option("Cpu_Brand")
choose_option("Gpu_Brand")

if st.button("Predict Price"):
    prediction = model.predict([features])[0]

    st.subheader("Estimated Laptop Price: ")
    st.success(f"{prediction:.2f} (Euros)")


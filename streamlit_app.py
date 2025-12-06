import streamlit as st
import requests
import json

st.title("(KNN Model)")

# ✅ Pull secrets from the DATABRICKS section
TOKEN = st.secrets["DATABRICKS"]["TOKEN"]
ENDPOINT_URL = st.secrets["DATABRICKS"]["ENDPOINT_URL"]

product_position = st.selectbox("Product Position", ["Aisle", "Front", "Back"])
product_category = st.selectbox("Category", ["Clothing", "Accessories"])
seasonal = st.selectbox("Seasonal", ["Yes", "No"])
brand = st.selectbox("Brand", ["Zara"])
sales_volume = st.number_input("Sales Volume", min_value=0)
price = st.number_input("Price", min_value=0)

if st.button("Predict"):

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "dataframe_records": [{
            "product_position": product_position,
            "product_category": product_category,
            "seasonal": seasonal,
            "sales_volume": int(sales_volume),
            "brand": brand,
            "name": "Unknown",
            "description": "None",
            "price": float(price),
            "currency": "USD",
            "section": "General"
        }]
    }

    try:
        response = requests.post(ENDPOINT_URL, headers=headers, json=payload)
        st.write("Status:", response.status_code)

        if response.status_code == 200:
            st.success(f"Prediction: {response.json()}")
        else:
            st.error(f"Error {response.status_code}: {response.text}")

    except Exception as e:
        st.error(f"Exception: {str(e)}")




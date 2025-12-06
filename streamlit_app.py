import streamlit as st
import requests
import json

st.title("Zara Promo Dependence Predictor (KNN Model)")

ENDPOINT_URL = "https://dbc-a4fffd05-8bae.cloud.databricks.com/serving-endpoints/zara-knn-endpoint/invocations"
TOKEN = "dapi54363c5219dad6c93a76ad902a141b7d"

product_position = st.selectbox("Product Position", ["Aisle", "Front", "Back", "Checkout"])
promotion = st.selectbox("Promotion", ["Yes", "No"])
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
        "sales_volume": sales_volume,
        "brand": brand,
        "name": "Unknown",
        "description": "None",
        "price": price,
        "currency": "USD",
        "section": "None"
    }]
}

    response = requests.post(ENDPOINT_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result}")
    else:
        st.error(f"Error {response.status_code}: {response.text}")


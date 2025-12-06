import streamlit as st
import requests
import json

st.title("Zara Promo Dependence Predictor (KNN Model)")

ENDPOINT_URL = "YOUR_ENDPOINT_URL"
TOKEN = "YOUR_TOKEN"

product_position = st.selectbox("Product Position", ["Aisle", "End-cap"])
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
            "promotion": promotion,
            "product_category": product_category,
            "seasonal": seasonal,
            "brand": brand,
            "sales_volume": sales_volume,
            "price": price
        }]
    }

    response = requests.post(ENDPOINT_URL, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            result = response.json()
            st.success(f"Predicted Value: {result}")
        except Exception:
            st.write(response.text)
    else:
        st.error(f"Error: {response.text}")

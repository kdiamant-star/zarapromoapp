import streamlit as st
import requests
import json

st.title("👔🛍️👘Zara Item Promotion Decider👖🎩👗")

ENDPOINT_URL = st.secrets["DATABRICKS"]["ENDPOINT_URL"]
TOKEN = st.secrets["DATABRICKS"]["TOKEN"]

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
            result = response.json()

            # ⭐ NEW: Clean extraction of prediction
            pred_value = result.get("predictions", [None])[0]

            # ⭐ NEW: Beautiful human-readable output
            if pred_value == 1:
                st.success("🔥 Prediction: PROMOTE THIS ITEM (1)")
            elif pred_value == 0:
                st.info("ℹ️ Prediction: DO NOT PROMOTE (0)")
            else:
                st.warning(f"Unexpected prediction format: {result}")

            # Optional: Show raw response for debugging
            # st.write("Raw output:", result)

        else:
            st.error(f"Error {response.status_code}: {response.text}")

    except Exception as e:
        st.error(f"Exception: {str(e)}")





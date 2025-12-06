import streamlit as st
import requests
import json

st.title("👗 Zara Item Promotion Decider 👔")

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

          
            pred_value = result.get("predictions", [None])[0]

            if pred_value == 1:
                st.success("🔥 Prediction: PROMOTE THIS ITEM (1)")
            elif pred_value == 0:
                st.info("ℹ️ Prediction: DO NOT PROMOTE (0)")
            else:
                st.warning(f"Unexpected prediction format: {result}")

            
         

        else:
            st.error(f"Error {response.status_code}: {response.text}")

    except Exception as e:
        st.error(f"Exception: {str(e)}")

import streamlit as st
import base64


def add_bg_from_url(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


add_bg_from_url("https://wallpapers.com/background/zara-background-q43a5kgakrkmybzd.html")





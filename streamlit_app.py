import streamlit as st
import requests
import json

st.markdown("""
    <style>
    /* Make success/error/info boxes fully opaque */
    .stAlert {
        background-color: rgba(30, 30, 30, 0.95) !important; 
        color: white !important;
        border-radius: 10px;
        padding: 15px;
    }

    /* Fix text color inside alert */
    .stAlert p {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Change the main title color */
    h1 {
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("👗 Zara Item Promotion Decider 👔")

ENDPOINT_URL = st.secrets["DATABRICKS"]["ENDPOINT_URL"]
TOKEN = st.secrets["DATABRICKS"]["TOKEN"]

product_position = st.selectbox("Product Position", ["Aisle", "Front", "Back"])
product_category = st.selectbox("Category", ["Clothing", "Accessories"])
seasonal = st.selectbox("Seasonal", ["Yes", "No"])
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


add_bg_from_url("https://cdn.prod.website-files.com/64830736e7f43d491d70ef30/64bfca456e3a5a803618a25d_64a5802512ee9430c0eafec6_64a2d408d2249c6450b8989f_zara-large.webp")





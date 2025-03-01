import streamlit as st
import cython_api
import json

# Streamlit Dark Theme
st.set_page_config(page_title="Market Taking", layout="wide")

# Custom CSS for Dark Theme
st.markdown("""
    <style>
        body { background-color: #121212; color: white; }
        .stButton>button { background-color: white; color: black; border-radius: 10px; }
        .stTextInput>div>div>input { background-color: #1E1E1E; color: white; border: 1px solid #444; }
        .stSlider>div>div>div>div { background-color: #00b894; }
        .stDataFrame { background-color: #1E1E1E; }
    </style>
""", unsafe_allow_html=True)

st.title("Market Taking")

# User inputs API key
api_key = st.text_input("Enter your API Key", type="password")

if not api_key:
    st.warning("Please enter your API key to continue.")
    st.stop()

# Fetch and display balances
balances = cython_api.get_funds(api_key)
inr_balance = balances.get("INR", 0)
usdt_balance = balances.get("USDT", 0)

col1, col2 = st.columns(2)
col1.metric("INR Balance", f"₹ {inr_balance}")
col2.metric("USDT Balance", f"$ {usdt_balance}")

# Fetch USDT Price
usdt_price = cython_api.get_usdt_price()
col1, col2 = st.columns(2)
col1.metric("USDT Price (Buy)", usdt_price["buy"], delta_color="inverse")
col2.metric("USDT Price (Sell)", usdt_price["sell"], delta_color="normal")

# Profit Percentage Slider
profit_percentage = st.slider("Profit %", min_value=0, max_value=20, value=10)

# Fetch and Display Order Book
orders = cython_api.get_orders(api_key)

# Debugging: Print the response to check its structure
st.write("API Response for Orders:", orders)

# Ensure `orders` is a list before iterating
if not isinstance(orders, list):
    st.error("Unexpected API response format. Check logs for details.")
    st.stop()

# Convert orders to table format
table_data = []
for order in orders:
    if isinstance(order, dict):  # Ensure it's a dictionary
        table_data.append([
            order.get("type", "").capitalize(),
            order.get("market", "N/A"),
            order.get("price", 0),
            order.get("floor", 0),
            profit_percentage,
            order.get("profit", 0),
            "Trade"
        ])


# Display Orders in Table
st.table(table_data)

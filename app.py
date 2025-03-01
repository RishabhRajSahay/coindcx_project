import streamlit as st
import cython_api
import json

st.title("Crypto Trading Dashboard")

# Fetch symbols data
symbols = cython_api.get_symbols()
selected_symbol = st.selectbox("Select Trading Pair", symbols)

# Fetch Order Book
if st.button("Get Order Book"):
    order_book = cython_api.get_order_book(selected_symbol)
    st.json(order_book)

# Check Funds
if st.button("Check Funds"):
    funds = cython_api.get_funds()
    st.json(funds)

# Place an Order
order_type = st.selectbox("Order Type", ["buy", "sell"])
price = st.number_input("Price")
quantity = st.number_input("Quantity")
if st.button("Place Order"):
    response = cython_api.place_order(selected_symbol, order_type, price, quantity)
    st.json(response)

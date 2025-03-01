from requests import post, get
import json

cdef str BASE_URL = "https://api.coindcx.com"

def get_symbols():
    response = get(f"{BASE_URL}/exchange/v1/markets")
    return response.json()

def get_order_book(str symbol):
    response = get(f"{BASE_URL}/exchange/v1/depth", params={"pair": symbol})
    return response.json()

def get_funds():
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    response = get(f"{BASE_URL}/exchange/v1/users/balances", headers=headers)
    return response.json()

def place_order(str symbol, str order_type, float price, float quantity):
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    data = {
        "market": symbol,
        "side": order_type,
        "price": price,
        "quantity": quantity,
        "order_type": "limit_order"
    }
    response = post(f"{BASE_URL}/exchange/v1/orders/create", headers=headers, json=data)
    return response.json()

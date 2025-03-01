from requests import post, get
import json

cdef str BASE_URL = "https://api.coindcx.com"

def get_symbols():
    response = get(f"{BASE_URL}/exchange/v1/markets")
    return response.json()

def get_order_book(str symbol):
    response = get(f"{BASE_URL}/exchange/v1/depth", params={"pair": symbol})
    return response.json()

def get_funds(str api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    response = get(f"{BASE_URL}/exchange/v1/users/balances", headers=headers)
    return response.json()

def get_usdt_price():
    response = get(f"{BASE_URL}/exchange/v1/markets")
    
    try:
        data = response.json()  # Ensure we parse JSON correctly
        
        if isinstance(data, list):  # Ensure it's a list of dictionaries
            for item in data:
                if isinstance(item, dict) and item.get("market") == "USDT-INR":
                    return {"buy": item.get("buy", 0), "sell": item.get("sell", 0)}
                    
    except Exception as e:
        print("Error fetching USDT price:", e)
    
    return {"buy": 0, "sell": 0}  # Return default values if API fails

def get_orders(str api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    response = get(f"{BASE_URL}/exchange/v1/orders", headers=headers)

    try:
        data = response.json()  # Ensure correct JSON parsing

        if isinstance(data, list):  # Ensure we received a list
            return data

    except Exception as e:
        print("Error fetching orders:", e)

    return []  # Return an empty list if API call fails


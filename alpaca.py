import requests, json
from config import *

APCA_API_BASE_URL='https://paper-api.alpaca.markets'

ACCOUNT_URL = '{}/v2/account'.format(APCA_API_BASE_URL)
ORDERS_URL = '{}/v2/orders'.format(APCA_API_BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

# get account info
def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)

info = get_account()
print(info)

# submit a new order
def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    return json.loads(r.content)

response = create_order("PTON", 100, "sell", "market", "day")
print(response)

# check open orders
def get_orders():
    r = requests.get(ORDERS_URL, headers=HEADERS)
    return json.loads(r.content)

orders = get_orders()
print(orders)





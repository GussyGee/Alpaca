import config, json
import websocket

# send authentication data and subscribe to stream
def on_open(ws):
    print("opened")
    auth_data = {
        "action": "auth",
        "key": config.API_KEY,
        "secret": config.SECRET_KEY
    }
    ws.send(json.dumps(auth_data))
    listen_message = {"action": "subscribe", "quotes": ["PTON"]}
    ws.send(json.dumps(listen_message))

# print confirmation to console when payload received
def on_message(ws, message):
    print("received a message")
    print(message)

# print confirmation that connection is closed to console
def on_close(ws):
    print("closed connection")

# define websocket and invoke functions
socket = "wss://stream.data.alpaca.markets/v2/iex"
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()
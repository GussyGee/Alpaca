import config, json
import websocket

# wscat -c wss://stream.data.alpaca.markets/v2/iex
# {"action": "auth", "key": "PKTS7T5474RJFXA5N68G", "secret": "5prqSY2CZRb1zUN4JF534i8LTFgx733uVOCtj5J8"}

# # for minute bars
# {"action": "subscribe", "bars": ["AMD"]}


def on_open(ws):
    print("opened")
    auth_data = {
        "action": "auth",
        "key": config.API_KEY,
        "secret": config.SECRET_KEY
    }

    ws.send(json.dumps(auth_data))

    listen_message = {"action": "subscribe", "bars": ["AMD"]}

    ws.send(json.dumps(listen_message))


def on_message(ws, message):
    print("received a message")
    print(message)

def on_close(ws):
    print("closed connection")

socket = "wss://stream.data.alpaca.markets/v2/iex"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()
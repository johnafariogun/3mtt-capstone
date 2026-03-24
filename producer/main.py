import websocket
import json

SOCKET_URL = "wss://ws.coincap.io/prices?assets=bitcoin,ethereum"

def on_message(ws, message):
    data = json.loads(message)
    print(f"Received Live Data: {data}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("### Connection Closed ###")

if __name__ == "__main__":
    ws = websocket.WebSocketApp(SOCKET_URL,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
    
    print("Connecting to Crypto Stream...")
    try:
        ws.run_forever()
    except KeyboardInterrupt:
        print("Stopping the stream...")

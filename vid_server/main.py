import cv2
import numpy as np
import base64
from websocket_server import WebsocketServer

def new_client(client, server):
    print(f"New client connected and was given id {client['id']}")

def client_left(client, server):
    print(f"Client({client['id']}) disconnected")

def message_received(message):
    # Assuming the message is the base64-encoded image
    img_data = base64.b64decode(message)
    nparr = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img is not None:
        cv2.imshow("Stream", img)
        cv2.waitKey(1)

# Create a websocket server
server = WebsocketServer(host='', port=6789)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
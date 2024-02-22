# pip install websocket-client
# pip install opencv-python-headless


import cv2
import base64
import websocket
import threading

def send_video(ws):
    # Connect to webcam by inputing 0 to vid capture
    try:
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        print("Capturing webcam")
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                _, buffer = cv2.imencode('.jpg', frame)
                ws.send(base64.b64encode(buffer).decode('utf-8'))

            # Adjust the sleep time to match the desired frame rate
            cv2.waitKey(10)
    except:
        print("Cam failed")
    finally:
        cap.release()

def on_open(ws):
    print("Opened connection")
    # Start sending video in another thread
    threading.Thread(target=send_video, args=(ws,)).start()

if __name__ == "__main__":
    # Replace 'localhost' with your server's IP if necessary
    ws = websocket.WebSocketApp("ws://10.110.218.20:6789",
                                on_open=on_open)
    ws.run_forever()
    while True:
        print('hi')
# pip install websocket-client
# pip install opencv-python-headless

import cv2
import base64
import websocket
import threading
import time

class vidClient():
    def __init__(self, ip, port):
        
        server_thread = threading.Thread(target=self.__startClient, args=(ip, port))
        server_thread.daemon = True
        server_thread.start()

    def __startClient(self, ip, port):
        destination = f"ws://{ip}:{port}"
        retry_interval = 3  # Time to wait between connection attempts, in seconds
        while True:
            try:
                print("destination:", destination)

                ws = websocket.WebSocketApp(destination,
                                        on_open=self.on_open)
                ws.run_forever()
            except:
                print(f"Connection failed")
                time.sleep(retry_interval)  # Wait before retrying
                continue  # Retry connection
    
    def on_open(self, ws):
        # Connect to webcam by inputing 0 to vid capture
        try:
            cap = cv2.VideoCapture(0) # this is for windows but will be adjusted
            print("capture cam")
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
            print("released camera")
            cap.release()

if __name__ == "__main__":
    print("Starting client")
    sendVideo = vidClient("192.168.254.20", 6789)
    while True:
        print("Running background")
        time.sleep(1)
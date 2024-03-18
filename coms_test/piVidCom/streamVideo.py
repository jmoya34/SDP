from webStream import startStream
from vidReceive import vidClient
import time

class streamVideo():
    def __init__(self, ip, port):
        vidStream = startStream()
        time.sleep(5) # Allow the camera local stream to start
        sendVideo = vidClient("47.148.234.28", 6789)
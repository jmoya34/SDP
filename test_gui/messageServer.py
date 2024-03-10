import socket

class sendCommand():
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def sendMsg(self, msg):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            #convert the msg string into bytes
            info = msg.encode('utf-8')
            s.sendall(info)
            data = s.recv(1024)
        print('Confirmation from server', repr(data))
# Echo client program
import socket

HOST = '10.110.220.71'    # The remote host
PORT = 65432              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Confirmation from server', repr(data))
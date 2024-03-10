import socket

# Set the host and port
HOST = ''  # Available to all platforms
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the address and port
    s.bind((HOST, PORT))
    # Start listening for incoming connections
    s.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        # Accept a new connection
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                # Receive data from the client
                data = conn.recv(1024)
                if not data:
                    break  # Break the loop if no more data is received
                # Print received data
                print('Received', repr(data))
                print('Data type:', type(repr(data))) # repr turns the bytes into a string
                # Echo the received data back to the client
                conn.sendall(b'Data received')
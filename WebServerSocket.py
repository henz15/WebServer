from cgitb import html
from socket import *
import sys
import time
from datetime import datetime

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 6570

# Create socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((SERVER_HOST, SERVER_PORT))
serverSocket.listen(1)
print("\nListening on port ", SERVER_PORT)

current_time = datetime.now().strftime("%H:%M:%S")
print("\n Server started at", current_time)
print("\nReady to serve...")

while True:    
    # Wait for client connections
    connectionSocket, connectionAddress = serverSocket.accept()
    try:
        # Get the client request
        request = connectionSocket.recv(1024).decode()
        print("\n" + request)

        # Get html file
        htmlFile = open('./index.html')
        content = htmlFile.read()
        htmlFile.close()

        # Send HTTP response
        response = 'HTTP/1.1 200 OK\n\n' + content
        connectionSocket.sendall(response.encode())
        connectionSocket.close()

    except IOError:
        # Send http 404
        connectionSocket.sendall("\nHTTP/1.1 404 Not Found\n\n".encode())
        connectionSocket.close()
        
serverSocket.close()
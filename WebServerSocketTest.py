from socket import *
import sys
import time
from datetime import datetime

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 6570

# Create socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((SERVER_HOST, SERVER_PORT))
serverSocket.listen(1)
# active for 1 minute
serverSocket.settimeout(60)
print("\n" + 'Listening on port ', SERVER_PORT)

timeBegin = time.time()


def get_currentTime(action):
    current_time = datetime.now().strftime("%H:%M:%S")
    print("\n" + 'Server', action, 'at', current_time)


def get_timeElapsed(seconds):
    timeEnd = time.time()
    timeElapsed = timeEnd - timeBegin

    if timeElapsed > seconds:
        # stop Server
        connectionSocket.close()
        serverSocket.close()
        get_currentTime('stopped')
        sys.exit()


get_currentTime('started')
print("\n"+'Ready to serve...')

while True:
    # Wait for client connections
    connectionSocket, connectionAddress = serverSocket.accept()
    try:
        # Run for 60 seconds (1 minute)
        get_timeElapsed(60)

        # Get the client request
        request = connectionSocket.recv(1024).decode()
        print("\n"+request)

        # Get html file
        fin = open('./index.html')
        content = fin.read()
        fin.close()

        # Send HTTP response
        response = 'HTTP/1.1 200 OK\n\n' + content
        connectionSocket.sendall(response.encode())
        connectionSocket.close()

    except IOError:
        # Send http 404
        connectionSocket.sendall("\nHTTP/1.1 404 Not Found\n\n".encode())
        connectionSocket.close()
        # Retry for 20 seconds
        get_timeElapsed(20)

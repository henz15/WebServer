import time
from socket import *

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1.0)
message = 'ping'
address = ("localhost", 6767)

for sequence_number in range(1,11):
    start = time.time()
    client_socket.sendto(message.encode(), address)
    try:
        response_message, server = client_socket.recvfrom(1024)
        end = time.time()
        RTT = end - start
        #print(f'{sequence_number} {response_message} {RTT}')
        print('\n#',sequence_number, 'Response_message:',response_message.decode(),  'RTT: ',RTT,' seconds')
    except timeout:
        print('# ',sequence_number)
        print('Request timed out')
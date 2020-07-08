import random
from socket import *
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 7777))
print('Ping Server Ready...')
while True:
    rand = random.randint(0, 10)
    message, address = serverSocket.recvfrom(1024)
    message = message.upper()
    if rand < 4:
        print('Packet dropped.')
        continue
    serverSocket.sendto(message, address)
    print('Packet echoed.')

import threading
import time
from socket import *
import datetime
import time

serverName = 'localhost'
serverPort = 7777
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
for i in range(1, 11):
    sending_time = datetime.datetime.now()
    message = "ping " + str(i) + " time " + str(sending_time)
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    try:
        message1, server_address = clientSocket.recvfrom(1024)
        receiving_time = datetime.datetime.now()
        print(message1)
        RTT = receiving_time.microsecond*(10**-6) - sending_time.second*(10**-6)
        print("RTT time = %f" % RTT)
    except:
        print("Request timed out")
clientSocket.close()
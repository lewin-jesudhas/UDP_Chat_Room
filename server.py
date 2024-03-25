import socket
import sys
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.bind((IP_address, Port))

list_of_clients = []

while True:
    message, addr = server.recvfrom(2048)
    message = message.decode()
    if addr not in list_of_clients:
        list_of_clients.append(addr)
    name, message = message.split(': ', 1)  # Split the message into name and message
    print("<" + name + "> " + message)
    for client_addr in list_of_clients:
        if client_addr != addr:
            server.sendto(message.encode(), client_addr)

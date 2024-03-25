import socket
import sys
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(('0.0.0.0', 0))  # Bind to any available port on any available network interface

if len(sys.argv) != 4:
    print("Correct usage: script, IP address, port number, your name")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
name = str(sys.argv[3])

def receive_messages():
    while True:
        message, addr = client.recvfrom(2048)
        print(message.decode())

def send_messages():
    while True:
        message = input()
        client.sendto((name + ': ' + message).encode(), (IP_address, Port))

# Start separate threads for receiving and sending messages
receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)
receive_thread.start()
send_thread.start()

#!/usr/bin/env python3

import socket

BIND_IP = "127.0.0.1"
BIND_PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((BIND_IP, BIND_PORT))
server.listen(1)

print(f"Listening on {BIND_IP}:{BIND_PORT}")

client, addr = server.accept()
print(f"Accepted connection from {addr[0]}:{addr[1]}")

current_dir = client.recv(1024).decode()
print(f"[*] Current directory: {current_dir}")
print("[*] Enter commands:")

while True:
    command = input(">> ")
    client.send(command.encode())

    if command.lower() == 'exit':
        break

    response = client.recv(4096).decode()
    print(response)

client.close()
server.close()

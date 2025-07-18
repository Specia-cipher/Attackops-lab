#!/usr/bin/env python3
import argparse
import logging
import time
import os
import requests
import paramiko

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def generate_dummy_data():
    return "SensitiveData:1234567890abcdef\n" * 10  # simple dummy content

def http_exfiltrate(url, interval, count):
    data = generate_dummy_data()
    logger.info(f"Starting HTTP exfiltration to {url}")
    for i in range(count):
        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            logger.info(f"HTTP exfiltration attempt {i+1}/{count} succeeded")
        except Exception as e:
            logger.error(f"HTTP exfiltration attempt {i+1}/{count} failed: {e}")
        time.sleep(interval)

def sftp_exfiltrate(host, port, username, password, remote_path, interval, count):
    dummy_file = "dummy_exfil.txt"
    with open(dummy_file, "w") as f:
        f.write(generate_dummy_data())

    logger.info(f"Starting SFTP exfiltration to {host}:{port} as {username}")
    for i in range(count):
        try:
            transport = paramiko.Transport((host, port))
            transport.connect(username=username, password=password)
            sftp = paramiko.SFTPClient.from_transport(transport)
            remote_file = f"{remote_path}/dummy_exfil_{int(time.time())}.txt"
            sftp.put(dummy_file, remote_file)
            sftp.close()
            transport.close()
            logger.info(f"SFTP exfiltration attempt {i+1}/{count} succeeded")
        except Exception as e:
            logger.error(f"SFTP exfiltration attempt {i+1}/{count} failed: {e}")
        time.sleep(interval)

    os.remove(dummy_file)

def parse_args():
    parser = argparse.ArgumentParser(description="DataExfilSim - Simulate data exfiltration over HTTP and SFTP")
    parser.add_argument('--protocol', choices=['http', 'sftp'], required=True, help="Protocol to use for exfiltration")
    parser.add_argument('--target-url', help="HTTP destination URL for exfiltration")
    parser.add_argument('--sftp-host', help="SFTP server hostname or IP")
    parser.add_argument('--sftp-port', type=int, default=22, help="SFTP server port (default: 22)")
    parser.add_argument('--username', help="Username for SFTP")
    parser.add_argument('--password', help="Password for SFTP")
    parser.add_argument('--remote-path', default='.', help="Remote directory on SFTP server (default: current dir)")
    parser.add_argument('--interval', type=int, default=10, help="Seconds between exfiltration attempts")
    parser.add_argument('--count', type=int, default=5, help="Number of exfiltration attempts")
    return parser.parse_args()

def main():
    args = parse_args()

    if args.protocol == 'http':
        if not args.target_url:
            logger.error("HTTP protocol selected but --target-url not provided")
            return
        http_exfiltrate(args.target_url, args.interval, args.count)

    elif args.protocol == 'sftp':
        if not all([args.sftp_host, args.username, args.password]):
            logger.error("SFTP protocol selected but --sftp-host, --username, or --password missing")
            return
        sftp_exfiltrate(args.sftp_host, args.sftp_port, args.username, args.password, args.remote_path, args.interval, args.count)

if __name__ == '__main__':
    main()

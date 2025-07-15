#!/usr/bin/env python3

import nmap
import sys

def scan_ports(target, ports):
    nm = nmap.PortScanner()
    try:
        results = nm.scan(target, ports=ports, arguments='-sS -T4') # -sS for SYN scan, -T4 for faster timing
        if target in results['scan']:
            print(f"Scan results for: {target}")
            for port in results['scan'][target]['tcp']:
                if results['scan'][target]['tcp'][port]['state'] == 'open':
                    print(f"Port {port}: Open")
        else:
            print(f"Could not scan target: {target}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: ./recon_raptor.py <target_ip>")
        sys.exit(1)

    target_ip = sys.argv[1]
    common_ports = '21,22,23,25,53,80,110,115,135,139,143,443,445,3389,8080' # Add more as needed
    scan_ports(target_ip, common_ports)

if __name__ == "__main__":
    main()

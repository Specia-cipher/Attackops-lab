#!/usr/bin/env python3

import nmap
import sys
import dns.resolver

def scan_ports(target, ports):
    """Performs a SYN port scan on the target for the specified ports."""
    nm = nmap.PortScanner()
    try:
        results = nm.scan(target, ports=ports, arguments='-sS -T4') # -sS for SYN scan, -T4 for faster timing
        if target in results['scan']:
            print(f"Scan results for: {target}")
            for proto in results['scan'][target].get('tcp', {}):
                state = results['scan'][target]['tcp'][proto]['state']
                print(f"Port {proto}: {state}")
        else:
            print(f"Could not scan target: {target}")
    except Exception as e:
        print(f"An error occurred during port scanning: {e}")

def enumerate_subdomains(target_domain, subdomains):
    """Enumerates subdomains for the given target domain."""
    print(f"\nSubdomains for: {target_domain}")
    try:
        for subdomain in subdomains:
            url = f"{subdomain}.{target_domain}"
            try:
                answers = dns.resolver.resolve(url, 'A')
                for rdata in answers:
                    print(f"Found: {url} - {rdata.address}")
            except dns.resolver.NXDOMAIN:
                pass # Subdomain does not exist
            except dns.resolver.NoAnswer:
                pass # No A record found for the subdomain
    except Exception as e:
        print(f"An error occurred during subdomain enumeration: {e}")

def is_valid_ipv4(ip):
    """Checks if the input is a valid IPv4 address."""
    parts = ip.split('.')
    if len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts):
        return True
    return False

def main():
    """Main function to handle script arguments and execution."""
    if len(sys.argv) != 2:
        print("Usage: ./recon_raptor.py <target_ip_or_domain>")
        sys.exit(1)

    target = sys.argv[1]
    common_ports = '21,22,23,25,53,80,110,115,135,139,143,443,445,3389,8080'
    subdomains_list = ["www", "mail", "ftp", "admin", "blog", "shop", "test", "dev", "webmail", "smtp", "owa"] # Expanded list

    print(f"Target: {target}")

    # Try port scanning if the target looks like an IP address
    if is_valid_ipv4(target):
        print("\nPerforming basic port scan...")
        scan_ports(target, common_ports)
    else:
        print("\nPerforming basic port scan (if resolves to IP)...")
        try:
            dns.resolver.resolve(target, 'A') # Check if domain resolves
            scan_ports(target, common_ports)
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.Timeout):
            print(f"Could not resolve {target} to an IP for port scanning.")

    # Perform subdomain enumeration if the target looks like a domain
    if '.' in target and not target.replace('.', '').isdigit():
        print("\nPerforming subdomain enumeration...")
        enumerate_subdomains(target, subdomains_list)

if __name__ == "__main__":
    main()


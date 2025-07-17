#!/usr/bin/env python3

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from colorama import Fore, Style, init
import sys

# Initialize Colorama
init(autoreset=True)

def banner():
    print(Fore.CYAN + Style.BRIGHT + """
    ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗ ██████╗██████╗  █████╗ ████████╗
    ██╔══██╗██║  ██║██║██╔════╝██║  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝
    ██████╔╝███████║██║███████╗███████║██║     ██████╔╝███████║   ██║   
    ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██║     ██╔═══╝ ██╔══██║   ██║   
    ██║     ██║  ██║██║███████║██║  ██║╚██████╗██║     ██║  ██║   ██║   
    ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝     ╚═╝  ╚═╝   ╚═╝   
    """)
    print(Fore.GREEN + "📧 PhishCraft Mailer - Educational Use Only")
    print(Fore.YELLOW + "Author: Sanni Babatunde Idris (Specia-Cipher)\n")


def send_email(smtp_server, port, sender, recipient, subject, body, username=None, password=None, use_tls=True):
    """
    Sends an email via SMTP relay or authenticated SMTP server.
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))

        print(Fore.CYAN + f"[*] Connecting to {smtp_server}:{port}...")
        server = smtplib.SMTP(smtp_server, port, timeout=10)

        if use_tls:
            print(Fore.CYAN + "[*] Starting TLS encryption...")
            server.starttls()

        if username and password:
            print(Fore.CYAN + "[*] Authenticating as " + username)
            server.login(username, password)

        print(Fore.CYAN + "[*] Sending email...")
        server.send_message(msg)
        print(Fore.GREEN + "[+] Email sent successfully!")

    except Exception as e:
        print(Fore.RED + f"[!] Error: {e}")

    finally:
        server.quit()
        print(Fore.CYAN + "[*] Connection closed.")


if __name__ == "__main__":
    banner()

    if len(sys.argv) < 6:
        print(Fore.YELLOW + "Usage:")
        print(Fore.YELLOW + "  For relay: ./phishcraft_mailer.py <smtp_server> <port> <sender> <recipient> <subject>")
        print(Fore.YELLOW + "  For auth:  ./phishcraft_mailer.py <smtp_server> <port> <sender> <recipient> <subject> <username> <password>")
        sys.exit(1)

    smtp_server = sys.argv[1]
    port = int(sys.argv[2])
    sender = sys.argv[3]
    recipient = sys.argv[4]
    subject = sys.argv[5]
    username = sys.argv[6] if len(sys.argv) > 6 else None
    password = sys.argv[7] if len(sys.argv) > 7 else None

    # Example email body
    body = """
    <h2>Hello!</h2>
    <p>This is a <b>PhishCraft</b> test email.</p>
    <p>Stay ethical, stay dangerous.</p>
    """

    send_email(smtp_server, port, sender, recipient, subject, body, username, password)

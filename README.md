🗡️ AttackOps-Lab

A modular offensive security lab designed for mastering attack chains and adversarial techniques – the offensive sibling of **DefenseOps-Lab**.

Where DefenseOps-Lab focused on hardening systems and countering attacks, **AttackOps-Lab flips the script**: demonstrating how attacks happen in the first place. Together, these two labs provide full-spectrum coverage for ethical hackers, red teamers, and blue teams alike.

📍 **Author**: Sanni Babatunde Idris  
📧 **Email**: sannifreelancer6779@gmail.com  
🐙 **GitHub**: [Specia-cipher](https://github.com/Specia-cipher)

---

## 📑 Table of Contents

- 🎯 Overview  
- 🚀 Project Objectives  
- ⚙️ Tools and Modules  
- 🛠️ Features  
- 🐳 Containerization  
- 📦 Deployment  
- 📜 License  
- ⚠️ Disclaimer

---

## 🎯 Overview

AttackOps-Lab is a collection of offensive security tools designed to:

✅ Simulate real-world attack chains across the MITRE ATT&CK framework.  
✅ Teach adversarial techniques in a **controlled lab** for ethical and defensive purposes.  
✅ Provide a sandbox where learners can see the offensive side of cybersecurity – complementing DefenseOps-Lab’s defensive tooling.  
✅ Empower professionals and self-learners alike to understand both sides of the coin.

This project runs seamlessly on **Kali Linux**, **WSL2**, and lightweight environments like **Termux**. Future updates will add Docker support for fully isolated labs.

---

## 🚀 Project Objectives

1. 🎯 Build modular offensive tools covering every phase of the attack chain.  
2. 🏹 Simulate adversarial techniques to help defenders recognize and counter them.  
3. 📦 Offer containerized deployments for safe, reproducible environments *(planned)*.  
4. 📚 Deliver a practical lab for red team training, blue team awareness, and ethical hacking practice.

---

## ⚙️ Tools and Modules

| Stage               | Tool Name        | Description                                                   | Status |
|---------------------|------------------|---------------------------------------------------------------|--------|
| Reconnaissance      | 🕵️ ReconRaptor   | Active/passive recon with port scanning and subdomain enumeration. | ✅     |
| Weaponization       | 💣 PayloadForge  | Reverse shell payload generator, droppers, and basic persistence. | ✅     |
| Delivery            | ✉️ PhishCraft    | Phishing simulation with mailer & fake login portals.         | ✅     |
| Exploitation        | 🔥 ExploitHunter | Automated scanner for SQLi, XSS, and simulated command injection vulnerabilities. | ✅     |
| Installation        | 🐛 DropperSim    | Simulate post-compromise persistence mechanisms via cron jobs. | ✅ (cronjob only) 🔜 (systemd planned) |
| Command & Control   | 🎛️ C2Ghost       | Reverse shell C2 server & client for post-exploitation.         | ✅     |
| Actions on Objectives| 📂 DataExfilSim  | Simulate data exfiltration of sensitive information over HTTP and SFTP protocols. | ✅     |

---

## 🛠️ Features

### ✅ ReconRaptor
- Multi-threaded Nmap scanning (fast, full, UDP).  
- Subdomain enumeration using DNS brute-forcing.  
- Output: TXT, JSON, and HTML reports.

### ✅ PayloadForge
- Reverse shell payloads for Linux targets.  
- File upload/download and basic persistence via cron jobs.  
- **AES encryption planned (kept simple for educational use).**

### ✅ C2Ghost
- Command & Control server and client for managing shells.  
- File transfer support.  
- Tested on Kali WSL2 and Termux.

### ✅ PhishCraft
- Mailer module: send crafted phishing emails.  
- Tracker module: host fake login portals, capture credentials.  
- Extendable for WAN use with Cloudflared/ngrok tunnels.

### ✅ ExploitHunter
- Automated detection of web vulnerabilities: **SQL Injection (SQLi)**, **Cross-Site Scripting (XSS)**, and **simulated Command Injection (RCE)**.  
- Discover all HTML forms on a target application and inject a curated set of payloads.  
- Parses server responses for vulnerability signatures and reflected payloads.  
- Simulates OS command injection safely by checking output snippets without executing harmful commands.  
- Robust error handling with connection and read timeouts to avoid hangs.  
- Polite request pacing with delays and realistic user-agent headers to minimize blocking.  
- Command-line interface allowing selective scans (enable/disable SQLi, XSS, command injection) and JSON report output.  
- Logs all activity both to console with color-coded alerts and to a timestamped persistent log file (`exploit_hunter.log`).  
- Designed as a modular, extensible proof-of-concept tool illustrating fundamental offensive web scanning techniques for educational use.

### ✅ DropperSim
- Cron job persistence simulation successfully implemented and tested.  
- Supports deploying and cleaning persistence jobs safely on Linux targets.  
- **Systemd service/timer persistence support planned for future releases.**  
- *Note:* Systemd persistence requires a full systemd user session, which may not be available in lightweight environments like WSL2. BackBox VMs or native Linux with systemd are recommended for testing systemd features.

### ✅ DataExfilSim  
- Simulates data exfiltration of dummy sensitive data over **HTTP** and **SFTP** protocols.  
- **HTTP exfiltration** tested successfully with configurable intervals and counts; sends data to target URLs using POST requests.  
- **SFTP exfiltration** tested end-to-end with a secure, chrooted SFTP server user; supports uploading dummy files to specified remote directories with password authentication.  
- Uses Python’s Paramiko library for SFTP connectivity, with robust session and authentication handling.  
- Logs each exfiltration attempt with status for monitoring success/failure.  
- Deprecation warnings on some cryptography algorithms may appear due to underlying libraries but do not affect functionality.  
- Configurable exfiltration intervals and repeat counts for realistic simulation pacing.  
- Designed to integrate into wider offensive toolchains and red team training scenarios.  

---

## 🐳 Containerization (Planned)

AttackOps-Lab will ship Dockerized modules for:

✅ Isolated, reproducible lab environments.  
✅ Full lab orchestration via `docker-compose up`.  
✅ Safe testing without impacting host systems.

For now, scripts run natively on Linux and Termux.

---

## 📦 Deployment

### Clone the repo:
git clone https://github.com/Specia-cipher/AttackOps-Lab.git  
cd AttackOps-Lab

### Run a module:
python3 recon_raptor.py <target>  
python3 payloadforge.py  
python3 c2ghost_listener.py  
python3 c2ghost_client.py  
PHISH_TEMPLATE=gmail python3 phishcraft_tracker.py  
python3 phishcraft_mailer.py --to victim@example.com  
python3 exploit_hunter.py http://targetsite.com

### ExploitHunter Example Usage:
Run full scan (SQLi, XSS, Command Injection enabled):  
`python3 exploit_hunter.py http://example.com`

Skip command injection scan:  
`python3 exploit_hunter.py http://example.com --no-cmd`

Save JSON report:  
`python3 exploit_hunter.py http://example.com --json results.json`

### Planned full lab launch:
`docker-compose up --build`  
*(Coming soon)*

---

📜 License

MIT License © Sanni Babatunde Idris

---

⚠️ Disclaimer

This lab is intended strictly for educational and ethical testing purposes. Unauthorized use against systems you don’t own or have explicit permission to test is illegal. The author assumes no responsibility for misuse.

---

🔥 With AttackOps-Lab you don’t just study attacks… you build them, test them, and learn how to stop

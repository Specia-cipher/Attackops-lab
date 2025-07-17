# 🗡️ AttackOps-Lab

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
| Reconnaissance      | 🕵️ ReconRaptor   | Active/passive recon with port scanning and subdomain enum.   | ✅     |
| Weaponization       | 💣 PayloadForge  | Reverse shell generator, droppers, and basic persistence.     | ✅     |
| Delivery            | ✉️ PhishCraft    | Phishing simulation with mailer & fake login portals.         | ✅     |
| Exploitation        | 🔥 ExploitHunter | Scanner for SQLi, XSS, and simulated RCE vulnerabilities.     | 🔜     |
| Installation        | 🐛 DropperSim     | Deploy persistence mechanisms post-compromise.                | 🔜     |
| Command & Control   | 🎛️ C2Ghost       | Reverse shell C2 server & client for post-exploitation.       | ✅     |
| Actions on Objectives| 📂 DataExfilSim  | Simulate data exfiltration of sensitive information.          | 🔜     |

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

### 🔜 ExploitHunter
- Planned SQLi and XSS scanner.
- Simulated RCE exploits for ethical testing.

### 🔜 DropperSim
- Planned deployment of persistence (cron jobs, startup scripts).
- Test how attackers maintain access post-compromise.

### 🔜 DataExfilSim
- Planned simulation of data exfiltration over HTTP/SFTP.
- Dummy sensitive data extraction for blue team training.

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
```bash
git clone https://github.com/Specia-cipher/AttackOps-Lab.git
cd AttackOps-Lab

Run a module:

python3 recon_raptor.py <target>
python3 payloadforge.py
python3 c2ghost_listener.py
python3 c2ghost_client.py
PHISH_TEMPLATE=gmail python3 phishcraft_tracker.py
python3 phishcraft_mailer.py --to victim@example.com

Planned full lab launch:

docker-compose up --build

(Coming soon)


---

📜 License

MIT License © Sanni Babatunde Idris


---

⚠️ Disclaimer

This lab is intended strictly for educational and ethical testing purposes. Unauthorized use against systems you don’t own or have explicit permission to test is illegal. The author assumes no responsibility for misuse.


---

🔥 With AttackOps-Lab you don’t just study attacks… you build them, test them, and learn how to stop them.


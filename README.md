# 🗡️ AttackOps-Lab

A modular offensive security lab engineered for mastering attack chains and adversarial techniques — designed for ethical research and defensive innovation.

📍 **Author**: Sanni Babatunde Idris  
📧 **Email**: sannifreelancer6779@gmail.com  
🐙 **GitHub**: [Specia-cipher](https://github.com/Specia-cipher)  

---

## 📑 Table of Contents
- 🎯 Overview
- 🚀 Project Objectives
- ⚙️ Tools and Modules
- 🛠️ Planned Features
- 🐳 Containerization
- 📦 Deployment
- 📜 License
- ⚠️ Disclaimer

---

## 🎯 Overview

AttackOps-Lab is a collection of offensive security tools designed for:

✅ Simulating real-world attack chains.  
✅ Understanding adversarial techniques in a controlled environment.  
✅ Building offensive tools that mirror MITRE ATT&CK and Lockheed Cyber Kill Chain stages.  
✅ Equipping defensive security teams to recognize and counter these attacks.  

Built to run seamlessly on **Kali Linux**, with lightweight scripts compatible with **Termux** for mobile testing. Docker support may be included later to ship a full isolated lab for ethical purposes.

---

## 🚀 Project Objectives

1. 🎯 Hands-on mastery of offensive security techniques.  
2. 🏹 Build a library of modular tools covering Reconnaissance to Impact.  
3. 🛡️ Provide red-teamers and blue-teamers with a controlled sandbox for practicing attack and defense.  
4. 🐳 Offer containerized deployments for isolated, reproducible environments *(planned)*.  

---

## ⚙️ Tools and Modules

Here’s the current and planned lineup of modules in AttackOps-Lab:

| Stage               | Tool Name        | Description                                                   | Status |
|---------------------|------------------|---------------------------------------------------------------|--------|
| Reconnaissance      | 🕵️ ReconRaptor   | Active/passive recon with port scanning and subdomain enum.   | ✅     |
| Weaponization       | 💣 PayloadForge  | Python reverse shells, basic droppers, and persistence.       | ✅     |
| Delivery            | ✉️ PhishCraft    | Simulate phishing emails and fake login pages.                | 🔜     |
| Exploitation        | 🔥 ExploitHunter | Scanner for SQLi, XSS, and simulate RCE vulnerabilities.       | 🔜     |
| Installation        | 🐛 DropperSim     | Deploy lightweight persistence mechanisms.                    | 🔜     |
| Command & Control   | 🎛️ C2Ghost       | Simulated C2 server to manage reverse shells.                 | ✅     |
| Actions on Objectives| 📂 DataExfilSim  | Simulate data exfiltration from compromised systems.          | 🔜     |

---

## 🛠️ Features Highlights

### ✅ ReconRaptor
- Port scanning with OS & service version detection.
- Subdomain enumeration using DNS queries.
- Runs on Kali and Termux.

---

### ✅ PayloadForge
- Python reverse shell generator.
- Linux persistence via cron jobs.
- Supports file upload & download commands.
- **Can be upgraded to AES encryption** (deliberately kept simple for educational use).

---

### ✅ C2Ghost
- Encrypted C2 server (AES support planned).  
- Manage incoming shells, execute commands.  
- Download & upload files from target systems.

---

### 🔜 PhishCraft *(Planned)*
- Craft phishing emails with fake login portals.
- Track victim clicks and credential submissions.

---

### 🔜 ExploitHunter *(Planned)*
- Basic scanners for SQLi and XSS.
- Simulated RCE payloads for ethical testing.

---

### 🔜 DropperSim *(Planned)*
- Deploy cron jobs, registry keys, or startup scripts.
- Simulate attacker persistence post-compromise.

---

### 🔜 DataExfilSim *(Planned)*
- Exfiltrate dummy sensitive data to attacker-controlled servers.

---

## 🐳 Containerization (Planned)

AttackOps-Lab **may include Docker support in future updates** to:
- Isolate each module for safe testing.
- Quickly spin up the full attack chain with `docker-compose`.
- Provide pre-configured lab environments for ethical use only.  

For now, scripts run natively on Linux and Termux.

---

## 📦 Deployment

### 1️⃣ Clone the repo:
```bash
git clone https://github.com/Specia-cipher/AttackOps-Lab.git
cd AttackOps-Lab

2️⃣ Run modules:

python3 recon_raptor.py <target_ip_or_domain>
python3 payloadforge.py
python3 c2ghost_listener.py  # Start the C2 listener
python3 c2ghost_client.py    # Deploy client on target

3️⃣ Planned full lab launch:

docker-compose up --build

(Docker support coming later)


---

📜 License

MIT License © Sanni Babatunde Idris


---

⚠️ Disclaimer

This project is intended strictly for educational and ethical testing purposes. Unauthorized use against systems you do not own or have permission to test is illegal. The author is not responsible for misuse.


---

🔥 With AttackOps-Lab you don’t just learn attacks… you master the entire kill chain.



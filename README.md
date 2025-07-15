🗡️ AttackOps-Lab

A modular offensive security lab engineered for mastering attack chains and adversarial techniques — designed for ethical research and defensive innovation, **mirroring the structure and intent of DefenseOps-Lab but on the offensive side.**

📍 Author: Sanni Babatunde Idris  
📧 Email: sannifreelancer6779@gmail.com  
🔗 LinkedIn: [Sanni Idris](https://www.linkedin.com/in/sanni-idris-89917a262/)  
🐙 GitHub: [Specia-cipher](https://github.com/Specia-cipher)

---

## 📑 Table of Contents

1. [Overview](#overview)
2. [Project Objectives](#project-objectives)
3. [Completed Modules](#completed-modules)
   * [ReconRaptor](#reconraptor)
   * [PayloadForge](#payloadforge)
   * [Listener](#listener)
4. [Planned Modules](#planned-modules)
   * [C2Ghost](#c2ghost)
   * [PhishCraft](#phishcraft)
   * [ExploitHunter](#exploithunter)
   * [DropperSim](#droppersim)
   * [DataExfilSim](#dataexfilsim)
5. [Containerization](#containerization)
6. [Deployment](#deployment)
7. [License](#license)
8. [Disclaimer](#disclaimer)

---

## 🎯 Overview

AttackOps-Lab is a collection of offensive security tools designed for:

✅ Simulating real-world attack chains  
✅ Understanding adversarial techniques in a controlled environment  
✅ Building offensive tools that mirror MITRE ATT&CK and Cyber Kill Chain stages  
✅ Helping defensive security teams recognize and counter attacks  

This project complements **DefenseOps-Lab**, showing mastery of both red and blue team tactics. Development is split between:

💻 Laptop (full containerized stack planned)  
📱 Mobile (Termux + Kali/Ubuntu on UserLAnd for smaller modules)

---

## 🎯 Project Objectives

- Hands-on mastery of offensive techniques  
- Modular tools for each stage of an attack chain  
- Sandbox for red-teaming and blue-teaming  
- Containerized deployments for reproducibility  
- Cross-platform support where possible  

---

## ✅ Completed Modules

### 🕵️ ReconRaptor

Performs active reconnaissance, including:  

- Port scanning (TCP SYN scan)  
- OS detection and service version detection  
- Subdomain enumeration with DNS resolver  

📄 **Usage Example:**

```bash
python3 recon_raptor.py example.com

📌 Features:

✅ Basic SYN scan

✅ OS fingerprinting

✅ Service version detection

✅ Expanded subdomain list

⬜ Future: Passive recon (whois, Shodan API)



---

💣 PayloadForge

Generates Python-based reverse shells and persistence mechanisms. Designed to simulate weaponization and initial access.

📄 Features:

✅ Reverse TCP shell

✅ Linux persistence via cron jobs

✅ File download/upload support

⬜ Future: Windows payloads


📄 Usage Example:

python3 payloadforge.py

Start the listener first:

python3 listener.py


---

🎧 Listener

Handles incoming connections from PayloadForge payloads. Supports:

Interactive shell

File download/upload

Session logging (planned)


📄 Usage Example:

python3 listener.py


---

⬜ Planned Modules

🎛️ C2Ghost

⬜ Centralized C2 server for managing reverse shells

⬜ Issue commands to connected agents

⬜ Log sessions



---

✉️ PhishCraft

⬜ Email delivery simulator

⬜ Fake login pages

⬜ Track “victim” interactions



---

🔥 ExploitHunter

⬜ SQLi, XSS, and RCE vulnerability simulation

⬜ Payload library



---

🐛 DropperSim

⬜ Lightweight droppers for persistence testing



---

📂 DataExfilSim

⬜ Simulate data exfiltration



---

🐳 Containerization

AttackOps-Lab aims for containerized deployments (Docker/Podman):

🐳 Each module isolated in its own container

📦 Docker Compose to simulate full attack chains



---

📦 Deployment

1. Clone the repo:



git clone https://github.com/Specia-cipher/AttackOps-Lab.git
cd AttackOps-Lab

2. Run modules:



# Example:
python3 recon_raptor.py target.com
python3 payloadforge.py
python3 listener.py

3. (Planned) Deploy with Docker:



docker-compose up --build


---

📜 License

MIT License


---

⚠️ Disclaimer

This project is for educational and ethical use only. Unauthorized usage is prohibited. The author is not liable for misuse.


---

🔥 Building AttackOps-Lab is part of mastering adversarial techniques and contributing responsibly to offensive security research.

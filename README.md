🗡️ AttackOps-Lab

A modular offensive security lab engineered for mastering attack chains and adversarial techniques — designed for ethical research and defensive innovation, **mirroring the structure and intent of DefenseOps-Lab but on the offensive side.**

📍 Author: Sanni Babatunde Idris
📧 Email: sannifreelancer6779@gmail.com
🔗 LinkedIn
🐙 GitHub


---

📑 Table of Contents

🎯 Overview

🚀 Project Objectives

⚙️ Tools and Modules (Laptop-Focused)

📱 Tools and Modules (Phone-Focused)

🛠️ Planned Features (Laptop)

📱 Planned Features (Phone)

🐳 Containerization

📦 Deployment

📜 License

⚠️ Disclaimer


---

🎯 Overview

AttackOps-Lab is a collection of offensive security tools designed for:

✅ Simulating real-world attack chains.
✅ Understanding adversarial techniques in a controlled environment.
✅ Building offensive tools that mirror MITRE ATT&CK and Lockheed Cyber Kill Chain stages.
✅ Equipping defensive security teams to recognize and counter these attacks.

**This project is intentionally designed to complement DefenseOps-Lab, showcasing a comprehensive understanding of both offensive and defensive security principles.** It is being built with flexibility in mind, **leveraging the resources of both a laptop (during periods of stable power) and a mobile environment (Kali Linux via UserLAnd on phone and Termux) for various stages of development and testing.**


---

🚀 Project Objectives

1. 🎯 Hands-on mastery of offensive security techniques


2. 🏹 Build a library of modular tools covering Reconnaissance to Impact.


3. 🛡️ Provide red-teamers and blue-teamers with a controlled sandbox for practicing attack and defense.


4. 🐳 Offer containerized deployments for isolated, reproducible environments (primarily on laptop).


---

⚙️ Tools and Modules (Laptop-Focused - Prioritize these during NEPA windows)

Stage	Tool Name	Description	Status

Reconnaissance	🕵️ ReconRaptor	Active/passive recon against targets.	**[Focus: Implement basic port scanning using nmap in Python.]**
Weaponization	💣 PayloadForge	Create simple trojans (e.g., reverse shell), phishing pages.	[Initial plan: Generate a basic Python reverse shell payload.]
Command & Control	🎛️ C2Ghost	Simulated C2 server for managing reverse shells.	[Initial plan: Set up a basic listener for incoming connections.]


---

📱 Tools and Modules (Phone-Focused - Can be developed using Kali UserLAnd/Termux)

Stage	Tool Name	Description

Delivery	✉️ PhishCraft	Email + link delivery simulator for phishing. (Can be scripted in Python and tested on phone)
Exploitation	🔥 ExploitHunter	Simulate exploitation of common web vulns (SQLi, XSS). (Basic simulations can be done with scripting on phone)
Installation	🐛 DropperSim	Basic droppers for persistence testing. (Lightweight scripts can be developed on phone)
Actions on Objectives	📂 DataExfilSim	Exfiltrate dummy data to test detection. (Simple file operations can be scripted on phone)


---

🛠️ Planned Features (Laptop)

✅ ReconRaptor
    * **Basic port scanning (Nmap-like)**
    * DNS subdomain enumeration
    * WHOIS lookup
    * Passive OS fingerprinting

✅ PayloadForge
    * **Generate Python-based reverse shells**
    * Windows/Linux payloads (harmless for simulation)
    * Encode/obfuscate payloads for bypass simulation

✅ C2Ghost
    * **Listen for incoming reverse shells**
    * Issue basic commands (pwd, ls, cat)
    * Store logs of sessions


---

📱 Planned Features (Phone - Tasks suitable for mobile environments)

✅ PhishCraft

HTML email templates (can be created and tested)
Fake login pages (basic structures can be built)
Track “victim” clicks and submissions (basic tracking can be implemented)


✅ ExploitHunter

SQL injection scanner for test apps (basic scripting)
Basic XSS payload library (can be created and tested)
Simulated RCE on vulnerable targets (simple simulations)


✅ DropperSim

Deploy lightweight persistence mechanisms (scripting for registry edits simulation on Windows, cronjob creation on Linux)


✅ DataExfilSim

Simulate stealing sensitive data from “victim” systems (scripting file operations)
Upload to simulated attacker server (simple HTTP requests can be tested)


---

🐳 Containerization

This lab will aim for Docker support, primarily developed and tested on the laptop:

🐳 Each module containerized for isolation.

📦 Docker Compose for spinning up the full attack chain.

📱 Lighter modules might explore Termux-compatible packaging in the future.


---

📦 Deployment

1. Clone the repo:

   ```bash
   git clone [https://github.com/Specia-cipher/AttackOps-Lab.git](https://github.com/Specia-cipher/AttackOps-Lab.git)
   cd AttackOps-Lab
Run modules (check the comments in the scripts for environment suitability - laptop or phone):

Bash

# Example (Laptop):
python3 recon_raptor.py --target example.com
python3 payload_forge.py --reverse-shell

# Example (Phone - via Termux/UserLAnd):
python3 phish_craft.py --template basic_email.html --target victim@example.com
Deploy full lab in Docker (Laptop):

Bash

docker-compose up --build
📜 License

MIT License

⚠️ Disclaimer

This project is intended for educational and ethical testing purposes only. Use of these tools for unauthorized activity is strictly prohibited. The author is not responsible for misuse.

🔥 Mirroring the defensive focus of DefenseOps-Lab, AttackOps-Lab showcases a comprehensive understanding of the cyber battlefield, leveraging both the power of a laptop and the flexibility of a mobile environment. Let's get to work!

cat > README.md <<'EOF'
# 🔐 ICS/SCADA Security Lab

A hands-on cybersecurity project that simulates an industrial control system under attack.

---

## 🚀 Overview

This project demonstrates a segmented ICS environment built with Docker.

The lab simulates a realistic attack scenario where an attacker:
- moves from IT to DMZ to OT
- exploits Modbus TCP
- changes register values
- gets detected using Suricata IDS

---

## 🏗️ Architecture

| Zone | Description |
|------|------------|
| IT | Attacker workstation |
| DMZ | Jump server |
| OT | Modbus server |

Security design:
- No direct IT to OT access  
- Firewall enforced segmentation  
- Jump server required for pivoting  

---

## 🧰 Technologies Used

- Docker  
- Docker Compose  
- Python (pymodbus)  
- Modbus TCP  
- Suricata IDS  
- tcpdump  
- iptables  

---

## ⚔️ Attack Scenario

Steps performed:

1. Accessed jump server  
2. Pivoted into OT network  
3. Sent Modbus write request  
4. Changed register value  

---

## 📸 Screenshots

### 🔴 Attack
Modbus write attack executed from jump server to OT.

![Attack](screenshots/attack.png)

### 📡 tcpdump
Captured Modbus traffic on port 502.

![tcpdump](screenshots/tcpdump.png)

### 🚨 Suricata Alert
Detection of malicious Modbus write activity.

![Suricata](screenshots/suricata.png)

### 📜 Detection Rule
Custom rule used in Suricata.

![Rule](screenshots/rule.png)

### 🔥 Firewall
iptables rules enforcing segmentation.

![Firewall](screenshots/firewall.png)

---

## 🧪 Detection

A custom Suricata rule was used:

```bash
alert tcp any any -> any 502 (msg:"MODBUS WRITE DETECTED"; content:"|00 06|"; sid:1000001;)

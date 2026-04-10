# ICS/SCADA Security Lab

## Overview
This project demonstrates a segmented ICS environment with IT, DMZ, and OT zones using Docker.

It shows how an attacker can pivot through a jump server to reach an OT Modbus server, modify register values, and trigger detection with Suricata IDS.

## Architecture
- IT zone: attacker workstation
- DMZ: jump server
- OT zone: Modbus server

Security model:
- No direct access from IT to OT
- Traffic is controlled through firewall rules
- Access to OT is limited through the jump server

## Technologies Used
- Docker
- Docker Compose
- Modbus TCP
- pymodbus
- Suricata IDS
- tcpdump
- iptables

## Attack Scenario
The attack was performed from the IT side through the jump server to the OT network.

The attacker:
1. Reached the jump server
2. Connected to the Modbus server in OT
3. Sent a Modbus write request
4. Changed a register value

## Results
- Register values were modified successfully
- Traffic on port 502 was captured with tcpdump
- Suricata detected the attack with a custom alert

## Detection Rule
Example Suricata rule used in the lab:

```bash
alert tcp any any -> any 502 (msg:"MODBUS WRITE DETECTED"; content:"|00 06|"; sid:1000001;)

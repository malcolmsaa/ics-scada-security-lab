# ICS/SCADA Security Lab

## Översikt

Detta projekt demonstrerar en segmenterad ICS/SCADA-miljö byggd med Docker för att simulera industriell cybersäkerhet och OT-säkerhet i praktiken.

Miljön är uppdelad i tre separerade zoner enligt Purdue-modellen:

- IT-zon
- DMZ-zon
- OT-zon

Projektets mål var att undersöka hur nätverkssegmentering, övervakning och detektion kan skydda industriella system mot obehörig åtkomst och attacker.

---

## Purdue-modell och nätverkssegmentering

Arkitekturen implementerades enligt Purdue-modellen med tydlig separation mellan IT och OT.

```text
IT Zone
   |
   v
DMZ / Jump Server
   |
   v
OT Zone (OpenPLC + ScadaBR)
```

All trafik mellan zonerna kontrolleras genom brandväggsregler och segmentering.

---

## Säkerhetsarkitektur

Följande säkerhetsåtgärder implementerades:

- Segmentering mellan IT, DMZ och OT
- Brandväggsregler enligt principen "deny all, allow explicit"
- Jump server för kontrollerad åtkomst till OT-zonen
- IDS-övervakning med Suricata
- Trafikanalys med tcpdump
- Logginsamling och övervakning med Wazuh

Målet var att skapa en realistisk industriell miljö med flera säkerhetslager.

---

## Använda verktyg

- Docker
- Docker Compose
- OpenPLC
- ScadaBR
- Suricata IDS
- tcpdump
- Wazuh
- iptables
- pymodbus

---

## Attackscenario

Ett simulerat Modbus TCP-angrepp genomfördes från IT-zonen mot OT-zonen via DMZ.

Attacken försökte manipulera registervärden i PLC-miljön. Suricata detekterade den misstänkta trafiken och genererade larm som verifierades med tcpdump.

---

## Incidentrapport

### Tidslinje

1. Angriparen initierade Modbus-kommunikation från IT-zonen.
2. Trafiken passerade via DMZ och jump server.
3. Ett write-kommando skickades mot OT-zonen.
4. Suricata genererade en säkerhetsvarning.
5. Trafiken verifierades med tcpdump.
6. Händelsen analyserades och dokumenterades.

### Containment

- Trafiken begränsades genom brandväggsregler.
- Åtkomst till OT-zonen sker endast via DMZ.

### Recovery

- Systemets konfiguration verifierades.
- Säkerhetsregler uppdaterades vid behov.
- Loggar sparades för vidare analys.

---
## IEC 62443 Security Levels

Miljön bedöms motsvara Security Level 1 (SL1) enligt IEC 62443.

Motivering:
- Segmentering mellan IT och OT
- Brandväggsregler för trafikfiltrering
- IDS-övervakning med Suricata
- Kontrollerad åtkomst via DMZ och jump server

För att nå högre säkerhetsnivåer krävs:
- Stark autentisering
- Krypterad kommunikation
- Rollbaserad åtkomstkontroll
- Fler processpecifika IDS-regler

## Incidentrapport

### Detektion
Suricata identifierade Modbus write-kommandon och genererade larm.

### Containment
Brandväggsregler begränsade trafiken mellan zonerna och OT-systemet var endast åtkomligt via DMZ.

### Recovery
Systemets konfiguration verifierades och loggar sparades för vidare analys och förbättring av regler.


## Riskanalys enligt IEC 62443

| Risk | Sannolikhet | Konsekvens | Åtgärd |
|------|------------|------------|--------|
| Obehörig åtkomst till OT | Medel | Hög | Segmentering och DMZ |
| Modbus utan autentisering | Hög | Hög | IDS-regler och övervakning |
| Lateral movement från IT | Medel | Hög | Brandvägg och nätverksisolering |
| Manipulation av PLC-data | Medel | Hög | Detektion med Suricata |

Bedömningen visar att segmentering och övervakning minskar riskerna avsevärt.

---

## Utökade Suricata-regler för Modbus

För att förbättra detektionen utökades Suricata med process-specifika regler för flera Modbus-funktionskoder.

Reglerna fokuserar på Modbus WRITE-operationer, eftersom dessa kan användas för att manipulera industriella processvärden.

Övervakade funktionskoder:

- FC5, Write Single Coil
- FC6, Write Single Register
- FC15, Write Multiple Coils
- FC16, Write Multiple Registers

Exempel på Suricata-regler:

```text
alert tcp any any -> any 502 (msg:"MODBUS FC5 WRITE SINGLE COIL DETECTED"; content:"|00 05|"; sid:1000005;)
alert tcp any any -> any 502 (msg:"MODBUS FC6 WRITE SINGLE REGISTER DETECTED"; content:"|00 06|"; sid:1000006;)
alert tcp any any -> any 502 (msg:"MODBUS FC15 WRITE MULTIPLE COILS DETECTED"; content:"|00 0F|"; sid:1000015;)
alert tcp any any -> any 502 (msg:"MODBUS FC16 WRITE MULTIPLE REGISTERS DETECTED"; content:"|00 10|"; sid:1000016;)

## Screenshots

### Attack mot OT-zon

![Attack](screenshots/attack.png)

### Suricata Alert

![Suricata](screenshots/suricata.png)

### tcpdump Analys

![tcpdump](screenshots/tcpdump.png)

### Brandväggsregler

![Firewall](screenshots/firewall.png)

### Dashboard och övervakning

![Dashboard](screenshots/dashboard.png)

---

## Utmaningar och lösningar

Projektet innehöll flera tekniska utmaningar:

- Docker-nätverk och routing mellan zoner
- Modbus-kommunikation mellan containrar
- IDS-regler som inte triggade korrekt
- Brandväggsregler som blockerade trafik

För att lösa problemen användes:

- tcpdump för trafikanalys
- Docker logs för felsökning
- Anpassade Suricata-regler
- Stegvis verifiering av nätverkskommunikation

---

## Slutsats

Projektet demonstrerar hur nätverkssegmentering, IDS-övervakning och säkerhetskontroller kan användas för att skydda industriella system.

Labben gav praktisk erfarenhet av:

- ICS/SCADA-säkerhet
- OT-arkitektur
- Attackdetektion
- Incidenthantering
- Riskanalys enligt IEC 62443

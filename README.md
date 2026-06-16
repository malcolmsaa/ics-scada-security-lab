# ICS/SCADA Security Lab

## Översikt

Detta projekt demonstrerar en segmenterad ICS/SCADA-miljö byggd med Docker för att simulera industriell nätverkssäkerhet och OT-säkerhet i praktiken.

Miljön består av tre separerade zoner:

- IT-zon
- DMZ-zon
- OT-zon

Syftet med projektet var att förstå:
- nätverkssegmentering
- Modbus TCP-kommunikation
- attackdetektion
- IDS-övervakning
- säkerhetsanalys i OT-miljöer

---

## Purdue-modell och nätverkssegmentering

Miljön byggdes enligt Purdue-modellen med separerade zoner för IT, DMZ och OT.

```text
IT Zone
   |
   v
DMZ / Jump Server
   |
   v
OT Zone (OpenPLC + ScadaBR)

---

---

# 2. Lägg till säkerhetsarkitektur

```md
## Säkerhetsarkitektur

Följande säkerhetsåtgärder implementerades i miljön:

- Segmentering mellan IT, DMZ och OT
- Brandväggsregler enligt "deny all, allow explicit"
- IDS med Suricata för övervakning av Modbus-trafik
- Trafikanalys med tcpdump
- Wazuh för logginsamling och övervakning
- Jump server för kontrollerad åtkomst till OT-zonen

Målet var att simulera en realistisk industriell miljö med grundläggande OT-säkerhet.

---

## Arkitektur

### IT-zon
Angriparens arbetsstation där attacken initieras.

### DMZ-zon
Jump server som fungerar som kontrollerad åtkomstpunkt mellan IT och OT.

### OT-zon
Modbus-server som simulerar industriell utrustning.

---

## Säkerhetsmodell

Projektet implementerar flera säkerhetsprinciper:

- Ingen direkt åtkomst mellan IT och OT
- Trafik filtreras genom brandväggsregler
- Åtkomst till OT sker endast via jump server
- Suricata används för IDS-detektion
- Modbus-trafik analyseras med tcpdump

## Riskanalys

| Risk | Konsekvens | Åtgärd |
|---|---|---|
| Obehörig åtkomst till OT-zonen | Manipulation av PLC-data | Segmentering och brandvägg |
| Modbus utan autentisering | Obehöriga write-kommandon | IDS-regler och nätverksisolering |
| Lateral movement från IT | Spridning till OT-system | DMZ och begränsad trafik |
| Sårbara containrar | Exploatering av tjänster | Trivy-scanning och uppdateringar |

---

## Attackscenario

Ett simulerat attackscenario genomfördes från IT-zonen mot OT-miljön.

### Attackflöde

1. Angriparen ansluter till jump servern
2. Trafik routas vidare mot OT-zonen
3. En Modbus write-operation skickas
4. Registervärden modifieras
5. Suricata genererar säkerhetsalert

---

## Detektion och Övervakning

### Suricata IDS

Suricata användes för att identifiera misstänkt Modbus-trafik och generera alerts vid write-operationer.

### tcpdump

tcpdump användes för att verifiera och analysera nätverkstrafiken mellan zonerna.

---

## Incidentrapport

Ett simulerat angrepp genomfördes mot OT-miljön via Modbus TCP.

Attacktrafiken genererade alerts i Suricata och kunde verifieras med tcpdump.

Övervakningen visade hur IDS kan identifiera misstänkt trafik mellan nätverkszoner.

Attacken dokumenterades med screenshots och logganalys.

---


## Utmaningar och lösningar

Projektet innehöll flera tekniska utmaningar:

- Problem med Docker-nätverk och routing mellan zoner
- Felsökning av Modbus-kommunikation
- IDS-regler som inte triggade korrekt
- Containerproblem och felaktiga images
- Trafik som blockerades av brandväggsregler

För att lösa problemen användes:

- tcpdump för trafikanalys
- Docker logs och container debugging
- Anpassade Suricata-regler
- Dokumentation och felsökning steg för steg

Projektet var betydligt mer avancerat än tidigare labbar men också mycket lärorikt.

## Verktyg och Teknologier

- Docker
- Docker Compose
- Python
- pymodbus
- Suricata IDS
- tcpdump
- iptables
- Linux networking

---

## Screenshots

### Attack mot OT-zon
![Attack](screenshots/attack.png)

### Suricata Alert
![Suricata](screenshots/suricata.png)

### tcpdump Analys
![tcpdump](screenshots/tcpdump.png)

### Brandväggsregler
![Firewall](screenshots/firewall.png)

---

## Slutsats

Projektet demonstrerar hur nätverkssegmentering och IDS-övervakning kan användas för att skydda industriella system mot obehörig åtkomst och skadlig trafik.

Labben gav praktisk förståelse för:
- OT-säkerhet
- ICS-arkitektur
- attackdetektion
- nätverkssegmentering
- incidentanalys
## IEC 62443 Security Level Analys

Miljön bedöms uppnå ungefär Security Level 1 (SL1) enligt IEC 62443.

Implementerade säkerhetsåtgärder:

- Nätverkssegmentering mellan IT, DMZ och OT
- Brandväggsregler enligt "deny all, allow explicit"
- IDS-övervakning med Suricata
- Övervakning med Wazuh
- Logginsamling och trafikanalys

Gap mot högre Security Levels:

- Ingen multifaktorautentisering
- Ingen kryptering av Modbus-trafik
- Ingen redundans eller hög tillgänglighet
- Begränsad åtkomstkontroll

För att uppnå SL2 eller högre krävs starkare autentisering, kryptering och mer avancerad åtkomstkontroll.
## Riskanalys

| Risk | Sannolikhet | Konsekvens | Åtgärd |
|------|------------|------------|--------|
| Obehörig åtkomst till OT | Medel | Hög | Segmentering och brandvägg |
| Modbus-manipulation | Hög | Hög | IDS-regler och övervakning |
| Lateral movement från IT | Medel | Hög | DMZ och filtrering |
| Komprometterad container | Medel | Medel | Uppdateringar och scanning |
## Incidentrapport

### Händelse

En simulerad attack genomfördes från IT-zonen mot OT-zonen via Modbus TCP.

### Detektion

Suricata identifierade misstänkt Modbus WRITE-trafik och genererade säkerhetslarm.

### Containment

Brandväggsregler begränsade kommunikationen mellan zonerna och all åtkomst till OT skedde via jump server i DMZ.

### Recovery

Miljön återställdes genom att stoppa attacktrafiken och verifiera systemets integritet med loggar och övervakning.

### Lärdomar

Incidenten visade vikten av nätverkssegmentering, IDS och kontinuerlig övervakning i industriella miljöer.

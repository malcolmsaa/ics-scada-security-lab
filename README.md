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

## Utmaningar

Projektet innehöll flera tekniska utmaningar:

- Routing mellan containrar
- Docker-nätverk och segmentering
- Modbus-kommunikation
- IDS-regler i Suricata
- Felsökning av trafikflöden
- Containerkommunikation mellan zoner

### Lösningar

Problemen löstes genom:
- stegvis felsökning
- analys av nätverkstrafik
- verifiering med tcpdump
- justering av brandväggsregler
- analys av Suricata-alerts
- dokumentation och testning av varje komponent

Projektet var betydligt mer avancerat än tidigare labbar men gav mycket praktisk erfarenhet inom OT- och ICS-säkerhet.

---

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

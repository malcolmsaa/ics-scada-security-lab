# Slutreflektion och VG-analys

## Introduktion

I denna laboration byggde jag en centraliserad säkerhetsövervakningsmiljö med hjälp av Wazuh och Docker. Målet var att samla loggar, övervaka systemhändelser, upptäcka attacker och analysera misstänkt aktivitet genom både regelbaserad och AI-baserad detektion.

Projektet innehåller:

- Wazuh Manager
- Wazuh Dashboard
- Wazuh Indexer
- Wazuh Agent
- Custom detection rules
- File Integrity Monitoring
- AI-baserad anomalidetektion
- Automatiserad incidentrespons
- Dokumentation och screenshots

---

## Hur systemet fungerar

Wazuh fungerar som ett SIEM-system där flera delar arbetar tillsammans.

### Agent

Wazuh-agenten installeras på klienten och samlar in:

- loggar
- filändringar
- kommandon
- säkerhetshändelser
- systemaktivitet

Agenten skickar informationen vidare till Wazuh Manager.

### Manager

Wazuh Manager analyserar datan och jämför den mot regler. Om något misstänkt upptäcks skapas en alert.

Exempel på händelser:

- misslyckade inloggningar
- filändringar
- misstänkta kommandon
- portscanning
- simulerade attacker

### Dashboard

Dashboarden visar resultatet visuellt.

Exempel:

- alerts
- severity levels
- aktiva agenter
- säkerhetsöversikt
- threat hunting
- file integrity monitoring

Dashboarden användes för att verifiera att systemet fungerade korrekt.

---

## Problem och utmaningar

Under laborationen uppstod flera problem.

### Problem 1: Agenten visades inte korrekt

Ett av de största problemen var att agenten inte dök upp som `Active` i dashboarden.

I vissa fall stod agenten som:

- `Never connected`
- `Disconnected`
- saknades helt i dashboarden

Detta gjorde att inga loggar skickades korrekt.

#### Orsak

Problemet berodde främst på:

- fel manager-adress
- kommunikationsproblem mellan Docker och WSL
- gamla containers och cache
- versionskonflikter mellan Wazuh-delarna

---

### Problem 2: Docker-miljön blev instabil

Flera gånger fungerade inte kommunikationen mellan:

- Wazuh Manager
- Wazuh Indexer
- Dashboard
- Agent

Ibland startade vissa containers korrekt medan andra inte gjorde det.

#### Orsak

Problemet berodde på:

- blandade versioner
- gamla Docker images
- felaktiga compose-filer
- korrupt miljö efter flera installationer

---

### Problem 3: Admin-användaren kunde inte ändras

När jag försökte ändra lösenord för admin fick jag felmeddelandet:

```text
FORBIDDEN: Resource 'admin' is reserved


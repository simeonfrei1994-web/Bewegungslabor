# KI-Deklaration – BewegungsLabor

## Projekt

- Titel: BewegungsLabor – Drei Bewegungsarten im Weg-Zeit-Diagramm
- Hochschule: Pädagogische Hochschule St. Gallen (PHSG)
- Modul: Projekt Applikation
- Semester: HS26

## Allgemeine Angaben zur KI-Unterstützung

Als KI-Werkzeug wird ChatGPT (OpenAI) eingesetzt.

Die Unterstützung umfasst die Projektplanung, die Entwicklung
von Programmcode, die Erklärung von Programmierkonzepten,
die Entwicklung von Tests sowie die technische Fehlerdiagnose.

Die vorgeschlagenen Codeblöcke werden in die lokale
Entwicklungsumgebung übernommen, nachvollzogen und getestet.

Die Dokumentation wird während der Projektentwicklung
fortlaufend ergänzt.

---

## Schritt 2 – Physikalisches Bewegungsmodell

### Quelle

- Werkzeug: ChatGPT (OpenAI)
- URL: https://chatgpt.com/
- Datum: 25.11.2026
- Chat: BewegungsLabor – Schritt 2/10

### KI-generierte Programmteile

Datei: motion.py

- Zentrale Bewegungs- und Simulationsparameter
- Dictionary MOTIONS
- Funktion effective_time()
- Funktion distance()
- Funktion velocity()
- Behandlung eines möglichen vorzeitigen Stillstands
- Behandlung negativer Zeitwerte
- Validierung der Anfangsgeschwindigkeit

Datei: test_motion.py

- Automatisierte Tests mit unittest
- Mathematische Referenzwerte
- Tests der Anfangs-, Zwischen- und Endwerte
- Tests besonderer physikalischer Grenzfälle

### Weitere KI-Unterstützung

- Erläuterung der physikalischen Bewegungsgleichungen
- Erläuterung der Softwarearchitektur
- Vorbereitung auf das mündliche Fachgespräch
- Anleitung zur Ausführung automatisierter Tests
- Fehlerdiagnose beim Start des grafischen Testprogramms
- Unterstützung bei Git-Commit und GitHub-Push
- Erstellung dieser KI-Deklaration

### Tatsächlich verwendeter Hauptprompt

Der vollständige ursprüngliche Prompt aus dem Chat
«BewegungsLabor – Schritt 2/10» wird nachfolgend
unverändert eingefügt.

# BewegungsLabor – Schritt 2/10

Wir setzen die Entwicklung des Projekts «BewegungsLabor – Drei Bewegungsarten im Weg-Zeit-Diagramm» gemäss der optimierten 10-Stunden-Masterplanung fort.

## 1. Projektziel

Entwicklung einer interaktiven, fachlich korrekten, optisch hochwertigen und stabilen Lernapplikation für Natur und Technik (NaTech 7) im Rahmen des Leistungsnachweises «Projekt Applikation» der PHSG.



Die Applikation visualisiert drei Bewegungsarten mittels eines animierten Objekts auf einer horizontalen Strecke und eines synchron entstehenden Weg-Zeit-Diagramms.

## 2. Abgeschlossener Entwicklungsstand

**Schritt 1 – Entwicklungsumgebung einrichten ist vollständig abgeschlossen.**

- Betriebssystem: macOS
- Entwicklungsumgebung: PyCharm 2025.2.3
- Python: 3.14.0
- Java: 19.0.1
- py5: 0.10.12a0
- Virtuelle Umgebung (.venv) eingerichtet
- Lokaler Projektordner: PythonProject2
- main.py erstellt
- Grafischer py5-Systemtest erfolgreich durchgeführt
- .gitignore korrekt eingerichtet
- Git initialisiert
- Erster Git-Commit erfolgreich erstellt
- GitHub-Konto mit PyCharm verbunden
- Projekt erfolgreich auf GitHub hochgeladen

Sämtliche technischen Voraussetzungen sind erfüllt. Es sind keine weiteren Installationen erforderlich.

## 3. Verbindliche mathematische Parameter

**Gleichförmige Bewegung:**

- Anfangsgeschwindigkeit: 5 m/s
- Beschleunigung: 0 m/s²

**Gleichmässig beschleunigte Bewegung:**

- Anfangsgeschwindigkeit: 0 m/s
- Beschleunigung: +1 m/s²

**Gleichmässig verzögerte Bewegung:**

- Anfangsgeschwindigkeit: 10 m/s
- Beschleunigung: −1 m/s²

**Gemeinsame Eigenschaften:**

- Startposition: 0 m
- Simulationsdauer: 10 Sekunden
- Zurückgelegter Weg: 50 Meter
- Durchschnittsgeschwindigkeit: 5 m/s

Für alle drei Bewegungsarten sollen dieselben parametrisierten Berechnungsfunktionen verwendet werden.



Bei einer verzögerten Bewegung muss ein allfälliger vorzeitiger Stillstand korrekt berücksichtigt werden. Negative Geschwindigkeiten und Richtungswechsel sind nicht vorgesehen.

## 4. Verbindlicher Funktionsumfang

- Auswahl einer der drei Bewegungsarten
- Animation eines einzelnen beweglichen Objekts
- Synchron entstehendes Weg-Zeit-Diagramm
- Start, Pause, Weiter und Reset
- Automatisches Simulationsende
- Live-Anzeige von Zeit, Weg und momentaner Geschwindigkeit
- Speicherung abgeschlossener Bewegungsversuche
- Gemeinsame Darstellung der abgeschlossenen Graphen im Vergleichsmodus
- Saubere Zustandskontrolle
- Hochwertige, übersichtliche Benutzeroberfläche

Keine Schieberegler, frei einstellbaren Bewegungsparameter oder unnötigen Zusatzfunktionen.

## 5. Verbindliche Softwarearchitektur

Drei eigentliche Programmdateien:

- **main.py:** Programmsteuerung, Zeitmessung, Zustandsverwaltung und Mausinteraktionen.
- **motion.py:** Bewegungsparameter und physikalische Berechnungen.
- **visualization.py:** Grafische Darstellung, Diagramme und Bedienelemente.

Ergänzende Dateien:

- test_motion.py
- README.md
- KI_Deklaration.md
- requirements.txt
- .gitignore (bereits vorhanden)

Die Architektur soll modular, parametrisiert, verständlich und möglichst einfach sein. Unnötig komplexe Programmierkonzepte sind zu vermeiden.

## 6. Entwicklungsplan

Das gesamte Projekt muss innerhalb eines Arbeitsbudgets von zehn Stunden realisierbar sein.

1. Entwicklungsumgebung einrichten – 45 min – ABGESCHLOSSEN
2. Physikalisches Bewegungsmodell – 45 min
3. Grafisches Grundlayout – 45 min
4. Bewegungsanimation – 45 min
5. Dynamisches Weg-Zeit-Diagramm – 60 min
6. Simulationssteuerung – 60 min
7. Bewegungsauswahl und Messwerte – 60 min
8. Vergleichsmodus – 60 min
9. Testing und Feinschliff – 60 min
10. Dokumentation und Abschluss – 75 min

Zusätzliche Zeitreserve: 45 Minuten.

## 7. Aktueller Auftrag

**Schritt 2/10 – Physikalisches Bewegungsmodell entwickeln.**



Arbeitsbudget: 45 Minuten.



Plane die konkrete Implementierung maximal gründlich und sorgfältig, aber setze sie möglichst effizient und einfach um.



Entwickle insbesondere:

- die Datei motion.py;
- eine zentrale Datenstruktur für die drei Bewegungsarten;
- die allgemeine Wegberechnung;
- die allgemeine Geschwindigkeitsberechnung;
- die fachlich korrekte Behandlung eines möglichen Stillstands;
- gezielte automatisierte Tests anhand mathematischer Referenzwerte.

Das bestehende grafische Testprogramm in main.py soll vorerst erhalten bleiben.

## 8. Vorgehen bei der gemeinsamen Programmierung

Führe mich in kleinen, konkreten Teilschritten durch die Programmierung in PyCharm 2025.2.3.



Gib mir jeweils:

1. Das konkrete Ziel des Teilschritts.
2. Genaue Anweisungen, wo ich in PyCharm klicken muss.
3. Vollständigen, direkt einsetzbaren Code.
4. Eine kompakte und verständliche Erklärung des Codes.
5. Eine eindeutige Funktionskontrolle.

Warte nach jedem Teilschritt auf meine Rückmeldung, bevor du mit dem nächsten beginnst.



Am Ende des Entwicklungsschritts:

- sämtliche relevanten Funktionen überprüfen;
- einen aussagekräftigen Git-Commit erstellen;
- den Entwicklungsstand auf GitHub hochladen;
- die KI-Unterstützung mit den tatsächlich verwendeten Prompts und Quellen gemäss PHSG-Vorgaben dokumentieren;
- einen vollständigen Übergabeprompt für Schritt 3 erstellen.

## 9. Qualitätsanforderungen

Orientiere dich konsequent an den hochgeladenen Modulunterlagen und am offiziellen Bewertungsraster der PHSG.



Das Ziel ist eine möglichst hohe Bewertung (angestrebt: 24/24 Punkte) bei konsequenter Einhaltung des Arbeitsbudgets.



Priorisiere fachliche Korrektheit, Stabilität, Modularität, didaktischen Nutzen und Nachvollziehbarkeit. Ich muss den gesamten Code im mündlichen Fachgespräch selbstständig erklären können.



Arbeite maximal sorgfältig, aber pragmatisch. Vermeide unnötige Zwischenschritte, Wiederholungen und übertriebene Perfektionierung.



Beginne jetzt mit dem ersten konkreten Teilschritt von Schritt 2.
### Tatsächlich verwendete Folgeprompts

1. «hat funktioniert.»

2. «Teilschritt 2.2 erfolgreich abgeschlossen. Alle drei
   Tests haben funktioniert. Weiter mit Teilschritt 2.3.»

3. «Teilschritt 2.3 erfolgreich abgeschlossen. Alle 8
   automatisierten Tests haben funktioniert.
   Weiter mit Teilschritt 2.4.»

4. «es zeigt bei RUN main.py kein Fenster an»

5. «das fenter ist erschienen»

6. «bei 4. nach git Status erscheint: git status
   Password for 'https://git status@github.com':»

7. «es scheint funktioniert zu haben. nach push
   ist keine Fehlermeldung erschienen.»

8. «wo finde ich die commit-nachricht»

9. «Teilschritt 2.5 erfolgreich abgeschlossen.
   Alle Kontrollen haben funktioniert.
   Weiter mit Teilschritt 2.6.»

### Eigene Durchführung und Funktionskontrolle

- Erstellung der Programmdateien in PyCharm
- Übernahme des vorgeschlagenen Programmcodes
- Erfolgreiche Überprüfung der Bewegungsparameter
- Erfolgreiche Durchführung manueller Berechnungstests
- Erfolgreiche Ausführung aller acht automatisierten Tests
- Erfolgreicher Start des grafischen Testprogramms
  über das Terminal
- Erstellung eines Git-Commits
- Erfolgreicher Upload auf GitHub
- Kontrolle des hochgeladenen Entwicklungsstands

### Technische und fachliche Grundlage

Das physikalische Modell verwendet die allgemeinen
Bewegungsgleichungen für Bewegungen mit konstanter
Beschleunigung.

Für die automatisierten Tests wird das in Python
integrierte Modul unittest verwendet.

Für die Erstellung des Programmcodes in diesem
Entwicklungsschritt wurden keine externen
Codeschnipsel oder zusätzlichen Bibliotheken übernommen.

### Git-Versionierung

Commit:
Implement physics motion model and automated tests

### Bekannte offene Punkte

- Integration des physikalischen Modells in die
  grafische Applikation erfolgt in späteren Schritten.
- Die Ursache des Startproblems über die
  PyCharm-Run-Konfiguration wurde nicht abschliessend
  ermittelt. Der Start über das Terminal funktioniert.

### Ergebnis

Das physikalische Bewegungsmodell ist implementiert,
getestet und versioniert.

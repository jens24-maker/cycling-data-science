# Status (wird bei jedem Coaching-Check-in aktualisiert)

Letztes Update: 03.07.2026

## Woche 1 (Baseline-Woche, 01.07.–07.07.2026)

Curriculum-Thema der Woche: Python-Auffrischung, Git/GitHub-Setup, Repo-Aufbau.

## Heute (03.07.2026, Tag 3)

Readiness gut (HRV 92, RHR 49, Schlaf 9h) — kein Downgrade, Plan lief normal, dann deutlich erweitert:

- venv eingerichtet, `requirements.txt` befüllt (numpy, pandas, matplotlib)
- Modul 2: CSV/JSON einlesen, `scripts/load_readiness_data.py` gebaut und getestet
- **Automatisierter Readiness-Daily-Export:** iPhone-Kurzbefehl → Google Apps Script Webhook → Google Sheet (HRV/RHR automatisch aus Apple Health, Schlaf manuell eingegeben, da Zepp-Schlafsegmente in Shortcuts nicht sauber summierbar waren). Sheet als CSV veröffentlicht, Automation läuft täglich morgens.
- **Apple-Health-Historie importiert:** `scripts/parse_health_export.py` — parst `data/raw/Export.xml` (669MB), filtert auf Quelle "Zepp" (andere Quellen: Athlytic, Schlaftracker, altes Gerät "iPhone von Roland" ausgeschlossen), aggregiert pro Tag → `data/health_history.csv` (321 Tage, 16.08.2025–03.07.2026). Bug gefunden+gefixt: Zepp-"InBed"-Summensatz führte zu doppelt gezählter Schlafdauer.
- **Visualisierung:** `scripts/visualize_health_history.py` — Zeitreihen mit 7-Tage-Rolling-Average für HRV/RHR/Schlaf, Korrelationsmatrix. Ergebnis: HRV↔RHR -0,56 (physiologisch plausibel), auffällige gleichzeitige Verschlechterung aller drei Metriken Ende Mai/Anfang Juni 2026 (möglicherweise die in der Übergabe erwähnte frühere Übertrainingsphase).

## Erledigt (Woche 1 bisher)

- Tag 1 (01.07.): Repo-Setup vorbereitet, Python Modul 1 noch nicht durchgeführt
- Tag 2 (02.07.): Git/GitHub-Setup komplett abgeschlossen, Python Modul 1 fertiggestellt (readiness_avg.py)
- Tag 3 (03.07.): Modul 2 fertig, automatisierter Health-Datenexport aufgebaut, historische Daten importiert+bereinigt+visualisiert — deutlich über Plan hinaus (entspricht bereits Teilen von Woche 2/3)

## Offen

- Datenqualität: manuelle Check-in-Werte (Morgen-Einzelwert) weichen leicht von Zepp-Tagesdurchschnitten ab — ggf. Readiness-Regel künftig auf Morgenwert statt Tagesdurchschnitt umstellen
- Übertrainings-Phase (Ende Mai/Juni 2026) ggf. mit Trainingsdaten (Strava) abgleichen, sobald verfügbar
- Ab Woche 2: NumPy + Pandas vertiefen mit eigenen Strava-Daten

## Hinweis

Trainingsplanung, Readiness-Log und Wochenplan liegen im Obsidian-Vault (Ideaverse), Projekt "Personal Coaching Projekt". Diese Datei hier ist der Auszug, der für Coding-Sessions relevant ist.

# cycling-data-science

Persönliches Lern- und Portfolio-Projekt von Jens im Rahmen des Data-Science-Curriculums (01.07.–01.09.2026, danach Fortsetzung). Ziel: sicher in der Arbeitsumgebung werden, Data-Science-Grundlagen lernen, Portfolio-Projekt mit eigenen Trainingsdaten (Power, HR, Schlaf, HRV) bauen.

**Aktueller Stand & heutige Aufgabe: siehe STATUS.md — wird laufend aktualisiert, immer zuerst lesen.**

## Hintergrund (Radsport-Daten)

- FTP: 178W, Körpergewicht 58,4kg → 3,05 W/kg
- Leistungszonen (aus FTP 178W):
  - Z1 Recovery: <97W
  - Z2 Endurance: 98-134W
  - Z3 Tempo: 134-160W
  - Z4 Threshold: 160-187W
  - Z5 VO2max: 187-214W
  - Z6 Anaerobic: 214-249W
  - Z7 Neuromuscular: 249W+
- Readiness-Metriken: HRV (Amazfit Helio, ~95-100 normal), RHR (47-49 normal), Schlaf (Ziel 22:00-7:00, 9h)
- Datenquellen: Strava-Export, Amazfit-Export, manuelles Daily-Log (HRV/RHR/Schlaf)

## Curriculum-Fahrplan (9 Wochen)

1. Python-Auffrischung, Git/GitHub-Setup, Repo-Aufbau
2. NumPy + Pandas mit eigenen Strava/Amazfit-Daten
3. Visualisierung + deskriptive Statistik
4. Lineare Algebra (Scientific Computing)
5. SQL Grundlagen
6. scikit-learn, Regression/Klassifikation auf eigenen Daten
7. Numerische Methoden / Scientific Computing Basics
8. Portfolio-Projekt zusammenbauen
9. Polieren, GitHub-Profil, Review, Abschluss

## Repo-Struktur

- `data/` — Rohdaten und aufbereitete Datensätze (Strava/Amazfit-Exports, Daily-Logs)
- `notebooks/` — Jupyter-Notebooks für Exploration/Analyse
- `scripts/` — wiederverwendbare Python-Skripte
- `requirements.txt` — Python-Abhängigkeiten
- `STATUS.md` — laufender Fortschritt, tagesaktuell

## Konventionen

- Commits klein und beschreibend halten.
- Neue Abhängigkeiten immer in `requirements.txt` eintragen.
- Rohdaten nicht verändern — Aufbereitung in Skripten/Notebooks, nicht manuell in den Rohdateien.
- **Code komplett auf Englisch:** Variablennamen, Funktionsnamen, Kommentare, Docstrings, print-Ausgaben, Commit-Messages, README/Dateiinhalte — alles Englisch. Gilt für alle Projekte von Jens, nicht nur dieses Repo.

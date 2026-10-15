# TrainingsApp

Persönliche Trainings-App von Nik (Handy-Web-App, läuft auf GitHub Pages:
https://nikleson-coder.github.io/TrainingsApp/). Nik schreibt Deutsch: immer auf Deutsch antworten,
einfach und ohne Fachbegriffe erklären. Er testet auf dem iPhone (Safari, „Zum Home-Bildschirm“).

## Dateien
- `src/prototyp.html` – **die Quelle**. Eine einzige Datei mit HTML, CSS und JS. Hier wird alles geändert.
- `build.py` – baut daraus `index.html` (Vollbild fürs Handy, Manifest, Service Worker) und erhöht die Cache-Version in `sw.js`.
- `index.html`, `sw.js`, `manifest.webmanifest`, `icon-*.png` – die veröffentlichte App (nicht von Hand bearbeiten, `index.html` kommt aus `build.py`).
- `docs/stand.md` – Versionsliste und alle Entscheidungen mit Nik. Vor größeren Änderungen lesen, danach eine Zeile anhängen.
- `docs/uebungen.md` – Regeln für Übungsarten und alle diktierten Übungen.

## Ablauf bei jeder Änderung
1. `src/prototyp.html` ändern.
2. Syntax prüfen: `sed -n '/<script>/,/<\/script>/p' src/prototyp.html | sed '1d;$d' > /tmp/chk.js && node --check /tmp/chk.js`
3. Im Browser testen (z. B. Playwright, Handy-Breite ~420 px), auch hell und dunkel.
4. `python3 build.py`
5. Committen und auf `main` pushen – GitHub Pages veröffentlicht automatisch, Niks App holt sich die neue Version beim nächsten Öffnen.
6. Eine Zeile in `docs/stand.md` ergänzen (Versionsnummer weiterzählen).

## Wichtig im Code
- Gespeichert wird alles im `localStorage` unter `"trainingsapp-v2"` (Logs, Routinen, eigene Übungen, Profil …). **Niemals Niks gespeicherte Daten kaputt machen**: neue Felder abwärtskompatibel einführen; einmalig eingefügte Inhalte über Flags wie `rSeedWarm1`, `rSeedCool1` steuern.
- Ansicht über `state.view` + `render()`; Klicks laufen über `data-*`-Attribute (leere Attribute mit `"x" in el.dataset` prüfen).
- Übungen: `EXERCISES[bereich] = [{ n, t: "w"|"bw"|"bwp", sec?, count?, time?, kcal? }]`
  - `w` Gewicht, `bw` Körpergewicht, `bwp` Körpergewicht + Zusatzgewicht; `sec` = Sekunden statt Wdh.
  - `count` (Schwimmen, Sprints): Satzanzahl + Zeit pro Satz; `time` (Joggen): eine Zeit; `kcal` (Peloton): Kalorien.
- Routinen (Aufwärmen/Cooldown): `state.routines = { warm: [...], cool: [...] }`, Einträge `{ n, sec }`, Player mit 10 s Pause.
- Löschen immer mit „Nochmal tippen“-Bestätigung, kein `confirm()`.
- Design: Variante „Klar“, ruhige Farben, im Hellmodus gedecktes Salbeigrün; Theme wählbar im Profil (Hell / Dunkel / Wie Handy).

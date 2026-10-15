# TrainingsApp – Stand vom 12.10.2026

Prototyp (Version 19): https://claude.ai/artifact/P5zYFCAMa5YCNc3XpCYigP
Quelldatei: prototyp.html · Übungsdaten: uebungen.json (128 Übungen aus deiner PDF)

## Aufbau
- Tabs: Heute, Plan, Split, Übungen, Verlauf
- Design „Klar“, folgt Hell-/Dunkelmodus des Handys, im hellen Modus gedämpfte Farben
- Training immer in 3 Abschnitten: Aufwärmen, Hauptteil, Cooldown
- Im Hauptteil: Ziel und „Letztes Mal“ (Wert aus dem letzten Training desselben Splits), kein PR
- Übungen-Tab: 6 Muskelgruppen, 22 Muskeln, Filter nach Bereich, Belastungs-Kasten; jede Übung zeigt „Zuletzt“ (Gewicht × Wdh.) und darunter „PR“ (höchstes Gewicht zählt)
- Verlauf: wochenweise mit KW-Pfeilen, Trainings / Stunden / in Folge
- Profil: rundes Profilbild oben rechts, Profilseite mit Foto, Körpergewicht und Körpergröße; Körpergewicht erscheint bei Körpergewichtsübungen (z. B. „Körpergewicht (90 kg) × 8“)
- Split-Ansicht: grüner Belastungs-Kasten oben

## Splits (Wochenablauf von dir festgelegt, Übungen sind Vorschläge)
- Kraftausdauer: Mo Oberkörper A, Di Unterkörper, Mi Pause, Do Lauf 10 km, Fr Oberkörper B, Sa Rad 1,5 h, So Pause
- Maximalkraft: Mo Oberkörper A, Di Unterkörper, Mi Pause, Do Kreuzheben, Fr Oberkörper B, Sa Sprints (8 × 100 m), So Pause
- Körpergewicht: Mo Push A, Di Pull A, Mi Beine & Core A, Do Pause, Fr Push B, Sa Pull B, So Beine & Core B
- Gewichtstraining: Mo Brust & Schultern, Di Rücken & hintere Schulter, Mi Beine & Core, Do Pause, Fr Oberkörper, Sa Arme, So Pause (Sonntag noch offen)

## Offen
- Übungsauswahl je Tag bestätigen oder tauschen
- Werte bei „Letztes Mal“ sind Beispiele
- Aufwärmen und Cooldown noch Platzhalter
- Eintragen von Gewicht/Wiederholungen und PRs
- Entscheidung Technik (Vorschlag: installierbare Web-App)

## Stand Version 27 (12.10.2026)
- Alle Beispielwerte entfernt (keine Ziele, keine erfundenen Gewichte/Wdh., kein Beispiel-Verlauf). Die App startet leer.
- Training läuft Schritt für Schritt: Aufwärmen, dann jede Übung einzeln (Satzanzahl wählen, je Satz kg × Wdh.), dann Cooldown, dann „Training abschließen“. Die Einträge speisen „Letztes Mal“ (gleicher Split), „Zuletzt“ und „PR“.
- Im Split lässt sich jeder Trainingstag im Wochenablauf antippen und zeigt das Training.
- Übungslisten je Tag sind noch Vorschläge. Als Nächstes legt Nik die Übungen je Training fest, beginnend mit Kraftausdauer Montag Oberkörper A.

- Version 28: Im Übungen-Tab gibt es unter „Ausdauer“ die Bereiche Laufen (Joggen, Sprinten) und Fahrrad (draußen, Peloton zu Hause). Am Radtag wählt man im Training Draußen oder Peloton.

- Version 29: Kraftausdauer Mo Oberkörper A hat im Hauptteil die Bereiche Rücken, Brust, Schultern, Arme mit je 2 frei wählbaren Übungen aus der Kraftausdauer-Liste (beliebige Reihenfolge, Bereiche mischbar). Aufwärmen und Cooldown folgen.
- Version 30: Hauptteil zeigt nur die Bereiche Rücken, Brust, Schultern, Arme zum Antippen. Im Bereich „Erste Übung“ / „Zweite Übung“; nach „Übung abschließen“ zurück zum Bereich.
- Version 31: Bereiche sind überall antippbar, auch im Split-Wochenablauf (öffnet das Training am nächsten passenden Tag, nur beim aktiven Split) und bei bereits abgeschlossenen Trainings (Einträge bleiben bearbeitbar).
- Version 32: Jedes Training lässt sich aus dem Split-Wochenablauf heraus starten, auch wenn der Split nicht aktiv ist („Training jetzt starten“, gespeichert mit heutigem Datum). Abhaken im Plan nur für den aktiven Split.

## Weiter am 13.10.2026
- Gemeinsam mit Nik jedes Training aller vier Splits fertig festlegen (Muster: Kraftausdauer Mo Oberkörper A = Bereiche mit je 2 frei wählbaren Übungen aus der Split-Liste).
- Danach Aufwärmen und Cooldown je Training; Nik bereitet die Inhalte vor.
- Prototyp-Stand: Version 32, Quelle prototyp.html (Arbeitskopie im Scratchpad geht mit der Sitzung verloren, diese Datei ist maßgeblich).

## 13.10.2026
- Version 33: Alle Übungen gelöscht (Übungen-Tab je Muskel leer) und die Einteilung der Übungen nach Kraftausdauer/Maximalkraft/… entfernt. Nik trägt die Übungen selbst neu ein, ohne Einteilung. Muskelgruppen, Ausdauer (Laufen, Fahrrad) und der Ablauf von Oberkörper A bleiben. Die Übungsvorschläge der übrigen Trainingstage sind ebenfalls entfernt.
- Version 34: Kraftausdauer Di Unterkörper: Hauptteil mit Bereichen Beine (8 Übungen frei wählbar) und Laufen (1 Übung: Joggen oder Sprinten).
- Version 35: Kraftausdauer Do Lauf: Hauptteil = Bereich Laufen mit 1 frei wählbaren Übung.
- Version 36: Donnerstag heißt jetzt „Laufen“ statt „Lauf 10 km“.
- Version 37: Kraftausdauer Fr Oberkörper B wie Oberkörper A (Rücken, Brust, Schultern, Arme, je 2 wählbar).
- Version 38: Kraftausdauer Sa heißt „Fahrrad“, Hauptteil = Bereich Fahrrad mit 1 wählbaren Übung (draußen / Peloton). Damit sind alle Kraftausdauer-Hauptteile festgelegt.
- Version 39: Maximalkraft: Mo/Fr Oberkörper A/B = Brust, Rücken, Schultern, Arme je 2; Di Unterkörper = Beine 7; Sa Sprints = Laufen 3. Do Kreuzheben noch offen.
- Version 40: Überschrift im Übungen-Tab nur „Übungen“. Unter Kraft nach Core neuer Bereich „Gesamtkörper“ ohne Muskeln, Übungen direkt darin.
- Version 41: Ausdauer um „Schwimmen“ ergänzt (noch ohne Übungen).
- Version 42: Ausdauer wie die Muskelgruppen aufgebaut: Laufen → Joggen, Sprinten; Fahrrad → Fahrrad draußen, Peloton zu Hause; Schwimmen noch ohne Unterbereiche. Übungen kommen in die Unterbereiche (noch leer).
- Version 43: Maximalkraft Do Kreuzheben = Gesamtkörper mit 2 frei wählbaren Übungen. Damit sind alle Maximalkraft-Hauptteile festgelegt.
- Version 44: Gewichtstraining: Mo Brust 4 + Schultern 4; Di „Rücken & Schulter“ (umbenannt) Rücken 6 + Schultern 2; Mi Beine 7 + Core 2; Fr Brust 2, Rücken 2, Schultern 3, Arme 2; Sa Arme 8. Alle frei wählbar.
- Version 45: Kraftausdauer Oberkörper A und B: Schultern 3 statt 2 Übungen.
- Version 46: Neuer Abschnitt „Skills“ im Übungen-Tab mit Oberkörper und Unterkörper, Übungen direkt darin (wie Gesamtkörper).
- Version 47: Skills heißen „Oberkörper-Skills“ / „Unterkörper-Skills“. Körpergewicht Mo Push A: Brust 3, Schultern 2, Arme 1, Oberkörper-Skills 1 (Anzahl noch zu bestätigen).
- Version 48: Körpergewicht komplett: Push A/B = Brust 3, Schultern 2, Arme 1, Oberkörper-Skills 1; Pull A/B = Rücken 3, Schultern 2, Arme 1, Oberkörper-Skills 1; Beine & Core A = Beine 6, Core 3, Laufen 1; Beine & Core B = Beine 6, Core 3, Fahrrad 1. Damit sind alle Hauptteile aller Splits festgelegt. Offen: Übungen eintragen, Aufwärmen, Cooldown, Unterbereiche Schwimmen.
- Version 49: Körpergewicht Push A/B und Pull A/B: Arme 2 statt 1.
- Version 50: Eigene Splits erstellen und alle Splits bearbeiten (Name, Belastung, Wochenablauf mit Kraft/Ausdauer/Skills/Rest Day, Trainingsname, Hauptteil-Bereiche mit Anzahl). Lauf/Rad heißen in den Wochenabläufen jetzt „Ausdauer“.
- Version 51: Ausdauer überall in Türkis.
- v52 (13.10.): Verlauf mit Umschalter Wochenansicht/Monatsansicht. Monatsansicht = Kalender mit Monatspfeilen, grüner Kreis erledigt, roter Kreis verpasst, Ring offen (heute/aktuelle Woche), nichts an Rest Days; heute als hinterlegte Zelle; Monatsstatistik (Trainings, Stunden, % geschafft).
- v53 (13.10.): Heute-Feld im Kalender grau gefüllt mit weißem Rand (hell: dunkler Rand), mehr Abstand zwischen Umschalter und Überschrift Verlauf.
- v54 (13.10.): Tab und Überschrift "Übungen" heißen jetzt "Training"; Zeile "6 Muskelgruppen · 22 Muskeln" entfernt. Nächster Schritt: Bereich Aufwärmen & Cooldown im Training-Tab (Nik: sein Aufwärmen ist immer gleich).
- v55 (13.10.): Tab "Plan" aus der Leiste entfernt (Leiste: Heute, Split, Training, Verlauf). Auf Heute ersetzt eine umrandete Karte "Wochenplan" (Überschrift, Diese Woche · KW, Tageskreise) den Abschnitt "Ganzer Plan"; Antippen öffnet den Wochenplan mit "‹ Heute" zurück.
- v56 (13.10.): Neuer Tab "Rahmen" (Symbol: Rahmen = zwei ineinanderliegende Quadrate) zwischen Split und Training, für Aufwärmen & Cooldown (gleich für alle Trainings). Seite zeigt vorerst zwei leere Karten Aufwärmen / Cooldown.
- v57 (13.10.): Rahmen → Aufwärmen bzw. Cooldown öffnet Seite "Routinen": eigene Routinen mit Namen anlegen (+ Neue Routine erstellen), öffnen, umbenennen, löschen; gespeichert (state.routines.warm/cool). Inhalte der Routinen und Aktivieren (wie Split) folgen mit Nik.
- v58 (13.10.): Löschen von Routinen und eigenen Splits repariert: Bestätigungsdialoge (confirm) sind im Artifact blockiert, jetzt zweimal tippen ("Wirklich löschen? Nochmal tippen", rot). Keine confirm()/alert() verwenden.
- v59 (13.10.): Aufwärmen und Cooldown im Training zeigen "Routine wählen" (antippbar). Auswahl aus den Rahmen-Routinen; Routine wird als Liste angezeigt, "Andere Routine wählen". "✓ Aufwärmen erledigt · zum Hauptteil" hakt Aufwärmen ab und geht zum Hauptteil; Cooldown: "✓ Cooldown erledigt · Training abschließen". Gewählte Routine bleibt pro Training gespeichert (state.rpicks). Routinen-Seite: Inhalte hinzufügen (Feld + Hinzufügen/Enter) und entfernen (✕). Je eine Beispielroutine angelegt (Beispiel-Aufwärmen, Beispiel-Cooldown).
- v60 (13.10.): Beispielroutinen wieder entfernt (auch aus gespeicherten Daten). Nik hat den Routinen-Ablauf im Training abgenommen ("genau so soll das funktionieren"). Nächster Schritt: Niks echte Aufwärm- und Cooldown-Routinen anlegen.
- v61 (13.10.): Kraft-Bereiche (Rücken, Brust, Schultern, Arme, Beine, Core) ohne einzelne Muskeln, Übungen direkt drin wie bei Gesamtkörper. Unten in jedem Kraft- und Skills-Bereich gestrichelt "+ Übung hinzufügen" → Namensfeld, "Übung speichern" (Enter) / Abbrechen. Eigene Übungen gespeichert (state.userEx) und im Training auswählbar. Ausdauer bleibt mit Unterbereichen.
- v62 (13.10.): Übungsarten: Mit Gewicht (kg × Wdh.), Körpergewicht (nur Wdh., Anzeige "Körpergewicht (Profilgewicht) × n Wdh."), Körpergewicht + Zusatzgewicht (+ kg × Wdh.). Art beim Hinzufügen wählbar, unter dem Namen angezeigt. Zuletzt/PR je Art: PR = höchstes (Zusatz-)Gewicht, bei Körpergewicht = meiste Wdh. Rücken: Shrugs mit Langhantel, Shrugs mit Kurzhantel (Gewicht), Farmer Carries mit Zusatzgewicht (KG + Zusatz).
- v63 (13.10.): Rücken komplett (22 Übungen): Shrugs LH/KH, Farmer Carries m. Zusatzgewicht, Rudern breit (Kabelturm, Maschine, LH, KH), Australian Pull-ups (KG / + Zusatz), Klimmzüge breit (KG / + Zusatz), Klimmzüge eng (KG / + Zusatz), Latzug (Kabelturm, Maschine), Überzüge am Kabelturm, Rudern eng (Kabelturm, Maschine), Rudern eng einarmig (KH, Maschine), Hyperextensions (KG / + Zusatz).
- v64 (13.10.): Brust komplett (15 Übungen): Schrägbankdrücken (KH, LH, Maschine), Butterfly von unten nach oben am Kabelturm, Liegestütze (KG / + Zusatz), Flachbankdrücken (LH, KH), Brustpresse, Butterfly (Maschine, Kabelturm), Dips (KG / + Zusatz), Butterfly von oben nach unten am Kabelturm, Brustpresse nach unten.
- v65 (13.10.): Schultern komplett (22 Übungen): Schulterdrücken (Maschine, KH, LH), Frontheben (KH ein-/beidarmig, Kabelturm ein-/beidarmig, LH), Pike Push-ups (KG / + Zusatz), Seitheben (KH einarmig, Kabelturm ein-/beidarmig, Maschine ein-/beidarmig), Reverse Butterfly (Maschine, KH, Kabelturm je ein-/beidarmig), Face Pulls. Offen: Seitheben mit KH beidarmig fehlt in Niks Liste (nachgefragt).
- v66 (13.10.): Arme komplett (21 Übungen): Hammer Curls (KH, Kabelturm ein-/beidarmig), Reverse Grip Curls (SZ, Kabelturm), Curls vorm Körper (KH, Kabelturm ein-/beidarmig, SZ), Curls hinterm Körper (KH, Kabelturm), Spider Curls (KH, SZ), Skull Crusher (KH ein-/beidarmig, SZ), Überkopf-Trizepsdrücken am Kabelturm (bei-/einarmig), Trizeps-Pushdowns am Kabelturm (ein-/beidarmig), Enge Liegestütze (KG). Doppelt Diktiertes nur einmal; "Form Körper" = vorm Körper.
- v67 (13.10.): Arme + Unterarmcurls (KH, LH, Kabelturm ein-/beidarmig) und Deadhangs (KG, Wdh.) → 26 Übungen.
- v68 (13.10.): Arme + Deadhangs mit Zusatzgewicht → 27 Übungen.
- v69 (13.10.): Beine komplett (29 Übungen): Squats (KG), Squats mit LH, Beinpresse, Bulgarian Split Squats (KG/+Z), Box Jumps (KG/+Z), Box Jumps einbeinig (KG/+Z), Beinstrecker Maschine, Ausfallschritte (KG/+Z), Beinbeuger Maschine, Romanian Deadlifts (LH, KH), Squats einbeinig auf dem Wackelpad (KG/+Z), Abduktorenheben einbeinig (KG), Wandsitzen (KG/+Z), Wadenpresse Maschine, Wadenheben beidbeinig (KG/+Z), Wadenheben einbeinig (KG/+Z), Adduktorenmaschine, Abduktorenmaschine, Fersenheben einbeinig (KG/+Z).
- v70 (13.10.): Core komplett (18 Übungen): Crunches (KG/+Z, Maschine, Kabelturm), Crunches auf der Schrägbank (KG/+Z), Leg Raises (KG/+Z), Plank (KG/+Z), Side Plank (KG/+Z), Russian Twist (KG/+Z), Side Crunches (KG/+Z), Side Crunches auf der Schrägbank (KG/+Z).
- v71 (13.10.): Übungen auf Zeit (Flag sec): Eingabe und Anzeige in Sek. statt Wdh. (z. B. "Körpergewicht (90 kg) + 30 kg × 45 Sek."). Bisher: Farmer Carries mit Zusatzgewicht. Weitere nennt Nik.
- v72 (13.10.): Weitere Zeit-Übungen (Sek. statt Wdh.): Deadhangs (KG/+Z), Abduktorenheben einbeinig, Wandsitzen (KG/+Z), Plank (KG/+Z), Side Plank (KG/+Z), Russian Twist (KG/+Z). Insgesamt 12 mit Farmer Carries.
- v73 (13.10.): Routinen mit Timer: jede Übung der Routine hat eine Dauer (Sek.). Neue Routinen heißen automatisch "Erste Routine", "Zweite Routine" … Im Training "▶ Routine starten": Vollbild nur mit aktueller Übung oben und großer Zeit in der Mitte; nach jeder Übung 10 Sek. Pause mit "Nächste Übung: …" (orange); Signalton/Vibration bei Wechsel; Pause/Beenden unten; am Ende "Geschafft!" → Aufwärmen abgehakt, weiter zum Hauptteil (Cooldown: zurück zum Cooldown).
- v74 (13.10.): Aufwärmen "Erste Routine" angelegt (16 Übungen, 15 Min inkl. Pausen): Unga Bunga 1', Oben-Mitte-Unten Stretch 1', Armkreisen 1', Spagatschritt mit Füße antippen 30", World's Best Stretch rechts 1' / links 1', Cat and Cow 30", Herabschauender Hund 30", Cobra mit Nacken drehen 30", Embryostellung und Schulterblätter dehnen 30", Handgelenke aufwärmen 1', Fersensitz 1' (Nik: "Fuß sitzen"), Kreuzsitz drehen 30", Kreuzsitz Waden heben 30", Rotatoren rechts 1' / links 1'.
- v75 (13.10.): Routine-Player: drei Knöpfe unten (Beenden links, Pause Mitte, "Nächste Übung ›" rechts). Überspringen: Übung → 10-Sek.-Pause mit Vorschau → nächste Übung; in der Pause → direkt nächste Übung; letzte Übung → Geschafft.

## Stand gesichert 13.10.2026, 17:40 (Version 75)
- Handy-Demo (bildschirmfüllend, ohne Rahmen/Erklärung): eigenes Artifact, Datei /mnt/project-files/trainingsapp/TrainingsApp-Demo.html. Wird aus prototyp.html erzeugt (Head mit viewport/Home-Screen-Metas + CSS-Override am Ende des Styles). Bei neuen Versionen Demo neu erzeugen und unter derselben Demo-URL veröffentlichen.
- Offen: Cooldown-Routine (Nik diktiert), Gesamtkörper-Übungen, Frage "Seitheben mit Kurzhanteln beidarmig", Ausdauer-/Skills-Übungen, Schwimmen-Unterbereiche, Niks Feedback aus dem Handy-Test.
- v76 (13.10.): Profil → unten "Darstellung": Hellmodus / Dunkelmodus / Wie Handy (gespeichert). Demo neu erzeugt (mkdemo.py in trainingsapp/).
- 13.10. 18:08: Installierbares Web-App-Paket /mnt/project-files/trainingsapp/TrainingsApp-WebApp.zip (index.html = Demo + manifest + Service Worker für offline, Icons 180/192/512 aus icon.js). Nik soll es über Netlify Drop hosten und per "Zum Home-Bildschirm" installieren. Bei Änderungen: Demo neu erzeugen (mkdemo.py), Paket neu bauen.
- 13.10. abends: App auf GitHub (Nikleson-coder/TrainingsApp, main) hochgeladen; Adresse https://nikleson-coder.github.io/TrainingsApp/ nach Pages-Freischaltung.
- v77: Schultern + Seitheben mit Kurzhanteln beidarmig. Deploy: scratchpad/deploy.sh vNN "msg" (baut Demo + PWA, pusht nach GitHub).
- v78: Oberkörper-Skills (8): Muscle Up KG/+Z, Handstand KG/+Z (Sek.), Handstand Push-ups KG/+Z, Front Lever (Sek.), Planche (Sek.).
- v79: Unterkörper-Skills (3): Pistol Squats KG/+Z, Rückwärtssalto (KG, Wdh.).
- v80: Schwimmen Unterbereiche Dauerschwimmen (500/750/1000/1500/2000 m) und Intervallschwimmen (50/100/150/200 m); Flag count:true → im Training nur 'Wie viele Sätze?' (1–10), Log {c}; Training-Tab zeigt nur Namen.
- v81: Schwimmen: nach Satzanzahl 'Zeit pro Satz' (min : Sek.), Log sets [{t: Sek.}]; Training-Tab Zuletzt (beste Zeit · n Sätze) + PR (schnellste Zeit).
- v82: Fahrrad › Peloton zu Hause: Peloton 30/45/60/90 Minuten, Flag kcal:true → im Training nur 'Verbrannte Kalorien'; Training-Tab Zuletzt/PR in kcal (PR = höchste kcal). Fahrrad draußen noch leer.
- v83: Laufen › Joggen: 3/5/8/10/12,5/15 km Joggen (Flag time:true → eine Zeit min:Sek., PR = schnellste); Sprinten: 20/50/100 m Sprint (count: 'Wie viele Sprints?' + Zeit pro Sprint).
- v84: Gesamtkörper: Kreuzheben (Gewicht), Burpees (KG).
- v85 (14.10.): Cooldown-Routinen leer angelegt (Flag rSeedCool1): Cooldown Push, Pull, Arme, Beine, Laufen, Fahrradfahren. Inhalt + Zeiten diktiert Nik später.
- v86 (15.10.): Handy-Ansicht: Leiste unten bündig bis zum Rand (keine dunkle Fläche mehr), oben weniger Abstand (Safe-Area − 12 px, Inhalt ohne Extra-Abstand). Geändert in build.py.
- v87 (15.10.): Dunkle Fläche unter der Leiste (iOS-Home-Bildschirm-App zu kurz): App im Standalone-Modus 100vh hoch, Hintergrund = Leistenfarbe; Tab-Leiste oben/unten gleicher Abstand (12 px).
- v88 (15.10.): Service Worker holt Dateien mit cache: no-cache, damit neue Versionen sofort ankommen (GitHub Pages cached sonst bis 10 Min.).
- v89 (15.10.): Tab-Leiste höher über dem iPhone-Home-Strich (oben/unten je Safe-Area − 16 px, ca. 18 px), oben wieder etwas mehr Abstand (Safe-Area − 2 px).
- v90 (15.10.): Überschriften von Split, Rahmen, Training auf gleicher Höhe wie „Hallo Nik“ (leere Datumszeile darüber); Profilbild richtet sich per JS an der Überschrift aus (im Verlauf tiefer, neben „Verlauf“).
- v91 (15.10.): Routine-Player: Geschafft-Haken ohne schwarze Füllung, größer (140 px) und dicker; Button nur „Nächste Übung“ (ohne Pfeil).
- v92 (15.10.): Nach „Übung abschließen“ direkt zurück zum Hauptteil. „Training abgeschlossen“ nicht mehr antippbar; darunter rötlich „Training zurücksetzen“ (zweimal tippen), erscheint nur bei abgeschlossenem Training; eingetragene Sätze bleiben gespeichert.
- v93 (15.10.): Routinen (Rahmen): unter „Übung + Sek. + Plus“ neue Zeile „Pause + Sek. + ✓“. Pause pro Routine gespeichert (Feld `pause`, Standard 10 s), gilt im Player zwischen allen Übungen und in der Gesamtzeit; 0 = ohne Pause.
- v94 (15.10.): Alle geschätzten Minutenangaben entfernt (Heute-Karte, Morgen, Wochenplan, Split-Übersicht „Ø Min“, Split-Tage, Training-Kopf, Phasen-Legende, Abschnitte, Hauptteil-Karte, Verlauf-Zeilen und „Stunden“-Kachel). Phasenbalken jetzt gleich breit. Echte Zeiten bleiben: Übungszeiten der Routinen und die daraus berechnete Routinendauer (auch im Training statt der Schätzung).
- v95 (15.10.): Konten vorbereitet (Firebase): Anmelden, Registrieren (Vorname, E-Mail, Passwort, Gewicht, Größe), Bestätigungs-Mail, Passwort vergessen, Abmelden im Profil, Vorname im Profil änderbar, „Hallo <Vorname>“. Daten je Konto (localStorage `trainingsapp-v2:<uid>` + Firestore `users/<uid>`.state als JSON, neuerer Stand gewinnt über `savedAt`). Das erste Konto auf einem Handy übernimmt die bisherigen Daten (`trainingsapp-claimed`). Aktiv erst, wenn `FIREBASE_CONFIG` gesetzt ist; bis dahin startet die App wie bisher. sw.js speichert nur noch eigene Dateien und gstatic zwischen.
- v96 (15.10.): App heißt jetzt „Alpha-Sports“ (Manifest, Titel, Home-Bildschirm-Name, Anmeldeseite). Anmeldung eingeschaltet (`AUTH_ON = true`); Firebase-Projekt trainingsapp-f379b geprüft: E-Mail-Anmeldung an, Domain erlaubt, Firestore-Regeln greifen. Echter Test: Registrieren → Mail → „E-Mail bestätigen“, Testkonto danach gelöscht. Vorschau-Artefakte laufen ohne Anmeldung (`window.TA_DEMO`).
- v97 (15.10.): Anmeldeseite: „Willkommen bei Alpha-Sports“ groß wie „Anmelden“ (Alpha-Sports ohne Trennung), alle Anmelde-Seiten senkrecht mittig.
- v98 (15.10.): Anmeldeseite: „Willkommen bei Alpha-Sports!“ (mit Ausrufezeichen) nach oben geschoben, etwas über der Mitte zwischen oberem Rand und „Anmelden“; Anmelden und alles darunter bleibt mittig.
- v99 (15.10.): Phasenbalken (Aufwärmen | Hauptteil | Cooldown) im Verhältnis 1 : 4 : 1 statt gleich breit.
- v100 (15.10.): Profil: Vorname-, Gewicht- und Größenfeld beginnen an derselben Stelle; Gewicht und Größe gleich breit, Einheiten (kg/cm) in fester Breite; Vorname endet rechts bündig mit den Einheiten. Auch im Registrieren-Formular.
- v101 (15.10.): Hellmodus: Hintergrund nicht mehr weiß, sondern das bisherige Kästchen-Grau (#F4F6F4); Kästchen etwas dunkler (#E8ECE9), Linien und Statusleiste/Tab-Leiste angepasst.
- v102 (15.10.): Vorschläge von anderen: eigene Übungen, eigene Splits und Routinen (mit Übungen) landen in Firestore `shared/<uid>_<hash>` {type ex|split|routine, by, byName}. Unter „+ Übung hinzufügen“, „+ Eigenen Split erstellen“ (auch im neuen Split) und „+ Neue Routine erstellen“ (auch in leerer Routine) erscheint „Vorschläge · … von anderen“, nur was man noch nicht hat (Übung: gleicher Name im Bereich; Split/Routine: gleicher Inhalt). Splits/Routinen ansehen, dann „Übernehmen“; Übungen direkt übernehmen. Braucht neue Firestore-Regeln für `shared`.
- v103 (15.10.): Vorschläge anonym (kein „von Name“, kein Name mehr in Firestore `shared`; alte Einträge werden beim nächsten Speichern ohne Namen neu geschrieben). Einführung beim ersten Anmelden: 5 Schritte (Heute, Split, Rahmen, Training, Verlauf), Karte über dem jeweiligen Tab, Zurück/Weiter/Überspringen, Flag `tutDone`; im Profil „Einführung nochmal ansehen“.
- v104 (15.10.): Einführung als geführter Klick-Rundgang (35 Schritte): alles abgedunkelt, nur die markierte Stelle ist antippbar (sonst „Weiter“). Ablauf Profil (Vorname, Gewicht, Größe, Darstellung, Abmelden) → heutiges Training (Aufwärmen, Hauptteil, Cooldown, Start-Knopf) → Morgen, Rest Day, Wochenplan → Split → Rahmen (Aufwärmen, Cooldown) → Training → Verlauf (Woche, Monat). Rundgang navigiert selbst, startet und speichert nichts außer `tutDone`; Schritte ohne Ziel (z. B. Abmelden in der Vorschau) werden übersprungen. Ist heute Rest Day, zeigt er das nächste Training.

#!/usr/bin/env python3
"""Baut die Handy-App (index.html) aus src/prototyp.html.

Aufruf:  python3 build.py
- übernimmt den Prototyp, entfernt Rahmen/Erklärtext (Vollbild fürs Handy),
- ergänzt Manifest, Icons und Service Worker,
- erhöht die Cache-Version in sw.js, damit Handys die neue Version laden.
Danach committen und auf main pushen: GitHub Pages veröffentlicht automatisch.
"""
import re, pathlib
root = pathlib.Path(__file__).parent
s = (root / "src/prototyp.html").read_text()
HEAD = '<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, user-scalable=no">\n<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">\n<meta name="apple-mobile-web-app-title" content="Training">\n<title>Training</title>\n<link rel="manifest" href="manifest.webmanifest">\n<link rel="apple-touch-icon" href="icon-180.png">\n<link rel="icon" href="icon-192.png">\n<meta name="theme-color" content="#111613">'
CSS = '\n/* ---------- Demo fürs Handy: App füllt den ganzen Bildschirm, kein Rahmen, keine Erklärung ---------- */\nhtml, body { margin: 0; height: 100%; overflow: hidden; background: var(--a-tabbg); }\n.page { display: block; max-width: none; padding: 0; margin: 0; }\n.intro, .statusbar { display: none !important; }\n.phone { position: fixed; top: 0; right: 0; bottom: 0; left: 0; width: 100%; max-width: none; height: auto; margin: 0; border: 0; border-radius: 0; box-shadow: none; padding-top: max(0px, calc(env(safe-area-inset-top, 0px) - 12px)); }\n.tabbar { padding-bottom: max(10px, env(safe-area-inset-bottom, 0px)); }\n.screen { padding-top: 0; }\n.screen { -webkit-overflow-scrolling: touch; }\n</style>'
assert s.count("<title>TrainingsApp Prototyp</title>") == 1
s = s.replace("<title>TrainingsApp Prototyp</title>", HEAD, 1)
s = s.replace("</style>", CSS, 1)
s = s.rstrip() + '\n<script>if ("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js").catch(() => {});</script>\n'
(root / "index.html").write_text(s)
sw = (root / "sw.js").read_text()
n = int(re.search(r"trainingsapp-v(\d+)", sw).group(1)) + 1
(root / "sw.js").write_text(re.sub(r"trainingsapp-v\d+", "trainingsapp-v%d" % n, sw))
print("index.html gebaut, Cache-Version v%d" % n)

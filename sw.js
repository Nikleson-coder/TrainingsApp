// Offline: App-Dateien zwischenspeichern, Seite zuerst aus dem Netz holen (immer frisch, ohne Browser-Cache)
const C = "trainingsapp-v98";
self.addEventListener("install", e => { e.waitUntil(caches.open(C).then(c => c.addAll(["./", "index.html", "manifest.webmanifest", "icon-192.png", "icon-512.png", "icon-180.png"]))); self.skipWaiting(); });
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(k => Promise.all(k.filter(x => x !== C).map(x => caches.delete(x))))); self.clients.claim(); });
self.addEventListener("fetch", e => { if (e.request.method !== "GET") return;
  // Nur eigene Dateien und die Firebase-Bibliotheken zwischenspeichern, nie die Datenbank-Verbindung
  const o = new URL(e.request.url).origin; if (o !== location.origin && o !== "https://www.gstatic.com") return;
  e.respondWith(fetch(e.request, { cache: "no-cache" }).then(r => { const cp = r.clone(); caches.open(C).then(c => c.put(e.request, cp)); return r; }).catch(() => caches.match(e.request).then(r => r || caches.match("index.html")))); });

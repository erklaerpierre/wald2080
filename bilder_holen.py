#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lädt je Baumart ein frei lizenziertes Foto von Wikimedia Commons nach bilder/<id>.jpg
und trägt Urheber, Lizenz und Quelle in bilder/quellen.csv ein.

AUFRUF (auf einem Rechner mit Internetzugang):
    python3 bilder_holen.py                 # alle Arten, die noch kein Bild haben
    python3 bilder_holen.py fichte buche    # nur diese IDs
    python3 bilder_holen.py --neu           # vorhandene Bilder ersetzen

WICHTIG
  * Es werden nur Dateien mit CC0, Public Domain, CC BY oder CC BY-SA übernommen (keine NC/ND).
  * CC BY / CC BY-SA verlangen die Namensnennung – sie steht auf der Kartenrückseite und in 13_Bildquellen.pdf.
  * Das Skript wählt automatisch das erste passende Suchergebnis. PRÜFE JEDES BILD AUGENSCHEINLICH
    (richtige Baumart? aussagekräftig? Qualität?) und tausche ggf. gegen ein besseres aus – dann Zeile in quellen.csv anpassen.
  * Hinweis: Dieses Skript konnte in der Entwicklungsumgebung nicht gegen den Live-Server getestet werden
    (Wikimedia war dort gesperrt); die Auswertung der Antworten ist mit Testdaten geprüft.
Nur Standardbibliothek + Pillow nicht nötig.
"""
import csv, json, os, re, sys, time, urllib.parse, urllib.request, html

BASE = os.path.dirname(os.path.abspath(__file__))
BILD = os.path.join(BASE, "bilder")
API = "https://commons.wikimedia.org/w/api.php"
UA = "Wald2080-Bildsuche/0.4 (Lehrmaterial; https://example.org/wald2080)"   # eigene Kontaktadresse eintragen!
ERLAUBT = re.compile(r"^(cc0|public domain|pd|cc[ -]by([ -]sa)?[ -]\d(\.\d)?|cc[ -]by([ -]sa)?)", re.I)
VERBOTEN = re.compile(r"((?<![a-z])(nc|nd)(?![a-z])|non-?commercial|noderiv|fair use|gfdl only)", re.I)


def lizenz_ok(kurz):
    kurz = (kurz or "").strip()
    return bool(kurz) and bool(ERLAUBT.match(kurz)) and not VERBOTEN.search(kurz)


def text(v):
    return html.unescape(re.sub(r"<[^>]+>", "", v or "")).strip()


def waehle(pages, latein):
    """Wählt aus der Commons-Antwort (query.pages) das beste Bild: Querformat, JPEG, >= 1000 px, erlaubte Lizenz."""
    kandidaten = []
    for p in (pages or {}).values():
        ii = (p.get("imageinfo") or [None])[0]
        if not ii: continue
        md = ii.get("extmetadata", {})
        lic = text(md.get("LicenseShortName", {}).get("value"))
        if not lizenz_ok(lic): continue
        if ii.get("mime") != "image/jpeg": continue
        w, h = ii.get("width", 0), ii.get("height", 0)
        if w < 1000 or h < 600 or w < h: continue
        titel = p.get("title", "")
        gattung = latein.split()[0].lower()
        punkte = (3 if gattung in titel.lower() else 0) + (2 if latein.lower() in titel.lower() else 0)
        if re.search(r"(range|map|distribution|leaf|blatt|seed|herbarium|illustration|drawing|stamp)", titel, re.I): punkte -= 3
        kandidaten.append((punkte, p.get("index", 99) * -1, p, ii, md, lic))
    if not kandidaten: return None
    kandidaten.sort(key=lambda t: (t[0], t[1]), reverse=True)
    _, _, p, ii, md, lic = kandidaten[0]
    return dict(titel=p["title"], url=ii.get("thumburl") or ii["url"], seite=ii.get("descriptionurl", ""),
                urheber=text(md.get("Artist", {}).get("value")) or "unbekannt", lizenz=lic)


def api(params):
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return json.load(urllib.request.urlopen(req, timeout=30))


def suche(latein):
    d = api({"action": "query", "format": "json", "generator": "search", "gsrsearch": f"{latein} filetype:bitmap",
             "gsrnamespace": 6, "gsrlimit": 20, "prop": "imageinfo", "iiprop": "url|size|mime|extmetadata", "iiurlwidth": 1400})
    return d.get("query", {}).get("pages", {})


def lade(url, ziel):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r, open(ziel, "wb") as f:
        f.write(r.read())


def lese_quellen():
    fn = os.path.join(BILD, "quellen.csv")
    if not os.path.exists(fn): return {}
    with open(fn, encoding="utf-8-sig") as f:
        return {r["id"]: r for r in csv.DictReader(f, delimiter=";")}


def schreibe_quellen(q):
    felder = ["id", "name", "latein", "datei", "urheber", "lizenz", "quelle_url", "bildtitel", "geprueft"]
    with open(os.path.join(BILD, "quellen.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=felder, delimiter=";", extrasaction="ignore")
        w.writeheader()
        for k in q: w.writerow(q[k])


def main(argv):
    sys.path.insert(0, BASE)
    from data import SPECIES_LIST
    neu = "--neu" in argv
    ids = [a for a in argv if not a.startswith("--")]
    q = lese_quellen()
    os.makedirs(BILD, exist_ok=True)
    for sp in SPECIES_LIST:
        if ids and sp["id"] not in ids: continue
        ziel = os.path.join(BILD, sp["id"] + ".jpg")
        if os.path.exists(ziel) and not neu:
            continue
        try:
            treffer = waehle(suche(sp["latin"]), sp["latin"])
        except Exception as e:
            print(f'{sp["id"]:16} FEHLER {e}'); continue
        if not treffer:
            print(f'{sp["id"]:16} kein passendes freies Bild gefunden – bitte manuell suchen'); continue
        lade(treffer["url"], ziel)
        q[sp["id"]] = dict(id=sp["id"], name=sp["name"], latein=sp["latin"], datei=sp["id"] + ".jpg", urheber=treffer["urheber"],
                           lizenz=treffer["lizenz"], quelle_url=treffer["seite"], bildtitel=treffer["titel"], geprueft="nein")
        schreibe_quellen(q)
        print(f'{sp["id"]:16} ok  {treffer["lizenz"]:14} {treffer["titel"][:60]}')
        time.sleep(1.0)
    print("Fertig. Bitte alle Bilder ansehen und in quellen.csv 'geprueft' auf 'ja' setzen.")


if __name__ == "__main__":
    main(sys.argv[1:])

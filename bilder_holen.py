#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lädt je Baumart frei lizenzierte Fotos von Wikimedia Commons – einheitlich nach Ansicht:

  baum    ganzer Baum (Habitus, Einzelbaum)   -> bilder/<id>.jpg           (Bild auf der Kartenrückseite)
  rinde   Rinde / Stamm                       -> bilder/details/<id>_rinde.jpg
  blatt   Blätter / Nadeln                    -> bilder/details/<id>_blatt.jpg
  frucht  Früchte / Samen / Zapfen            -> bilder/details/<id>_frucht.jpg
  bluete  Blüten / Kätzchen                   -> bilder/details/<id>_bluete.jpg

Urheber, Lizenz und Quelle landen in bilder/quellen.csv (Hauptbild) bzw. bilder/details/quellen.csv.

AUFRUF (auf einem Rechner mit Internetzugang):
    python3 bilder_holen.py                      # Hauptbild (ganzer Baum) für alle Arten ohne Bild
    python3 bilder_holen.py fichte buche         # nur diese IDs
    python3 bilder_holen.py --details            # zusätzlich alle Detailansichten
    python3 bilder_holen.py --ansicht=rinde,blatt   # nur diese Ansichten
    python3 bilder_holen.py --neu                # vorhandene Bilder ersetzen (außer geprueft=ja)
    python3 bilder_holen.py --zeigen buche       # nur die besten Kandidaten nummeriert auflisten, nichts laden
    python3 bilder_holen.py --zeigen --breit buche   # mehr Kandidaten (auch Fotos ohne "Baum" im Titel)
    python3 bilder_holen.py --wahl buche 3       # Kandidat Nr. 3 aus --zeigen übernehmen (mit --breit, falls dort genutzt)
    python3 bilder_holen.py --wahl buche "File:Fagus sylvatica 01.jpg"   # bestimmte Commons-Datei (auch URL)
    (--ansicht=rinde usw. wählt bei --zeigen/--wahl die Detailansicht)

WIE GESUCHT WIRD
  Commons sortiert Pflanzenfotos in Unterkategorien nach Pflanzenteil, z. B. "Fagus sylvatica (standalone)",
  "Fagus sylvatica (bark)", "Fagus sylvatica (leaves)", "Fagus sylvatica (fruit)". Das Skript nimmt die Bilder
  aus genau diesen Kategorien. Nur wenn es keine gibt, wird frei gesucht (dann mit strengen Filtern).
  Bevorzugt werden: Quality/Featured/Valued Images, Querformat (Hauptbild), hohe Auflösung.
  Ausgeschlossen: Herbarbelege, Zeichnungen, Karten, Briefmarken, Holz/Querschnitte, Bonsai, tote Bäume, Sorten …

WICHTIG
  * Übernommen werden CC0, Public Domain, CC BY, CC BY-SA sowie CC BY-NC / BY-NC-SA (Lehrzweck, nicht kommerziell).
    Keine ND-Lizenzen: Das Zuschneiden ist bereits eine Bearbeitung. Bei gleich guten Bildern gewinnt die freiere Lizenz.
    Mit NC-Bildern darf das Spielmaterial nicht verkauft werden.
  * CC-Lizenzen verlangen die Namensnennung – sie steht auf der Kartenrückseite und in 13_Bildquellen.pdf.
  * PRÜFE JEDES BILD AUGENSCHEINLICH und setze dann in quellen.csv "geprueft" auf "ja" – solche Bilder
    werden auch mit --neu nicht mehr ersetzt. Ein besseres Bild findet man schnell mit --zeigen <id>.
Nur Standardbibliothek.
"""
import csv, json, os, re, sys, time, urllib.parse, urllib.request, html

BASE = os.path.dirname(os.path.abspath(__file__))
BILD = os.path.join(BASE, "bilder")
DETAIL = os.path.join(BILD, "details")
API = "https://commons.wikimedia.org/w/api.php"
UA = "Wald2080-Bildsuche/0.5 (Lehrmaterial für https://github.com/erklaerpierre/wald2080; pierre@pierresmits.de)" # eigene Kontaktadresse eintragen!

ERLAUBT = re.compile(r"^(cc0|public domain|pd|cc[ -]by([ -]nc)?([ -]sa)?([ -]\d(\.\d)?)?)", re.I)
# ND verboten: schon das Zuschneiden aufs Kartenformat ist eine Bearbeitung
VERBOTEN = re.compile(r"((?<![a-z])nd(?![a-z])|noderiv|fair use|gfdl only)", re.I)
NC = re.compile(r"(?<![a-z])nc(?![a-z])|non-?commercial", re.I)

# Ansicht: (Bezeichnung, Commons-Kategoriezusätze in Vorzugsreihenfolge, Suchwörter für die freie Suche)
ANSICHTEN = {
    "baum":   ("ganzer Baum", ["standalone", "habitus", "habit", "solitary trees", "trees", "tree", "famous"], ["tree", "habitus"]),
    "rinde":  ("Rinde", ["bark", "trunks", "trunk"], ["bark"]),
    "blatt":  ("Blätter/Nadeln", ["leaves", "leaf", "needles", "foliage", "shoots"], ["leaves"]),
    "frucht": ("Früchte/Samen/Zapfen", ["fruit", "fruits", "cones", "cone", "seeds", "nuts", "acorns", "berries", "strobili"], ["fruit"]),
    "bluete": ("Blüten", ["flowers", "flower", "inflorescences", "catkins", "strobili", "blossoms"], ["flowers"]),
}
# Wörter, an denen man die Ansicht im Dateinamen erkennt (für die freie Suche und als Gegenprobe)
WORTE = {
    "baum":   r"\bhabit(us)?\b|standalone|solitary|single tree|einzelbaum|solitär|freistehend|wuchsform|"
              r"\btree\b|\bbaum\b|\barbre\b|árbol|drzewo|\bboom\b",
    "rinde":  r"\bbark|rinde|borke|corteza|écorce|schors|\btrunk|stamm\b",
    "blatt":  r"\bleaf|leaves|blatt\b|blätter|foliage|needles?|nadeln?\b|feuilles?|\bhojas?\b",
    "frucht": r"\bfruits?\b|frucht|früchte|\bcones?\b|zapfen|\bseeds?\b|samen\b|\bnuts?\b|nüsse|acorns?|eicheln?\b|berr(y|ies)|beeren?\b|cupules?",
    "bluete": r"flowers?|blüten?\b|\bbloom|blossom|inflorescence|catkins?|kätzchen|fleurs?\b|\bflor(es)?\b",
}
NIE = re.compile(r"herbari|illustrat|drawing|zeichnung|distribution|range map|\bmaps?\b|karte|stamp|briefmarke|bonsai|"
                 r"\bwood\b|\(wood\)|\bholz|timber|lumber|cross.?section|querschnitt|xylothe|specimen|\bmhnt\b|"
                 r"\(dead\)|dead tree|totholz|seedling|keimling|sapling|low quality|incidental|"
                 r"in art|painting|gemälde|books|historical|postcard|museum|plate|tafel|"
                 r"diseases|disorders|galls?\b|insects?|larva|caterpillar|fungi|fungus|beetle|käfer|"
                 r"christmas|weihnacht|schild\b|denkmalschild|\bsigns?\b|plaque|tafel|"
                 r"cultivars?|\bcv\.|'[a-z][\w ]{2,25}'|bud(s)?\b|knospen?|roots?\b|wurzel", re.I)
GUETE = [(re.compile(r"featured pictures", re.I), 5), (re.compile(r"quality images", re.I), 4), (re.compile(r"valued images", re.I), 2)]
# Kategorien, die auf einen frei stehenden Einzelbaum hindeuten
EINZELBAUM = re.compile(r"individual trees|solitary trees|natural monuments|naturdenkm|famous|notable trees|veteran trees|"
                        r"old trees|monumental trees|champion trees|\(standalone\)|\(habitus\)", re.I)

# Wo der Commons-Kategoriename vom lateinischen Namen in data.py abweicht
COMMONS_NAME = {
    "hybridlaerche": "Larix × marschlinsii",
    "hybridpappel": "Populus × canadensis",
    "hybridaspe": "Populus × wettsteinii",
    "hybridnuss": "Juglans × intermedia",
    "spirke": "Pinus uncinata",
}


def commons_name(sp):
    if sp["id"] in COMMONS_NAME: return COMMONS_NAME[sp["id"]]
    latein = re.sub(r"\s*\(.*\)", "", sp["latin"])                    # "Fraxinus excelsior (selektiert)"
    return re.sub(r"\s+(u\. ?a\.|s\. ?l\.|agg\.)$", "", latein).replace("ssp.", "subsp.").strip()


def lizenz_ok(kurz):
    kurz = (kurz or "").strip()
    return bool(kurz) and bool(ERLAUBT.match(kurz)) and not VERBOTEN.search(kurz)


def text(v):
    return html.unescape(re.sub(r"<[^>]+>", "", v or "")).strip()


def api(params):
    url = API + "?" + urllib.parse.urlencode({"format": "json", "formatversion": 2, **params})
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for versuch in range(3):
        try:
            return json.load(urllib.request.urlopen(req, timeout=30))
        except urllib.error.HTTPError as e:
            if e.code not in (429, 503) or versuch == 2: raise
            time.sleep(10 * (versuch + 1))


BILDINFO = {"prop": "imageinfo|categories", "iiprop": "url|size|mime|extmetadata", "iiurlwidth": 1920,
            "iiextmetadatafilter": "LicenseShortName|Artist", "cllimit": "max"}


def unterkategorien(latein):
    """{ansicht: [(rang, Kategorie), ...]} – Unterkategorien der Art nach Pflanzenteil."""
    d = api({"action": "query", "list": "categorymembers", "cmtitle": "Category:" + latein, "cmtype": "subcat", "cmlimit": 500})
    out = {}
    for m in d.get("query", {}).get("categorymembers", []):
        rest = m["title"].split(":", 1)[1]
        if latein.lower() not in rest.lower(): continue
        rest = re.sub(re.escape(latein), " ", rest, flags=re.I)
        rest = re.sub(r"[()\-–,]|\bof\b", " ", rest).strip().lower()
        rest = re.sub(r"\s+", " ", rest)
        for a, (_, teile, _) in ANSICHTEN.items():
            if rest in teile:
                out.setdefault(a, []).append((teile.index(rest), m["title"]))
    return out


def dateien_aus(kategorie, tiefe=0):
    """Dateien einer Kategorie; mit tiefe=1 auch aus (bis zu 8) Unterkategorien, z. B. einzelnen benannten Bäumen."""
    d = api({"action": "query", "generator": "categorymembers", "gcmtitle": kategorie, "gcmtype": "file", "gcmlimit": 50, **BILDINFO})
    pages = d.get("query", {}).get("pages", [])
    if tiefe:
        u = api({"action": "query", "list": "categorymembers", "cmtitle": kategorie, "cmtype": "subcat", "cmlimit": 8})
        for m in u.get("query", {}).get("categorymembers", []):
            if not NIE.search(m["title"]): pages += dateien_aus(m["title"], tiefe - 1)
    return pages


def dateien_gesucht(latein, wort):
    d = api({"action": "query", "generator": "search", "gsrsearch": f'"{latein}" {wort} filetype:bitmap',
             "gsrnamespace": 6, "gsrlimit": 30, **BILDINFO})
    return d.get("query", {}).get("pages", [])


def hole(url, params):
    req = urllib.request.Request(url + "?" + urllib.parse.urlencode({"format": "json", **params}), headers={"User-Agent": UA})
    return json.load(urllib.request.urlopen(req, timeout=30))


def dateiinfo(titel):
    """Commons-Bildinfos zu einer Liste von Dateititeln."""
    pages = []
    for i in range(0, len(titel), 40):
        pages += api({"action": "query", "titles": "|".join(titel[i:i + 40]), **BILDINFO}).get("query", {}).get("pages", [])
    return pages


def taxon(latein):
    """Wikidata + Wikipedia zur Art: {"p18": [Dateien], "wiki": [(Datei, Bildunterschrift), ...]}.
    P18 ist das Bild, das die Wikidata-Gemeinschaft gewählt hat. Die Bildunterschriften in den Artikeln
    (z. B. "Habitus einer freistehenden Fichte", "Rinde", "Zapfen") zeigen sehr zuverlässig, was zu sehen ist."""
    out = {"p18": [], "wiki": []}
    wd = "https://www.wikidata.org/w/api.php"
    treffer = hole(wd, {"action": "query", "list": "search", "srsearch": f'haswbstatement:"P225={latein}"', "srlimit": 1})
    treffer = treffer.get("query", {}).get("search", [])
    if not treffer: return out
    e = hole(wd, {"action": "wbgetentities", "ids": treffer[0]["title"], "props": "claims|sitelinks"})["entities"][treffer[0]["title"]]
    out["p18"] = ["File:" + c["mainsnak"]["datavalue"]["value"] for c in e.get("claims", {}).get("P18", []) if c["mainsnak"].get("datavalue")]
    for sprache in ("de", "en"):
        artikel = e.get("sitelinks", {}).get(sprache + "wiki", {}).get("title")
        if not artikel: continue
        h = hole(f"https://{sprache}.wikipedia.org/w/api.php", {"action": "parse", "page": artikel, "prop": "text", "formatversion": 2})
        h = h.get("parse", {}).get("text", "")
        stuecke = re.split(r'href="/wiki/(?:Datei|File|Bild|Image):([^"#?]+)"', h)
        for datei, danach in zip(stuecke[1::2], stuecke[2::2]):
            m = re.search(r'<figcaption>(.*?)</figcaption>|class="gallerytext"[^>]*>(.*?)</div>', danach[:2000], re.S)
            if m:
                out["wiki"].append(("File:" + urllib.parse.unquote(datei).replace("_", " "), text(m.group(1) or m.group(2))[:200]))
    return out


def bewerte(p, ansicht, latein, art_sicher, fremd, beleg=False):
    """Punkte für eine Datei (None = ungeeignet). art_sicher = stammt aus einer Kategorie/Wikidata der Art,
    fremd = Kategorien der Art für ANDERE Ansichten, beleg = Quelle zeigt sicher die gewünschte Ansicht."""
    ii = (p.get("imageinfo") or [None])[0]
    if not ii or ii.get("mime") != "image/jpeg": return None
    md = ii.get("extmetadata", {})
    lic = text(md.get("LicenseShortName", {}).get("value"))
    if not lizenz_ok(lic): return None
    w, h = ii.get("width", 0), ii.get("height", 0)
    if max(w, h) < 1200 or min(w, h) < 800: return None
    titel = p.get("title", "")
    kats = [c["title"] for c in p.get("categories", [])]
    alles = titel + " | " + " | ".join(kats)
    if NIE.search(alles): return None
    if not art_sicher and latein.lower() not in titel.lower(): return None      # freie Suche: Art muss im Titel stehen
    if any(k in fremd for k in kats): return None                               # z. B. Baumbild, das auch unter (leaves) steht
    andere = [a for a in WORTE if a != ansicht and re.search(WORTE[a], titel, re.I)]
    eigene = re.search(WORTE[ansicht], titel, re.I)
    if ansicht == "baum" and andere: return None                                # Nahaufnahme eines Pflanzenteils
    if andere and not eigene and not art_sicher: return None
    punkte = (3 if eigene else 0) - (3 if andere and not eigene else 0)
    punkte += max([pt for rx, pt in GUETE if any(rx.search(k) for k in kats)] or [0])
    seiten = w / h
    if ansicht == "baum":
        einzel = any(EINZELBAUM.search(k) for k in kats)
        if not (beleg or eigene or einzel): return None                          # sonst oft Landschafts- oder Wanderfotos
        punkte += 3 if 1.2 <= seiten <= 1.8 else (1 if seiten > 1.8 else -2)            # Kartenfeld ist Querformat 1,4 : 1
        punkte += 4 if einzel else 0
        if re.search(r"forests?\b|wald\b|forêt|bosque|\blas\b|stand\b|bestand|avenues?|allee|\balong\b|\btrees\b|bäume",
                     alles, re.I): punkte -= 3                                         # Bestand/Allee statt Einzelbaum
        if re.search(r"winter|snow|schnee", alles, re.I): punkte -= 3                    # unbelaubt -> schlecht vergleichbar
    else:
        punkte += 1 if seiten >= 1 else 0
    punkte += 1 if max(w, h) >= 2400 else 0
    punkte -= 1 if NC.search(lic) else 0                                         # NC nur, wenn deutlich besser
    return dict(punkte=punkte, titel=titel, url=ii.get("thumburl") or ii["url"], seite=ii.get("descriptionurl", ""),
                urheber=text(md.get("Artist", {}).get("value")) or "unbekannt", lizenz=lic, groesse=f"{w}x{h}")


def kandidaten(latein, ansicht, ukats, tx, breit=False):
    """Bewertete Bildvorschläge, bester zuerst. breit: für den ganzen Baum auch Fotos ohne Hinweis im Titel
    (zum Aussuchen per Auge mit --zeigen / --wahl)."""
    fremd = {k for a, lst in ukats.items() if a != ansicht for _, k in lst}
    gesehen, out = set(), []
    def nimm(pages, quelle, art_sicher=True, beleg=False):
        for p in pages:
            if p.get("title") in gesehen: continue
            gesehen.add(p.get("title"))
            b = bewerte(p, ansicht, latein, art_sicher, fremd, beleg)
            if b: b["punkte"] += quelle; out.append(b)
    baum = ansicht == "baum"
    # Bildunterschrift im Wikipedia-Artikel nennt genau diese Ansicht (und keine andere)
    passend = [d for d, u in tx["wiki"] if re.search(WORTE[ansicht], u, re.I)
               and not any(re.search(WORTE[a], u, re.I) for a in WORTE if a != ansicht)]
    if passend: nimm(dateiinfo(passend), 7, beleg=True)
    for rang, kat in sorted(ukats.get(ansicht, [])):
        nimm(dateien_aus(kat, tiefe=1 if baum else 0), 6 - rang, beleg=True)
    if baum:
        if tx["p18"]: nimm(dateiinfo(tx["p18"]), 3)      # kein Beleg: manchmal ist es eine Zapfen- oder Blattaufnahme
        nimm(dateien_aus("Category:" + latein, tiefe=1 if breit else 0), 0, beleg=breit)
    if baum or not out:
        for wort in ANSICHTEN[ansicht][2]: nimm(dateien_gesucht(latein, wort), 0, art_sicher=False)
    out.sort(key=lambda b: b["punkte"], reverse=True)
    return out


def lade(url, ziel):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for versuch in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                daten = r.read()
            break
        except urllib.error.HTTPError as e:
            if e.code not in (429, 503) or versuch == 3: raise
            warte = int(e.headers.get("Retry-After") or 0) or 30 * 2 ** versuch
            print(f"  … Wikimedia bremst (HTTP {e.code}), warte {warte} s"); time.sleep(warte)
    with open(ziel, "wb") as f:
        f.write(daten)


def lese_quellen(fn):
    if not os.path.exists(fn): return {}
    with open(fn, encoding="utf-8-sig") as f:
        return {r["id"]: r for r in csv.DictReader(f, delimiter=";")}


def schreibe_quellen(fn, q, felder):
    with open(fn, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=felder, delimiter=";", extrasaction="ignore")
        w.writeheader()
        for k in q: w.writerow(q[k])


FELDER = ["id", "name", "latein", "datei", "urheber", "lizenz", "quelle_url", "bildtitel", "geprueft"]
FELDER_DETAIL = ["id", "art", "ansicht", "name", "latein", "datei", "urheber", "lizenz", "quelle_url", "bildtitel", "geprueft"]


def direkt(titel):
    """Eine bestimmte Commons-Datei (Titel oder URL der Dateiseite) – nur Lizenz und Format werden geprüft."""
    titel = urllib.parse.unquote(titel.rsplit("/wiki/", 1)[-1]).replace("_", " ")
    if not titel.startswith("File:"): titel = "File:" + titel.split(":", 1)[-1]
    for p in dateiinfo([titel]):
        ii = (p.get("imageinfo") or [None])[0]
        if not ii: break
        md = ii.get("extmetadata", {})
        lic = text(md.get("LicenseShortName", {}).get("value"))
        if not lizenz_ok(lic):
            print(f"Lizenz nicht erlaubt: {lic or 'unbekannt'}"); return None
        return dict(punkte=0, titel=p["title"], url=ii.get("thumburl") or ii["url"], seite=ii.get("descriptionurl", ""),
                    urheber=text(md.get("Artist", {}).get("value")) or "unbekannt", lizenz=lic,
                    groesse=f'{ii.get("width")}x{ii.get("height")}')
    print(f"Datei nicht gefunden: {titel}"); return None


def main(argv):
    sys.path.insert(0, BASE)
    from data import SPECIES_LIST
    neu, zeigen, breit = "--neu" in argv, "--zeigen" in argv, "--breit" in argv
    wahl = None
    if "--wahl" in argv:                                    # --wahl <id> <nr | Datei>
        i = argv.index("--wahl")
        wahl, argv = argv[i + 2], argv[:i] + [argv[i + 1]] + argv[i + 3:]
        neu = True
    ansichten = ["baum"] + (list(ANSICHTEN)[1:] if "--details" in argv else [])
    for a in argv:
        if a.startswith("--ansicht="): ansichten = [x for x in a.split("=", 1)[1].split(",") if x in ANSICHTEN]
    ids = [a for a in argv if not a.startswith("--")]
    os.makedirs(BILD, exist_ok=True)
    qfn, dfn = os.path.join(BILD, "quellen.csv"), os.path.join(DETAIL, "quellen.csv")
    q, qd = lese_quellen(qfn), lese_quellen(dfn)
    if set(ansichten) - {"baum"}: os.makedirs(DETAIL, exist_ok=True)

    for sp in SPECIES_LIST:
        if ids and sp["id"] not in ids: continue
        latein = commons_name(sp)
        try:
            ukats = unterkategorien(latein)
        except Exception as e:
            print(f'{sp["id"]:16} FEHLER {e}'); continue
        try:
            tx = taxon(latein)
        except Exception as e:
            print(f'{sp["id"]:16} Wikidata/Wikipedia nicht erreichbar ({e}) – nur Commons'); tx = {"p18": [], "wiki": []}
        for a in ansichten:
            haupt = a == "baum"
            schluessel = sp["id"] if haupt else f'{sp["id"]}_{a}'
            datei = schluessel + ".jpg"
            ziel = os.path.join(BILD if haupt else DETAIL, datei)
            alt = (q if haupt else qd).get(schluessel, {})
            if not zeigen and not wahl and os.path.exists(ziel) and (not neu or alt.get("geprueft") == "ja"):
                continue
            if wahl and not wahl.isdigit():
                ks = [t for t in [direkt(wahl)] if t]
            else:
                try:
                    ks = kandidaten(latein, a, ukats, tx, breit)
                except Exception as e:
                    print(f'{sp["id"]:16} {a:7} FEHLER {e}'); continue
            if zeigen:
                print(f'\n{sp["name"]} ({latein}) – {ANSICHTEN[a][0]}')
                for n, k in enumerate(ks[:12], 1):
                    print(f'  {n:2}. {k["punkte"]:3}  {k["lizenz"]:13} {k["groesse"]:>10}  {k["seite"]}')
                if not ks: print("  (nichts Passendes – mit --breit mehr Kandidaten)")
                continue
            if wahl and wahl.isdigit():
                ks = ks[int(wahl) - 1:int(wahl)]
            if not ks:
                print(f'{sp["id"]:16} {a:7} kein passendes freies Bild – bitte manuell suchen'
                      + ("  (altes Bild bleibt liegen)" if os.path.exists(ziel) else "")); continue
            t = ks[0]
            try:
                lade(t["url"], ziel)
            except Exception as e:
                print(f'{sp["id"]:16} {a:7} FEHLER beim Laden {e}'); continue
            zeile = dict(id=schluessel, art=sp["id"], ansicht=a, name=sp["name"], latein=sp["latin"], datei=datei,
                         urheber=t["urheber"], lizenz=t["lizenz"], quelle_url=t["seite"], bildtitel=t["titel"], geprueft="nein")
            if haupt:
                q[schluessel] = zeile; schreibe_quellen(qfn, q, FELDER)
            else:
                qd[schluessel] = zeile; schreibe_quellen(dfn, qd, FELDER_DETAIL)
            print(f'{sp["id"]:16} {a:7} ok  {t["lizenz"]:13} {t["titel"][5:65]}')
            time.sleep(3.0)                                 # Wikimedia drosselt viele Downloads in Folge
    if not zeigen:
        print("Fertig. Bitte alle Bilder ansehen und in quellen.csv 'geprueft' auf 'ja' setzen.")


if __name__ == "__main__":
    main(sys.argv[1:])

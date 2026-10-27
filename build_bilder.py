# -*- coding: utf-8 -*-
"""Erzeugt bilder/quellen.csv (Vorlage, falls nicht vorhanden) und out/13_Bildquellen.pdf (Bildnachweis)."""
import os, sys, csv, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import *
from build_docs import *
import cardart

BILD = cardart.BILD_DIR
FELDER = ["id", "name", "latein", "datei", "urheber", "lizenz", "quelle_url", "bildtitel", "geprueft"]


def vorlage():
    fn = os.path.join(BILD, "quellen.csv")
    if os.path.exists(fn):
        return
    os.makedirs(BILD, exist_ok=True)
    with open(fn, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";"); w.writerow(FELDER)
        for s in SPECIES_LIST:
            w.writerow([s["id"], s["name"], s["latin"], "", "", "", "", "", ""])


def bildnachweis():
    vorlage()
    q = cardart.quellen()
    fn = f"{OUT}/13_Bildquellen.pdf"
    doc = BaseDocTemplate(fn, pagesize=landscape(A4), leftMargin=10 * mm, rightMargin=10 * mm, topMargin=12 * mm, bottomMargin=12 * mm,
                          title="Wald 2080 – Bildquellen")
    def foot(c, d):
        c.saveState(); c.setFont("DVC", 7); c.setFillColor(hc("#90A4AE"))
        c.drawString(10 * mm, 6 * mm, "Wald 2080 · Bildquellen und Lizenzen")
        c.drawRightString(287 * mm, 6 * mm, f"Seite {d.page}"); c.restoreState()
    doc.addPageTemplates([PageTemplate(id="p", frames=[Frame(10 * mm, 12 * mm, 277 * mm, 186 * mm, id="f", leftPadding=0, rightPadding=0,
                                                              topPadding=0, bottomPadding=0)], onPage=foot)])
    S = [P("Bildquellen und Lizenzen", H1),
         P("Auf der Rückseite jeder Baumkarte steht ein frei lizenziertes Foto. Verwendet werden nur Bilder unter CC0, Public Domain, CC BY oder CC BY-SA. "
           "Bei CC BY / CC BY-SA ist die Namensnennung Pflicht (steht klein auf der Karte; hier die vollständige Angabe). "
           "Bilder legt man als <b>bilder/&lt;id&gt;.jpg</b> ab und trägt sie in <b>bilder/quellen.csv</b> ein – oder lädt sie mit <b>bilder_holen.py</b> automatisch.", SUB)]
    rows = [["ID", "Baumart", "Foto", "Urheber / Rechteinhaber", "Lizenz", "Quelle (Seite des Bildes)", "geprüft", "Suche"]]
    n_ok = 0
    for s in SPECIES_LIST:
        r = q.get(s["id"], {})
        has = cardart.bild_pfad(s["id"]) is not None
        n_ok += has
        suche = "commons.wikimedia.org/w/index.php?search=" + urllib.parse.quote(s["latin"]) + "&ns6=1"
        rows.append([s["id"], f'<b>{s["name"]}</b><br/><font size="6" color="#78909C"><i>{s["latin"]}</i></font>',
                     "vorhanden" if has else "fehlt noch", r.get("urheber", "") or "–", r.get("lizenz", "") or "–",
                     (r.get("quelle_url", "") or "–")[:70], r.get("geprueft", "") or "–", f'<font size="5.5">{suche}</font>'])
    S += [P(f"Stand: {n_ok} von {len(SPECIES_LIST)} Baumarten mit Foto.", H2)]
    S += [tbl(rows, [24, 42, 17, 48, 22, 55, 13, 56], font=ParagraphStyle("c5", parent=CELL, fontSize=6.6, leading=8))]
    S += [Spacer(1, 4), P("Die Spalte „Suche“ ist nur ein Suchlink auf Wikimedia Commons (kein geprüftes Bild). Lizenz und Urheber immer auf der Bildseite kontrollieren. "
                          "Fotos von Personen oder erkennbaren Privatgrundstücken vermeiden.", SMALL)]
    doc.build(S)
    return n_ok


if __name__ == "__main__":
    print(bildnachweis(), "Bilder vorhanden")

# -*- coding: utf-8 -*-
"""Je Region/Bundesland eine Edition: Steckbrief + Standortkarten als eigenes PDF (Ordner out/Editionen/)."""
import os, re, sys, io, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
from data import *
import sim, balancing
from build_docs import P, B, H1, H2, SUB, SMALL, CELL, tbl, box, BOXS, GREEN
from build_cards import standort_card, MW, MH
from cardart import tile_map, LAND_COL
from reportlab.platypus import SimpleDocTemplate, Spacer, Flowable, Table, TableStyle, Paragraph
from reportlab.lib.styles import ParagraphStyle
from pypdf import PdfWriter, PdfReader

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out", "Editionen")
os.makedirs(OUT, exist_ok=True)
TR = {"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss", "Ä": "Ae", "Ö": "Oe", "Ü": "Ue"}


def slug(t):
    for a, b in TR.items(): t = t.replace(a, b)
    return re.sub(r"[^A-Za-z0-9]+", "-", t).strip("-")


class Kachel(Flowable):
    def __init__(self, code, tile=4.2):
        super().__init__(); self.code, self.tile = code, tile
        self.width, self.height = 6 * tile * mm, 9 * tile * mm
    def draw(self):
        c = self.canv; t = self.tile
        for r in REGION_LISTE:
            cx, cy = r["kachel"]
            on = r["code"] == self.code
            c.setFillColor(hc(r["farbe"]) if on else hc("#E0E4E7"))
            c.roundRect(cx * t * mm, (8 - cy) * t * mm, (t - 0.4) * mm, (t - 0.4) * mm, 0.8 * mm, stroke=0, fill=1)
            if on:
                c.setFillColor(hc("#FFFFFF")); c.setFont("DVCB", 5.5)
                c.drawCentredString((cx * t + (t - 0.4) / 2) * mm, ((8 - cy) * t + 1.3) * mm, r["code"])


def zuschlag_text(z):
    if not z: return "keiner"
    return ", ".join(f'{RES_NAMES[k].split("/")[0]} {v:+d}'.replace("-", "−") for k, v in z.items())


def steckbrief(r, bal, fn):
    doc = SimpleDocTemplate(fn, pagesize=A4, leftMargin=16 * mm, rightMargin=16 * mm, topMargin=14 * mm, bottomMargin=14 * mm,
                            title=f"Wald 2080 – Edition {r['name']}")
    sts = [s for s in STANDORTE if s["reg"] == r["code"]]
    S = []
    head = Table([[[P(f"Edition {r['name']}", H1),
                    P(f"{LAENDER[r['land']]} · Kürzel {r['code']} · {len(sts)} Standorte · {len(r['arten'])} typische Baumarten", SUB)],
                   Kachel(r["code"])]], colWidths=[140 * mm, 38 * mm])
    head.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))
    S += [head]
    S += [box([P(f"<b>{r['hinweis']}</b>", BOXS)], "#E8F5E9", "#A5D6A7", w=178)]
    S += [Spacer(1, 4), P("Spielwerte dieser Edition", H2)]
    S += [tbl([["Regionaler Gefahrenzuschlag", "Gewinnquote „solide“ (Simulation)", "passives Team"],
               [zuschlag_text(r["zuschlag"]),
                f'Kurz {bal["kurz"]} % · Standard {bal["standard"]} % · Lang {bal["lang"]} %', f'{bal["passiv"]} % (Standard)']],
              [56, 84, 38])]
    S += [P("Der Zuschlag erhöht (+) bzw. senkt (−) die Stärke aller Ereignisse der genannten Art in dieser Edition. Er ist die Stellschraube, "
            "mit der die Editionen auf eine vergleichbare Schwierigkeit kalibriert wurden.", SMALL)]
    S += [P("Standorte", H2)]
    rows = [["Nr.", "Standort", "Landschaft", "W", "N", "T", "Besonderheit", "Start", "E bei Klima 0/1/2/3", "Beschreibung"]]
    for s in sts:
        sp = SPECIES[s["start"]]
        rows.append([s["id"], f'<b>{s["name"]}</b>', s["land"], s["W"], s["N"], s["T"],
                     ", ".join(f'{RES_NAMES[k].split("/")[0]} {v:+d}'.replace("-", "−") for k, v in s["mods"].items()) or "–",
                     sp["name"], " / ".join(str(sim.eignung(sp, s, k)) for k in range(4)), s["text"]])
    S += [tbl(rows, [11, 29, 24, 5.5, 5.5, 5.5, 18, 17, 14, 48], font=ParagraphStyle("c", parent=CELL, fontSize=6.6, leading=7.8))]
    S += [P("Typische Baumarten dieser Edition", H2)]
    for deck in ("basis", "nachbar", "europa"):
        names = [SPECIES[a]["name"] for a in r["arten"] if SPECIES[a]["deck"] == deck]
        if names:
            S.append(P(f'<b>{DECKS[deck][0]}:</b> ' + ", ".join(sorted(names)), SMALL))
    S += [Spacer(1, 3), P("Alle weiteren Karten aus den Erweiterungsdecks (Saatgutbörse) sind zusätzlich spielbar. "
                           "Hinweis: Die Baumarten-Zuordnung ist eine didaktische Vereinfachung und ersetzt keine Standortkartierung.", SMALL)]
    doc.build(S)


def baue(r, bal):
    base = f'{r["land"]}_{r["code"]}_{slug(r["name"])}'
    tmp1, tmp2 = (os.path.join(tempfile.gettempdir(), f"_{base}_{k}.pdf") for k in "ab")
    steckbrief(r, bal, tmp1)
    sts = [s for s in STANDORTE if s["reg"] == r["code"]]
    card_sheet(tmp2, [standort_card(s) for s in sts], MW, MH, 4, 4, title=f"Standortkarten {r['name']}",
               footer=f'Wald 2080 · Edition {r["name"]} · Standortkarten · mit Anschnitt, an den Marken schneiden')
    w = PdfWriter()
    for f in (tmp1, tmp2):
        for p in PdfReader(f).pages: w.add_page(p)
    w.add_metadata({"/Title": f"Wald 2080 – Edition {r['name']}"})
    out = f"{OUT}/{base}.pdf"
    with open(out, "wb") as fh: w.write(fh)
    os.remove(tmp1); os.remove(tmp2)
    return out


if __name__ == "__main__":
    bal = balancing.lade()
    for r in REGION_LISTE:
        baue(r, bal[r["code"]])
    print(len(REGION_LISTE), "Editionen geschrieben")

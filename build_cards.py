# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
from data import *
import sim
from cardart import *
from data import REGIONEN, REGION_LISTE, REGION_ORDER, LAENDER

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)
CW, CH = 63, 88          # Pokerformat
MW, MH = 45, 63          # Mini-Format (Standortkarten)
EIG_TXT = {"PIO": "Pionier", "SCH": "Schattenbaum", "BOD": "Bodenverbesserer", "INV": "⚠ Invasiv"}
EIG_COL = {"PIO": "#F9A825", "SCH": "#455A64", "BOD": "#6D4C41", "INV": "#C62828"}


def cell_bar(cd, x, y, rng, color, label, cw=7.4, ch=3.6):
    cd.text(3, y + 2.7, label, "DVCB", 6.2, C_DARK)
    for v in range(1, 6):
        inside = rng[0] <= v <= rng[1]
        cd.rect(x + (v - 1) * (cw + 0.3), y, cw, ch, fill=color if inside else "#FFFFFF",
                stroke=color if inside else C_GREY, lw=0.35, r=0.6)
        cd.text(x + (v - 1) * (cw + 0.3) + cw / 2, y + 2.7, str(v), "DVCB", 5.6,
                "#FFFFFF" if inside else C_GREY, "c")


def dots(cd, x, y, n, r=1.05, color="#2E7D32"):
    for i in range(5):
        cd.circle(x + i * 3.0, y, r, fill=color if i < n else None, stroke=color if i >= n else None, lw=0.4) \
            if i >= n else cd.circle(x + i * 3.0, y, r, fill=color)


FR = 1.8          # Breite des farbigen Rahmens (innerhalb der Schnittkante)
PANEL_R = 1.6


def panel(cd, w, h, top, bottom=None, fill="#FFFFFF"):
    """Weißes Innenfeld mit Rahmen aus Kartenfarbe (Farbe läuft im Anschnitt weiter -> kein weißer Rand)."""
    cd.rect(FR, top, w - 2 * FR, (bottom or h - FR) - top, fill=fill, r=PANEL_R)


def tree_card(sp):
    def draw(cd):
        col = C_DECK[sp["deck"]]
        cd.bg(col)
        panel(cd, CW, CH, 15.5)
        size = fit_font(sp["name"], "DVB", 10.5, CW - 6 - 12, 6.5)
        cd.text(3.5, 7.2, sp["name"], "DVB", size, "#FFFFFF")
        lsz = fit_font(sp["latin"], "DVCI", 6.4, CW - 6 - 12, 5)
        cd.text(3.5, 12.0, sp["latin"], "DVCI", lsz, "#E8F5E9")
        cd.circle(CW - 7.2, 7.8, 4.6, fill="#FFD54F", stroke="#F9A825", lw=0.6)
        cd.text(CW - 7.2, 8.9, str(sp["cost"]), "DVB", 10, C_DARK, "c")
        cd.text(CW - 7.2, 11.4, "T€", "DVCB", 4.4, C_DARK, "c")
        # Unterzeile
        cd.rect(FR, 15.5, CW - 2 * FR, 5, fill=C_LGREY)
        cd.text(3.5, 19.2, f'{sp["grp"]} · {sp["kat"]}', "DVCB", 6, C_DARK)
        n = len(sp["regionen"])
        if n:
            cd.text(CW - 3.5, 19.0, f'typisch in {n} Region{"en" if n != 1 else ""}', "DVC", 5.2, "#546E7A", "r")
        cd.text(3.5, 24.3, "STANDORTANSPRUCH", "DVCB", 5.4, "#78909C")
        cell_bar(cd, 19, 25.6, sp["W"], C_WASSER, "Wasser")
        cell_bar(cd, 19, 30.4, sp["N"], C_NAEHR, "Nährst.")
        cell_bar(cd, 19, 35.2, sp["T"], C_WAERME, "Wärme")
        cd.text(3.5, 43.5, "WIDERSTANDSKRAFT  (höher = robuster)", "DVCB", 5.4, "#78909C")
        y = 46.9
        for k in RES_KEYS:
            cd.text(3.5, y, RES_NAMES[k], "DVC", 6, C_DARK)
            for i in range(5):
                if i < sp["res"][k]:
                    cd.circle(30 + i * 3.4, y - 0.9, 1.15, fill="#2E7D32")
                else:
                    cd.circle(30 + i * 3.4, y - 0.9, 1.15, stroke=C_GREY, lw=0.4)
            cd.text(CW - 3.5, y, str(sp["res"][k]), "DVCB", 6, "#2E7D32", "r")
            y += 3.2
        cd.hline(3.5, y - 1.9, CW - 3.5, "#CFD8DC")
        cd.text(3.5, y + 0.9, "Holzwert", "DVCB", 6, C_DARK)
        cd.text(30, y + 1.2, "★" * sp["hw"] + "☆" * (5 - sp["hw"]), "DV", 6.3, "#F9A825")
        ex = 3.5
        chips = [(EIG_TXT[e], EIG_COL[e]) for e in sp["eig"]]
        if sp["kat"] == "Züchtung":
            chips.append(("Züchtung", "#00897B"))
        for t, cc in chips:
            wd = pdfmetrics.stringWidth(t, "DVCB", 5.4) / mm + 3
            cd.rect(ex, y + 3.2, wd, 3.5, fill=cc, r=1)
            cd.text(ex + wd / 2, y + 5.7, t, "DVCB", 5.4, "#FFFFFF", "c")
            ex += wd + 1.2
        cd.hline(3.5, y + 7.9, CW - 3.5, "#CFD8DC")
        cd.para(3.5, y + 10.7, sp["note"], "DVCI", 6.0, "#37474F", maxw=CW - 7, lead=7.0, maxlines=3)
    return draw


def tree_back(sp):
    def draw(cd):
        col = C_DECK[sp["deck"]]
        cd.bg(col)
        panel(cd, CW, CH, FR, fill=col)
        # Foto
        has = zeichne_bild(cd, sp["id"], sp, FR, FR, CW - 2 * FR, 42.0, radius=PANEL_R)
        q = QUELLEN.get(sp["id"])
        if has and q:
            cd.rect(FR, 41.2, CW - 2 * FR, 2.6, fill=Color(0, 0, 0, alpha=0.55))
            cd.text(3.0, 43.1, f'Foto: {q.get("urheber", "")[:34]} · {q.get("lizenz", "")}', "DVC", 3.4, "#FFFFFF")
        # Name
        size = fit_font(sp["name"], "DVB", 10.5, CW - 8, 6.5)
        cd.text(CW / 2, 49.6, sp["name"], "DVB", size, "#FFFFFF", "c")
        lsz = fit_font(sp["latin"], "DVCI", 6.4, CW - 8, 5)
        cd.text(CW / 2, 53.7, sp["latin"], "DVCI", lsz, "#E8F5E9", "c")
        # Fuß: Karte + Text
        cd.rect(FR, 55.6, CW - 2 * FR, CH - FR - 55.6, fill="#FFFFFF", r=PANEL_R)
        act = set(sp["regionen"])
        tile_map(cd, 4.2, 58.3, act, tile=2.95)
        x0 = 26.5; w = CW - x0 - 3.2
        cd.text(x0, 60.6, "VERBREITUNG  (typisch)", "DVCB", 5.2, "#78909C")
        y = 64.6
        if act:
            for lnd in ("DE", "AT", "CH"):
                tot = len([r for r in REGION_LISTE if r["land"] == lnd])
                n = len([c for c in act if REGIONEN[c]["land"] == lnd])
                cd.rect(x0, y - 2.0, 2.3, 2.3, fill=LAND_COL[lnd] if n else "#E0E4E7", r=0.4)
                cd.text(x0 + 3.6, y, f'{LAENDER[lnd]}: {n} von {tot}', "DVCB" if n else "DVC", 5.8, C_DARK if n else "#90A4AE")
                y += 3.6
            codes = " · ".join(c for c in sorted(act, key=lambda c: REGION_ORDER[c]))
            if len(act) <= 20:
                cd.para(x0, y + 1.6, codes, "DVC", 5.0, "#546E7A", maxw=w, lead=5.9, maxlines=3)
            else:
                cd.text(x0, y + 1.6, f"insgesamt {len(act)} von {len(REGION_LISTE)} Regionen", "DVCI", 5.2, "#546E7A")
        else:
            cd.para(x0, y, "Nicht in D-A-CH heimisch: Herkunft außerhalb – nur als Erweiterung / Experiment.", "DVCI", 5.6, C_DARK, maxw=w, lead=6.6, maxlines=4)
        sz = fit_font(sp["kat"], "DVCI", 5.4, w, 4.2)
        cd.text(x0, CH - FR - 1.8, sp["kat"], "DVCI", sz, "#546E7A")
    return draw


def standort_card(s):
    reg = REGIONEN[s["reg"]]
    def draw(cd):
        col = reg["farbe"]
        cd.bg(col)
        panel(cd, MW, MH, 12.5)
        size = 7.0
        lines = wrap(s["name"], "DVB", size, MW - 15)
        while (len(lines) > 2 or any(pdfmetrics.stringWidth(l, "DVB", size) > (MW - 15) * mm for l in lines)) and size > 5.2:
            size -= 0.3; lines = wrap(s["name"], "DVB", size, MW - 15)
        y0 = 6.4 if len(lines) == 1 else 4.9
        for i, ln in enumerate(lines[:2]):
            cd.text(2.5, y0 + i * 3.5, ln, "DVB", size, "#FFFFFF")
        cd.rect(MW - 11.0, 1.8, 9.0, 3.6, fill="#FFFFFF", r=1)
        cd.text(MW - 6.5, 4.5, s["reg"], "DVCB", 5.6, col, "c")
        cd.text(2.5, 15.5, s["land"], "DVCI", 5.0, "#546E7A")
        y = 17.5
        for lab, val, colr in (("Wasser", s["W"], C_WASSER), ("Nährst.", s["N"], C_NAEHR), ("Wärme", s["T"], C_WAERME)):
            cd.text(2.5, y + 2.6, lab, "DVCB", 5.4, C_DARK)
            for v in range(1, 6):
                on = v <= val
                cd.rect(14 + (v - 1) * 5.8, y, 5.4, 3.3, fill=colr if on else "#FFFFFF", stroke=colr if on else C_GREY, lw=0.3, r=0.5)
            cd.text(MW - 2.8, y + 2.6, str(val), "DVCB", 6, colr, "r")
            y += 4.0
        cd.text(2.5, 31.6, "Besonderheit:", "DVCB", 5.0, "#78909C")
        mods = s["mods"]
        if not mods:
            cd.text(18, 31.6, "keine", "DVC", 5.2, "#546E7A")
        else:
            mx = 17.5
            for k, v in mods.items():
                t = f'{RES_NAMES[k].split("/")[0]} {v:+d}'.replace("-", "−")
                wd = pdfmetrics.stringWidth(t, "DVCB", 5.0) / mm + 2.4
                cd.rect(mx, 29.1, wd, 3.4, fill="#C62828" if v < 0 else "#2E7D32", r=0.9)
                cd.text(mx + wd / 2, 31.6, t, "DVCB", 5.0, "#FFFFFF", "c")
                mx += wd + 1
        cd.rect(2.8, 34, MW - 5.6, 17.4, fill="#F5F5F5", stroke="#CFD8DC", lw=0.3, r=1)
        cd.text(4.2, 37.3, "Klimastufe", "DVCB", 5.0, "#78909C")
        for k in range(4):
            cd.text(17.5 + k * 6.9, 37.3, str(k), "DVCB", 5.2, C_DARK, "c")
        sp = SPECIES[s["start"]]
        rows = [("Wasser", C_WASSER, lambda k: klima(s["W"], s["T"], k)[0]),
                ("Wärme", C_WAERME, lambda k: klima(s["W"], s["T"], k)[1])]
        yy = 41.0
        for lab, colr, f in rows:
            cd.text(4.2, yy, lab, "DVC", 5.2, colr)
            for k in range(4):
                cd.text(17.5 + k * 6.9, yy, str(f(k)), "DVCB", 5.8, colr, "c")
            yy += 3.5
        cd.text(4.2, yy, "Eignung E", "DVCB", 5.2, C_DARK)
        for k in range(4):
            e = sim.eignung(sp, s, k)
            colr = {3: "#2E7D32", 2: "#F9A825", 1: "#E65100", 0: "#C62828"}[e]
            cd.circle(17.5 + k * 6.9, yy - 1.4, 2.0, fill=colr)
            cd.text(17.5 + k * 6.9, yy - 0.4, str(e), "DVCB", 5.6, "#FFFFFF", "c")
        cd.text(2.8, 55.2, "Start:", "DVCB", 5.2, "#78909C")
        sz = fit_font(sp["name"], "DVB", 7.0, MW - 14, 5.5)
        cd.text(10.8, 55.2, sp["name"], "DVB", sz, C_DARK)
        cd.text(2.8, 59.0, "Reinbestand  ♥ ♥ ♥", "DVC", 5.8, "#C62828")
        cd.text(MW - 2.8, MH - 2.9, s["id"], "DVC", 3.8, "#B0BEC5", "r")
    return draw


def event_card(e):
    def draw(cd):
        col = C_KIND[e["kind"]]
        cd.bg(col)
        panel(cd, CW, CH, 14)
        cd.text(3.5, 5.0, KIND_NAME[e["kind"]], "DVCB", 6.2, "#FFFFFF")
        size = fit_font(e["name"], "DVB", 10.5, CW - 7 - (14 if e["kind"] in RES_KEYS else 0), 6.5)
        cd.text(3.5, 11.2, e["name"], "DVB", size, "#FFFFFF")
        if e["kind"] in RES_KEYS:
            cd.circle(CW - 8.5, 7.6, 5.6, fill="#FFFFFF")
            cd.text(CW - 8.5, 8.9, str(e["S"]), "DVB", 13, col, "c")
            cd.text(CW - 8.5, 11.7, "STÄRKE", "DVCB", 3.9, col, "c")
        y = 19
        cd.text(3.5, y, "Betroffen:", "DVCB", 6.2, col)
        y += cd.para(3.5, y + 3.4, e["filtertext"], "DVCB", 6.6, C_DARK, maxw=CW - 7, lead=8) + 3.4
        y += 2.5
        y += cd.para(3.5, y + 1.5, e["text"], "DVC", 6.8, "#37474F", maxw=CW - 7, lead=8.2) + 3.5
        if e["kind"] in RES_KEYS:
            cd.rect(3.5, y, CW - 7, 17.5, fill="#FAFAFA", stroke="#CFD8DC", lw=0.4, r=1.2)
            cd.text(5, y + 3.8, "PROBE", "DVCB", 5.6, col)
            cd.text(5, y + 8.2, f'W6 + {RES_NAMES[e["kind"]].split("/")[0]}-Wert + Eignung', "DVCB", 6.6, C_DARK)
            cd.text(5, y + 12.6, f'+ Standort − Jungwuchs  ≥  {e["S"]}', "DVCB", 6.6, C_DARK)
            y += 19.5
            if e["spread"]:
                cd.rect(3.5, y, CW - 7, 8.5, fill="#FFEBEE", stroke="#EF9A9A", lw=0.4, r=1.2)
                cd.para(5, y + 3.3, "Befallskette: Gleiche Reinbestände neben einem betroffenen Feld werden mit −1 erneut geprüft.",
                        "DVCB", 5.3, "#B71C1C", maxw=CW - 10, lead=6.2, maxlines=2)
                y += 10
        else:
            cd.rect(3.5, y, CW - 7, 18, fill="#F1F8E9" if e["kind"] == "GUT" else "#FFF8E1",
                    stroke="#C5E1A5" if e["kind"] == "GUT" else "#FFE082", lw=0.4, r=1.2)
            cd.text(5, y + 3.8, "EFFEKT", "DVCB", 5.6, col)
            cd.para(5, y + 7.5, e["effekt"], "DVCB", 7.0, C_DARK, maxw=CW - 10, lead=8.4, maxlines=3)
        cd.hline(3.5, CH - 15.5, CW - 3.5, "#CFD8DC")
        cd.text(3.5, CH - 11.8, "WALDWISSEN", "DVCB", 5.0, "#78909C")
        cd.para(3.5, CH - 8.0, e["lehr"], "DVCI", 6.2, "#37474F", maxw=CW - 7, lead=7.2, maxlines=3)
    return draw


def fach_card(f):
    name, cost, eff, n, lehr = f
    def draw(cd):
        col = "#00796B"
        cd.bg(col)
        panel(cd, CW, CH, 14)
        cd.text(3.5, 5.0, "FACHKARTE", "DVCB", 6.2, "#B2DFDB")
        size = fit_font(name, "DVB", 10.5, CW - 7 - 12, 6.5)
        cd.text(3.5, 11.2, name, "DVB", size, "#FFFFFF")
        cd.circle(CW - 7.2, 7.5, 4.6, fill="#FFD54F", stroke="#F9A825", lw=0.6)
        cd.text(CW - 7.2, 8.7, str(cost), "DVB", 10, C_DARK, "c")
        cd.text(CW - 7.2, 11.2, "T€", "DVCB", 4.4, C_DARK, "c")
        cd.text(3.5, 21, "EFFEKT", "DVCB", 5.8, col)
        cd.para(3.5, 26.5, eff, "DVCB", 9.5, C_DARK, maxw=CW - 7, lead=12)
        cd.text(3.5, CH - 11.8, "WALDWISSEN", "DVCB", 5.0, "#78909C")
        cd.hline(3.5, CH - 15.5, CW - 3.5, "#CFD8DC")
        cd.para(3.5, CH - 8.0, lehr, "DVCI", 6.2, "#37474F", maxw=CW - 7, lead=7.2, maxlines=3)
        cd.text(CW - 3.5, CH - 2.9, "nach Gebrauch ablegen", "DVC", 4.0, "#B0BEC5", "r")
    return draw


def card_back(col, titel, untertitel):
    """Einheitliche Rückseite (Ereignis-/Fachkarten): man sieht der verdeckten Karte nichts an."""
    def draw(cd):
        cd.bg(col)
        cd.rect(4.5, 4.5, CW - 9, CH - 9, stroke="#FFFFFF", lw=0.5, r=2.5)
        cd.rect(6.5, 6.5, CW - 13, CH - 13, stroke="#FFFFFF", lw=0.25, r=1.8)
        cx, cy = CW / 2, CH / 2 - 4
        cd.circle(cx, cy, 15, fill="#FFFFFF")
        cd.circle(cx, cy, 13.2, stroke=col, lw=0.5)
        # Baum-Symbol
        cd.c.saveState(); cd.c.setFillColor(hc(col))
        for i, (wd, top) in enumerate(((13, -11), (10.5, -6.5), (8, -2))):
            p = cd.c.beginPath()
            p.moveTo(cd.X(cx), cd.Y(cy + top)); p.lineTo(cd.X(cx - wd / 2), cd.Y(cy + top + 7)); p.lineTo(cd.X(cx + wd / 2), cd.Y(cy + top + 7)); p.close()
            cd.c.drawPath(p, fill=1, stroke=0)
        cd.c.restoreState()
        cd.rect(cx - 1, cy + 5, 2, 4.5, fill=col)
        cd.text(cx, cy + 27, titel, "DVB", 12, "#FFFFFF", "c")
        cd.text(cx, cy + 32.5, untertitel, "DVC", 6.5, "#E0E0E0", "c")
        cd.text(cx, CH - 11, "WALD 2080", "DVCB", 6, "#FFFFFF", "c")
    return draw


def build():
    footer = "Wald 2080 · Spielmaterial v0.4 · Spielwerte didaktisch vereinfacht · A4 beidseitig drucken, Wenden an der langen Kante, an den Marken schneiden"
    for deck, fn in (("basis", "02_Baumkarten_Basis"), ("nachbar", "03_Baumkarten_Erweiterung_Nachbarlaender"),
                     ("europa", "04_Baumkarten_Erweiterung_Europa"), ("welt", "05_Baumkarten_Erweiterung_Welt")):
        sp = [s for s in SPECIES_LIST if s["deck"] == deck]
        card_sheet(f"{OUT}/{fn}.pdf", [tree_card(s) for s in sp], CW, CH, 3, 3, footer=footer, title=fn,
                   backs=[tree_back(s) for s in sp])
        print(fn, len(sp), "Karten (je Vorder- + Rückseite)")
    st = sorted(STANDORTE, key=lambda s: (REGION_ORDER[s["reg"]], s["id"]))
    card_sheet(f"{OUT}/06_Standortkarten_alle.pdf", [standort_card(s) for s in st], MW, MH, 4, 4, footer=footer, title="Standortkarten")
    ev = EVENTS
    card_sheet(f"{OUT}/07_Ereigniskarten.pdf", [event_card(e) for e in ev], CW, CH, 3, 3, footer=footer, title="Ereigniskarten",
               backs=card_back("#37474F", "EREIGNIS", "nicht vorher ansehen!"))
    fc = [fach_card(f) for f in FACH for _ in range(f[3])]
    card_sheet(f"{OUT}/08_Fachkarten.pdf", fc, CW, CH, 3, 3, footer=footer, title="Fachkarten",
               backs=card_back("#00796B", "FACHKARTE", "Wissen hilft im Revier"))
    print("Standorte", len(st), "Ereignisse", len(ev), "Fachkarten", len(fc))


if __name__ == "__main__":
    build()

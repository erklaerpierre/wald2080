# -*- coding: utf-8 -*-
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
from data import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)
GREEN = "#2E7D32"


def hexpath(cd, cx, cy, R, fill=None, stroke=None, lw=0.8):
    c = cd.c
    p = c.beginPath()
    for i in range(6):
        a = math.radians(30 + 60 * i)
        x, y = cx + R * math.cos(a), cy - R * math.sin(a)
        if i == 0: p.moveTo(cd.X(x), cd.Y(y))
        else: p.lineTo(cd.X(x), cd.Y(y))
    p.close()
    c.saveState()
    if fill: c.setFillColor(hc(fill))
    if stroke: c.setStrokeColor(hc(stroke))
    c.setLineWidth(lw)
    c.drawPath(p, stroke=1 if stroke else 0, fill=1 if fill else 0)
    c.restoreState()


def lines(cd, x, y, items, size=7.6, font="DVC", color=C_DARK, lead=4.3, maxw=140):
    for it in items:
        if isinstance(it, tuple):
            txt, f, col = it
        else:
            txt, f, col = it, font, color
        for ln in wrap(txt, f, size, maxw):
            cd.text(x, y, ln, f, size, col); y += lead
    return y


def track(cd, x, y, n0, n1, cw, ch, label, marks=None, start=None):
    marks = marks or {}
    cd.text(x, y - 2, label, "DVB", 9, C_DARK)
    for i, v in enumerate(range(n0, n1 + 1)):
        fill = marks.get(v, "#FFFFFF")
        cd.rect(x + i * cw, y, cw - 0.4, ch, fill=fill, stroke="#78909C", lw=0.4, r=0.8)
        cd.text(x + i * cw + (cw - 0.4) / 2, y + ch - 2.4, str(v), "DVCB", 7, C_DARK, "c")


def revierplan():
    fn = f"{OUT}/09_Revierplan_A3.pdf"
    c = canvas.Canvas(fn, pagesize=landscape(A3))
    c.setTitle("Wald 2080 – Revierplan (A3)")
    cd = Card(c, 0, 0, 420, 297)
    # Titel
    cd.text(10, 13, "WALD 2080", "DVB", 22, GREEN)
    cd.text(70, 13, "Revierplan", "DVB", 22, C_DARK)
    cd.text(10, 19.5, "Ein Revier = 7 Felder (1 Mitte, 2–7 im Uhrzeigersinn). Standortkarten unten ablegen – Bäume mit Etiketten auf die Felder legen.", "DVCI", 8, "#546E7A")
    cd.text(252, 12, "Team: ______________________   Edition / Region: ______________________", "DV", 9.5, C_DARK)
    # Hexfeld
    cx, cy, d = 128, 122, 70
    R = d / math.sqrt(3)
    ang = {1: None, 2: 60, 3: 0, 4: -60, 5: -120, 6: 180, 7: 120}
    for n in range(1, 8):
        if ang[n] is None: hx, hy = cx, cy
        else:
            a = math.radians(ang[n]); hx, hy = cx + d * math.cos(a), cy - d * math.sin(a)
        hexpath(cd, hx, hy, R - 0.6, fill="#F1F8E9" if n > 1 else "#E8F5E9", stroke=GREEN, lw=1.2)
        cd.circle(hx, hy - 24.5, 5.2, fill=GREEN)
        cd.text(hx, hy - 22.6, str(n), "DVB", 11, "#FFFFFF", "c")
        # Haupt / Misch
        for lab, yy in (("HAUPTBAUMART", hy - 17), ("MISCHBAUMART", hy - 4)):
            cd.text(hx, yy - 0.8, lab, "DVCB", 4.8, "#78909C", "c")
            cd.rect(hx - 14, yy, 28, 10.5, fill="#FFFFFF", stroke="#90A4AE", lw=0.5, r=1)
        # Herzen
        for i in range(3):
            cd.circle(hx - 10 + i * 10, hy + 14.5, 4.0, fill="#FFFFFF", stroke="#C62828", lw=0.8)
            cd.text(hx - 10 + i * 10, hy + 16.2, "♥", "DV", 8, "#EF9A9A", "c")
        cd.text(hx, hy + 22.3, "Herzen", "DVCB", 4.8, "#C62828", "c")
        # J und B
        cd.rect(hx - 13.5, hy + 25.2, 6.5, 6.5, fill="#FFFFFF", stroke="#F9A825", lw=0.6, r=1)
        cd.text(hx - 10.25, hy + 30.1, "J", "DVB", 6.5, "#F9A825", "c")
        cd.rect(hx + 7, hy + 25.2, 6.5, 6.5, fill="#FFFFFF", stroke="#6D4C41", lw=0.6, r=1)
        cd.text(hx + 10.25, hy + 30.1, "B", "DVB", 6.5, "#6D4C41", "c")
    cd.text(10, 227.2, "♥ = Herzen (Münzen auflegen: 3 = voll, 0 = Kahlfläche)    J = Jungwuchs    B = Befall", "DVC", 6.5, "#546E7A")
    # Standortkarten-Slots
    cd.text(200, 227.2, "STANDORTKARTEN  (Feld 1 bis 7)", "DVB", 8, GREEN)
    for i in range(7):
        sx = 10 + i * 49.5
        cd.rect(sx, 232.5, 45, 63, fill="#FAFAFA", stroke="#90A4AE", lw=0.7, r=CORNER_R)
        cd.circle(sx + 5, 238, 3.4, fill=GREEN)
        cd.text(sx + 5, 239.6, str(i + 1), "DVB", 8, "#FFFFFF", "c")
    # Rechte Spalte
    X0 = 262
    cd.text(X0, 33, "Waldstabilität (SP)", "DVB", 11, C_DARK)
    for v in range(0, 21):
        fill = "#FFCDD2" if v == 0 else ("#C8E6C9" if v >= 12 else "#FFFFFF")
        cd.rect(X0 + v * 7.0, 37, 6.6, 10, fill=fill, stroke="#78909C", lw=0.5, r=1)
        cd.text(X0 + v * 7.0 + 3.3, 43.8, str(v), "DVCB", 7.5, C_DARK, "c")
    cd.text(X0 + 8 * 7.0 + 3.3, 52, "Start", "DVCB", 6.2, "#1565C0", "c")
    cd.text(X0 + 8 * 7.0 + 3.3, 49.5, "▼", "DV", 5, "#1565C0", "c")
    cd.text(X0 + 12 * 7.0 + 3.3, 52, "Ziel ≥ 12", "DVCB", 6.2, GREEN, "c")
    cd.text(X0 + 0 * 7.0 + 3.3, 52, "Kollaps", "DVCB", 6.2, "#C62828", "c")
    cd.text(X0, 66, "Kasse (T€)", "DVB", 11, C_DARK)
    for v in range(0, 21):
        cd.rect(X0 + v * 7.0, 70, 6.6, 10, fill="#FFF8E1", stroke="#F9A825", lw=0.5, r=1)
        cd.text(X0 + v * 7.0 + 3.3, 76.8, str(v), "DVCB", 7.5, C_DARK, "c")
    cd.text(X0, 85, "Start: 8 SP und 4 T€  ·  Einkommen jede Runde: +3 T€  ·  Marker (Münze/Büroklammer) auf die Leisten legen.", "DVCI", 7, "#546E7A")
    # Ablauf
    cd.rect(X0, 92, 148, 82, fill="#F5F5F5", stroke="#CFD8DC", lw=0.5, r=2)
    cd.text(X0 + 4, 99, "EINE RUNDE = EIN JAHRZEHNT", "DVB", 9.5, GREEN)
    y = 106
    steps = [("A  Vorschau", "Oberste Ereigniskarte aufdecken (Vorwarnung). Die zweite bleibt verdeckt."),
             ("B  Einnahmen", "+3 T€, 1 Fachkarte ziehen (max. 3 auf der Hand)."),
             ("C  Planen & Handeln", "Gemeinsam beraten, dann Maßnahmen umsetzen (siehe unten)."),
             ("D  Ereignisse", "Beide Karten nacheinander: W6 für ALLE würfeln, jedes Team prüft seine Felder."),
             ("E  Bilanz", "Erholung, Jungwuchs endet, Stabilität (SP) berechnen.")]
    for t, d_ in steps:
        cd.text(X0 + 4, y, t, "DVCB", 7.6, C_DARK)
        y2 = lines(cd, X0 + 40, y, [d_], 7.4, maxw=104, lead=3.9)
        y = max(y + 6.4, y2 + 1.6)
    cd.text(X0 + 4, y + 1, "Maßnahmen (Phase C):", "DVCB", 7.6, GREEN)
    ms = ["Pflanzen (Hauptbaum auf Kahlfläche): Kosten der Baumkarte → 2 Herzen, Jungwuchs",
          "Mischbaum ergänzen (Feld mit ≥ 1 Herz): Kosten der Baumkarte, Jungwuchs",
          "Pflege / Durchforstung: 1 T€ → +1 Herz (max. 3)    ·    Wildschutz: 1 T€ → Verbiss +2",
          "Nutzung (Ernte, Feld ≥ 2 Herzen): Holzwert +1 bei 3 Herzen als T€ → Kahlfläche"]
    y += 5.2
    for m in ms:
        y = lines(cd, X0 + 6, y, ["• " + m], 7.0, maxw=138, lead=3.7) + 0.6
    # Kurz-Probe (Details: Rückseite)
    cd.rect(X0, 180, 148, 40, fill="#FFFDE7", stroke="#FBC02D", lw=0.6, r=2)
    cd.text(X0 + 4, 187, "PROBE FÜR JEDES BETROFFENE FELD", "DVB", 9.5, "#F57F17")
    cd.text(X0 + 4, 195, "W6 + Widerstandswert + Eignungsbonus + Standort-Mod. − Jungwuchs ≥ Stärke", "DVCB", 7.6, C_DARK)
    y = 201
    for l in ["Mischbestand: Ein Wurf, zwei Bäume – Schaden nur, wenn BEIDE Arten die Probe verfehlen.",
              "Verfehlt: −1 Herz · um 4 oder mehr verfehlt: −2 Herzen · 0 Herzen = Kahlfläche.",
              "Alle Regeln, Eignungstabelle und Bilanz: siehe Rückseite (Seite 2)."]:
        y = lines(cd, X0 + 4, y, ["• " + l], 7.0, maxw=140, lead=3.7) + 1.4
    c.showPage()
    # ---------------- Seite 2: Spickzettel
    cd = Card(c, 0, 0, 420, 297)
    cd.text(10, 14, "WALD 2080", "DVB", 22, GREEN)
    cd.text(70, 14, "Spickzettel für dein Team", "DVB", 22, C_DARK)
    def box(x, y, w, h, title, items, fill, stroke, tcol, size=11.2):
        cd.rect(x, y, w, h, fill=fill, stroke=stroke, lw=0.8, r=2.5)
        cd.text(x + 5, y + 8, title, "DVB", 11.5, tcol)
        yy = y + 15
        for it in items:
            yy = lines(cd, x + 6, yy, ["• " + it], size, maxw=w - 12, lead=size * 0.53) + 2.2
    box(10, 24, 195, 88, "EINE RUNDE = EIN JAHRZEHNT", [
        "A  Vorschau: Oberste Ereigniskarte aufdecken – das ist eure Vorwarnung. Die zweite bleibt verdeckt.",
        "B  Einnahmen: +3 T€ pro Revier, eine Fachkarte ziehen (maximal 3 auf der Hand).",
        "C  Planen & Handeln: Gemeinsam beraten, dann Maßnahmen umsetzen.",
        "D  Ereignisse: Beide Karten nacheinander. EINE Person würfelt den W6 für die ganze Klasse. Jedes Team prüft seine Felder.",
        "E  Bilanz: Erholung, Jungwuchs endet, Stabilität (SP) berechnen. Rundenmarker weiter."],
        "#F5F5F5", "#CFD8DC", GREEN)
    box(215, 24, 195, 88, "MASSNAHMEN IN PHASE C", [
        "Pflanzen (Hauptbaum, nur auf Kahlfläche): Kosten der Baumkarte → Feld erhält 2 Herzen, Jungwuchs.",
        "Mischbaum ergänzen (Feld mit ≥ 1 Herz, noch ohne Mischbaum): Kosten der Baumkarte, Mischbaum ist Jungwuchs.",
        "Pflege / Durchforstung: 1 T€ → +1 Herz (max. 3).",
        "Wildschutz: 1 T€ → Verbiss-Proben +2 in dieser Runde.",
        "Nutzung (Ernte): Feld mit ≥ 2 Herzen. Einnahme = Holzwert der Hauptbaumart (+1 bei 3 Herzen). Danach Kahlfläche.",
        "Fachkarten ausspielen: Kosten stehen auf der Karte. Hilfe: Münzen an andere Teams geben."],
        "#F5F5F5", "#CFD8DC", GREEN)
    box(10, 118, 195, 84, "DIE PROBE (PRO BETROFFENEM FELD)", [
        "W6 + Widerstandswert der Baumart (Dürre, Sturm …) + Eignungsbonus + Standort-Modifikator − Jungwuchs  ≥  Stärke der Karte.",
        "Mischbestand: Ein Wurf, zwei Bäume. Das Feld verliert nur dann Herzen, wenn BEIDE Arten die Probe verfehlen. Ist die Mischbaumart vom Ereignis nicht betroffen, rettet sie das Feld.",
        "Verfehlt: −1 Herz.  Um 4 oder mehr verfehlt: −2 Herzen.  0 Herzen = Kahlfläche, Baumkarten ablegen.",
        "Befallskette (Käfer, Pilze): Gleiche Reinbestände neben einem betroffenen Feld werden mit −1 erneut geprüft, bis nichts Neues mehr passiert.",
        "Jungwuchs: −1 (Pionierarten nie). Klimastufe ≥ 2: Dürre-, Käfer-, Feuerereignisse +1 Stärke. Brandenburg: Dürre und Feuer +3. Bayern: Sturm und Schnee +1."],
        "#FFFDE7", "#FBC02D", "#F57F17", 9.6)
    box(215, 118, 195, 84, "EIGNUNG EINER BAUMART AUF EINEM FELD", [
        "Prüfe drei Achsen: Liegt der Standortwert im markierten Bereich der Baumkarte? Wasser · Nährstoffe · Wärme.",
        "Rechne mit der aktuellen Klimastufe: Wärme +Stufe (max. 5), Wasser −Stufe/2 (abgerundet, min. 1).",
        "E 3 → Bonus +2 · E 2 → 0 · E 1 → −2 · E 0 → Pflanzen nicht erlaubt.",
        "Bodenverbesserer als Mischbaum: Nährstoffe der Hauptbaumart gelten als passend.",
        "Schattenbaumarten als Mischbaum und Pionierarten: kein Jungwuchs-Malus."],
        "#E3F2FD", "#90CAF9", "#1565C0", 10.2)
    box(10, 208, 195, 82, "BILANZ AM RUNDENENDE", [
        "Erholung: Felder mit 1–2 Herzen und voller Eignung (E 3) erhalten +1 Herz.",
        "−2 SP je Kahlfläche · −1 SP je Feld mit nur 1 Herz · −1 SP je Feld mit invasiver Art.",
        "+1 SP, wenn mindestens die Hälfte der Felder Mischbestand mit ≥ 2 Herzen hat.",
        "+1 SP, wenn im Revier ≥ 5 verschiedene nicht-invasive Baumarten stehen.",
        "Danach: Jungwuchs-, Schutz- und Befall-Marker entfernen. SP bleibt zwischen 0 und 20."],
        "#E8F5E9", "#A5D6A7", GREEN, 10.2)
    box(215, 208, 195, 82, "GEWINNEN – GEMEINSAM!", [
        "Ziel am Ende: Der Durchschnitt aller Reviere erreicht 12 SP (Langspiel: 14 SP).",
        "Kein Revier darf bei 0 SP stehen (Kollaps). Ein kollabiertes Revier kann gerettet werden: Je 2 T€ aus Kasse oder Fördertopf anderer Teams ergeben +1 SP.",
        "Tauscht Baumkarten, gebt Münzen weiter und sprecht Vorwarnungen ab – Waldumbau gelingt nur gemeinsam.",
        "Tipp: Mischung, Standorteignung und Vielfalt sind eure stärksten Werkzeuge."],
        "#F3E5F5", "#CE93D8", "#6A1B9A", 10.2)
    c.showPage(); c.save()


def leitstelle():
    fn = f"{OUT}/10_Leitstelle_A3.pdf"
    c = canvas.Canvas(fn, pagesize=landscape(A3))
    c.setTitle("Wald 2080 – Leitstelle (A3)")
    cd = Card(c, 0, 0, 420, 297)
    cd.text(10, 13, "WALD 2080", "DVB", 22, GREEN)
    cd.text(70, 13, "Leitstelle – gemeinsame Tafel für die ganze Klasse", "DVB", 16, C_DARK)
    cd.text(10, 19.5, "Eine Leitstelle pro Spiel. Alle Teams spielen gemeinsam gegen die Ereignisse. Ein einziger Würfel entscheidet das „Wetter“ für alle.", "DVCI", 8, "#546E7A")
    # Rundenleiste
    short = {1, 3, 6}; std = {1, 2, 3, 4, 5, 6}
    kk = KLIMAPFAD_STANDARD
    kcol = {0: "#C8E6C9", 1: "#FFF9C4", 2: "#FFE0B2", 3: "#FFCCBC"}
    cd.text(10, 28, "RUNDENLEISTE", "DVB", 10, C_DARK)
    for r in range(1, 9):
        x = 10 + (r - 1) * 50
        cd.rect(x, 31, 46, 44, fill=kcol[kk[r]], stroke="#78909C", lw=0.8, r=2.5)
        cd.text(x + 23, 44, str(JAHRE[r]), "DVB", 17, C_DARK, "c")
        cd.text(x + 23, 50, f"Runde {r}", "DVC", 7.5, "#546E7A", "c")
        cd.text(x + 23, 58, f"Klimastufe {kk[r]}", "DVCB", 9, "#BF360C", "c")
        for i, (lab, member) in enumerate((("K", r in short), ("S", r in std), ("L", True))):
            cd.circle(x + 11 + i * 12, 67.5, 3.4, fill=GREEN if member else "#FFFFFF", stroke=GREEN if member else C_GREY, lw=0.5)
            cd.text(x + 11 + i * 12, 69.2, lab, "DVB", 6.5, "#FFFFFF" if member else C_GREY, "c")
        cd.rect(x + 3, 71.4, 40, 0.1, fill="#78909C")
    cd.text(10, 80, "Rundenmarker auf die aktuelle Runde stellen.   K = Kurzspiel (3 Felder, 3 Runden: 2030 · 2050 · 2080)   S = Standardspiel (bis 2080)   L = Langspiel (bis 2100)", "DVC", 7.5, "#546E7A")
    # Ereignisfelder
    cd.text(10, 92, "EREIGNISSE", "DVB", 10, C_DARK)
    for i, lab in enumerate(("Stapel (verdeckt)", "Vorschau (aufgedeckt)", "Ablage")):
        sx = 10 + i * 69
        cd.rect(sx - 1, 94, 65, 90, fill="#FAFAFA", stroke="#90A4AE", lw=0.8, r=CORNER_R + 0.8)
        cd.text(sx + 31.5, 140, lab, "DVCB", 8.5, "#78909C", "c")
        cd.text(sx + 31.5, 145, "Karte 63 × 88 mm", "DVC", 6, "#B0BEC5", "c")
    cd.text(10, 188, "Kurz 6 · Standard 12 · Lang 16 Karten  (≈ 80 % Schadens-, 20 % Glücks-/Klimakarten)", "DVCI", 7.3, "#546E7A")
    # Klimastufen
    X0 = 224
    cd.text(X0, 92, "KLIMASTUFEN  (Wirkung auf die Standorte)", "DVB", 10, C_DARK)
    hdr = ["Klimastufe", "Wärme", "Wasser", "Zeitraum"]
    rows = [("0", "+0", "−0", "2030 – 2040"), ("1", "+1", "−0", "2050 – 2060"),
            ("2", "+2", "−1", "2070 – 2080"), ("3", "+3", "−1", "2090 – 2100")]
    cw = [36, 32, 32, 44]
    yy = 96
    xx = X0
    for h, w in zip(hdr, cw):
        cd.rect(xx, yy, w, 8, fill=C_DARK); cd.text(xx + w / 2, yy + 5.6, h, "DVCB", 8, "#FFFFFF", "c"); xx += w
    for i, row in enumerate(rows):
        yy += 8; xx = X0
        for v, w in zip(row, cw):
            cd.rect(xx, yy, w, 8, fill=kcol[i], stroke="#B0BEC5", lw=0.3)
            cd.text(xx + w / 2, yy + 5.6, v, "DVCB", 8.5, C_DARK, "c"); xx += w
    cd.text(X0, 140, "Wärme-Achse des Standorts +k (max. 5), Wasser-Achse −k/2 abgerundet (min. 1).", "DVC", 7.2, "#37474F")
    cd.text(X0, 145, "Die Eignung aller Bäume wird jede Runde mit der aktuellen Klimastufe neu bestimmt!", "DVCB", 7.2, "#BF360C")
    cd.text(X0, 150, "„Heißes Jahrzehnt“ / „Kühles Jahrzehnt“ ändern die Stufe nur für diese Runde.", "DVC", 7.2, "#37474F")
    # Fördertopf
    cd.rect(X0, 156, 74, 32, fill="#FFF8E1", stroke="#F9A825", lw=0.8, r=2.5)
    cd.text(X0 + 4, 163, "FÖRDERTOPF (T€)", "DVB", 9, "#E65100")
    cd.text(X0 + 4, 169, "Gemeinsame Kasse. Teams dürfen jederzeit", "DVC", 6.6, "#37474F")
    cd.text(X0 + 4, 173, "einzahlen oder (nach Absprache) entnehmen.", "DVC", 6.6, "#37474F")
    for i in range(10):
        cd.circle(X0 + 8 + i * 6.4, 181, 2.7, fill="#FFFFFF", stroke="#F9A825", lw=0.6)
    cd.rect(X0 + 80, 156, 104, 32, fill="#E3F2FD", stroke="#90CAF9", lw=0.8, r=2.5)
    cd.text(X0 + 84, 163, "DER WÜRFEL", "DVB", 9, "#1565C0")
    lines(cd, X0 + 84, 169, ["Pro Ereignis wirft EINE Person den W6 für die gesamte Klasse. Dieselbe Zahl gilt für alle Reviere – so seht ihr, wie unterschiedlich dieselbe Ursache wirkt."], 6.8, maxw=96, lead=3.7)
    # Teamtabelle
    cd.text(10, 197, "STABILITÄTSTABELLE  (SP am Ende jeder Runde eintragen)", "DVB", 10, C_DARK)
    ty = 200
    cols = ["Team"] + ["Start"] + [f"R{r}" for r in range(1, 9)] + ["Ziel"]
    cws = [34] + [14] + [15] * 8 + [26]
    x = 10
    for h, w in zip(cols, cws):
        cd.rect(x, ty, w, 8, fill=C_DARK); cd.text(x + w / 2, ty + 5.6, h, "DVCB", 8, "#FFFFFF", "c"); x += w
    cd.text(10, ty + 8 + 1, "", "DV", 1)
    for r in range(6):
        y = ty + 8 + r * 11
        x = 10
        for j, w in enumerate(cws):
            fill = "#FFFFFF"
            txt = ""
            if j == 0: txt = f"Team {r + 1}" if r < 5 else "Ø Klasse"; fill = "#ECEFF1"
            if j == 1: txt = "8" if r < 5 else "8"; fill = "#E3F2FD"
            if j == len(cws) - 1: txt = "≥ 12  (L: 14)"; fill = "#E8F5E9"
            cd.rect(x, y, w, 11, fill=fill, stroke="#B0BEC5", lw=0.4)
            if txt: cd.text(x + w / 2, y + 7.2, txt, "DVCB", 7.4 if j == 0 else 6.8, C_DARK, "c")
            x += w
    cd.text(10, 277, "Gewonnen: Der Durchschnitt aller Reviere erreicht am Ende das Ziel (Kurz & Standard 12 SP, Lang 14 SP) und kein Revier steht bei 0 SP.", "DVCB", 8, GREEN)
    cd.text(10, 283, "Revier bei 0 SP = Kollaps. Notfallhilfe: Die anderen Teams dürfen spenden – je 2 T€ aus Kasse oder Fördertopf ergeben +1 SP für das Revier.", "DVC", 7.6, "#37474F")
    cd.text(10, 289, "Verloren: Mehr als die Hälfte der Reviere kollabiert, oder das Ziel wird verfehlt.", "DVC", 7.6, "#37474F")
    # Eignung
    cd.rect(X0, 197, 186, 90, fill="#F5F5F5", stroke="#CFD8DC", lw=0.6, r=2.5)
    cd.text(X0 + 4, 204, "EIGNUNG EINER BAUMART AUF EINEM FELD", "DVB", 9.5, GREEN)
    ls = ["Prüfe drei Achsen: Liegt der Standortwert (mit Klimastufe!) im markierten Bereich der Baumkarte?",
          "     Wasser · Nährstoffe · Wärme   →   E = Anzahl der passenden Achsen (0 bis 3)",
          "E 3 voll geeignet: Bonus +2, Erholung möglich    ·    E 2 bedingt: 0    ·    E 1 schwach: −2    ·    E 0: nicht pflanzbar",
          "Bodenverbesserer (Erle, Linde, Hainbuche …) als Mischbaum: Nährstoffe der Hauptbaumart gelten als passend.",
          "Schattenbaumarten als Mischbaum und Pionierarten haben keinen Jungwuchs-Malus."]
    y = 211
    for l in ls:
        y = lines(cd, X0 + 4, y, [l], 7.2, maxw=178, lead=3.9) + 1.2
    cd.text(X0 + 4, y + 3, "SYMBOLE", "DVB", 9.5, GREEN)
    cd.text(X0 + 4, y + 9, "T€ = Tausend Euro (Spielgeld)    ♥ = Herz (Vitalität 0–3)    SP = Stabilitätspunkte    J = Jungwuchs    B = Befall", "DVC", 7.2, C_DARK)
    c.showPage(); c.save()


def etiketten():
    """Baum-Etiketten 26 x 12 mm, Vorder- und Rückseite (Rückseite = Baumbild), mit Anschnitt."""
    from cardart import zeichne_bild
    fn = f"{OUT}/11_Baum-Etiketten.pdf"
    items = []
    for s in SPECIES_LIST:
        items += [s, s]
    W, H = 26, 12
    def front(s):
        def draw(cd):
            col = C_DECK[s["deck"]]
            cd.bg(col)
            cd.rect(0.8, 0.8, W - 1.6, H - 1.6, fill="#FFFFFF", r=0.8)
            size = 6.2
            ln = wrap(s["name"], "DVCB", size, W - 5)
            while (len(ln) > 2 or any(breite(l, "DVCB", size) > (W - 4.6) * mm for l in ln)) and size > 4.2:
                size -= 0.2; ln = wrap(s["name"], "DVCB", size, W - 5)
            y0 = 6.5 if len(ln) == 1 else 4.8
            for i, l in enumerate(ln[:2]): cd.text(2.2, y0 + i * 3.0, l, "DVCB", size, C_DARK)
            cd.text(W - 1.9, H - 1.9, f'{s["cost"]} T€', "DVC", 4.0, "#78909C", "r")
        return draw
    def back(s):
        def draw(cd):
            cd.bg(C_DECK[s["deck"]])
            zeichne_bild(cd, s["id"], s, -1.1, -1.1, W + 2.2, H + 2.2, radius=0, kurz=True)
            cd.rect(-1.1, H - 3.6, W + 2.2, 4.8, fill=Color(0, 0, 0, alpha=0.6))
            sz = fit_font(s["name"], "DVCB", 4.6, W - 3, 3.4)
            cd.text(W / 2, H - 1.1, s["name"], "DVCB", sz, "#FFFFFF", "c")
        return draw
    card_sheet(fn, [front(s) for s in items], W, H, 7, 20, title="Baum-Etiketten", bleed=1.0,
               backs=[back(s) for s in items],
               footer="Wald 2080 · Baum-Etiketten (2 je Art: Haupt- und Mischbaum) · beidseitig drucken, Wenden an der langen Kante")
    print("Etiketten:", len(items))


if __name__ == "__main__":
    revierplan(); leitstelle(); etiketten()

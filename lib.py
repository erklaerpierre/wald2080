# -*- coding: utf-8 -*-
"""Gemeinsame Zeichenhilfen für Wald 2080 (reportlab)."""
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white, black, Color
from reportlab.lib.pagesizes import A4, A3, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FD = "/usr/share/fonts/truetype/dejavu/"
for name, f in [("DV", "DejaVuSans.ttf"), ("DVB", "DejaVuSans-Bold.ttf"), ("DVI", "DejaVuSans-Oblique.ttf"),
                ("DVC", "DejaVuSansCondensed.ttf"), ("DVCB", "DejaVuSansCondensed-Bold.ttf"),
                ("DVCI", "DejaVuSansCondensed-Oblique.ttf")]:
    pdfmetrics.registerFont(TTFont(name, FD + f))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("DV", normal="DV", bold="DVB", italic="DVI", boldItalic="DVB")
registerFontFamily("DVC", normal="DVC", bold="DVCB", italic="DVCI", boldItalic="DVCB")

# Farben
C_DECK = {"basis": "#2E7D32", "nachbar": "#1565C0", "europa": "#E65100", "welt": "#6A1B9A"}
C_WASSER, C_NAEHR, C_WAERME = "#1E88E5", "#8D6E63", "#E64A19"
CORNER_R = 3.5     # mm – Radius des Eckenrunders; Stapelmarkierungen nutzen denselben Wert
BLEED = 2.0        # mm Anschnitt rund um jede Karte (Farbe läuft über die Schnittkante hinaus)
C_KIND = {"DÜ": "#E65100", "ST": "#455A64", "KÄ": "#6D4C41", "PI": "#7B1FA2", "FR": "#0288D1",
          "FE": "#C62828", "VE": "#827717", "GUT": "#2E7D32", "KL": "#F9A825"}
KIND_NAME = {"DÜ": "DÜRRE / HITZE", "ST": "STURM / SCHNEE", "KÄ": "KÄFER / INSEKTEN", "PI": "PILZE / KRANKHEIT",
             "FR": "FROST", "FE": "FEUER", "VE": "WILD / VERBISS", "GUT": "GLÜCKSFALL", "KL": "KLIMA"}
C_GREY = "#B0BEC5"
C_LGREY = "#ECEFF1"
C_DARK = "#263238"


def hc(x): return HexColor(x)


def wrap(text, font, size, maxw_mm):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if pdfmetrics.stringWidth(t, font, size) <= maxw_mm * mm:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines


def fit_font(text, font, size, maxw_mm, minsize=5.0):
    while size > minsize and pdfmetrics.stringWidth(text, font, size) > maxw_mm * mm:
        size -= 0.25
    return size


class Card:
    """Zeichenfläche mit Koordinaten in mm, Ursprung links oben (y nach unten)."""
    def __init__(self, c, x, y, w, h):
        self.c, self.x, self.y, self.w, self.h = c, x, y, w, h

    def bg(self, fill, bleed=None):
        """Vollflächiger Hintergrund INKLUSIVE Anschnitt (Farbe reicht über die Schnittkante hinaus)."""
        b = (BLEED if bleed is None else bleed) + 0.1
        self.rect(-b, -b, self.w + 2 * b, self.h + 2 * b, fill=fill)

    def X(self, v): return (self.x + v) * mm
    def Y(self, v): return (self.y + self.h - v) * mm

    def rect(self, x, y, w, h, fill=None, stroke=None, lw=0.3, r=0):
        c = self.c
        c.saveState()
        if fill: c.setFillColor(hc(fill) if isinstance(fill, str) else fill)
        if stroke: c.setStrokeColor(hc(stroke) if isinstance(stroke, str) else stroke)
        c.setLineWidth(lw)
        if r:
            c.roundRect(self.X(x), self.Y(y + h), w * mm, h * mm, r * mm, stroke=1 if stroke else 0, fill=1 if fill else 0)
        else:
            c.rect(self.X(x), self.Y(y + h), w * mm, h * mm, stroke=1 if stroke else 0, fill=1 if fill else 0)
        c.restoreState()

    def circle(self, x, y, r, fill=None, stroke=None, lw=0.3):
        c = self.c
        c.saveState()
        if fill: c.setFillColor(hc(fill))
        if stroke: c.setStrokeColor(hc(stroke))
        c.setLineWidth(lw)
        c.circle(self.X(x), self.Y(y), r * mm, stroke=1 if stroke else 0, fill=1 if fill else 0)
        c.restoreState()

    def text(self, x, y, s, font="DVC", size=7, color="#000000", align="l"):
        c = self.c
        c.saveState()
        c.setFillColor(hc(color)); c.setFont(font, size)
        if align == "l": c.drawString(self.X(x), self.Y(y), s)
        elif align == "c": c.drawCentredString(self.X(x), self.Y(y), s)
        else: c.drawRightString(self.X(x), self.Y(y), s)
        c.restoreState()

    def para(self, x, y, s, font="DVC", size=6, color="#000000", maxw=50, lead=None, maxlines=99, align="l"):
        lead_mm = (lead or size * 1.22) / 2.83465
        lines = wrap(s, font, size, maxw)[:maxlines]
        for i, ln in enumerate(lines):
            self.text(x if align == "l" else x + maxw / 2, y + i * lead_mm, ln, font, size, color, align)
        return len(lines) * lead_mm

    def hline(self, x1, y, x2, color=C_GREY, lw=0.3):
        c = self.c; c.saveState(); c.setStrokeColor(hc(color)); c.setLineWidth(lw)
        c.line(self.X(x1), self.Y(y), self.X(x2), self.Y(y)); c.restoreState()


def card_sheet(filename, draws, cw, ch, cols, rows, pagesize=A4, title=None, footer=None,
               backs=None, bleed=BLEED, footer_y=3.2, marks=True):
    """Legt Karten raster-weise auf Seiten – mit Anschnitt und Schneidemarken.

    Zwischen den Karten liegt ein Abstand von 2 x Anschnitt: Die Anschnitte benachbarter Karten
    berühren sich, es bleibt nie ein weißer Streifen. Geschnitten wird an den Karten-Kanten.
    backs: None | Zeichenfunktion für alle Rückseiten | Liste je Karte. Rückseitenseiten werden
    direkt hinter die Vorderseite gesetzt, Spalten gespiegelt (3 2 1 / 6 5 4 / 9 8 7) –
    beidseitig drucken, Wenden an der LANGEN Kante.
    """
    c = canvas.Canvas(filename, pagesize=pagesize)
    c.setTitle(title or filename); c.setAuthor("Wald 2080")
    pw, ph = pagesize[0] / mm, pagesize[1] / mm
    gap = 2 * bleed
    tw, th = cols * cw + (cols - 1) * gap, rows * ch + (rows - 1) * gap
    mx, my = (pw - tw) / 2, (ph - th) / 2
    per = cols * rows

    def page(items, mirror):
        if footer:
            c.setFont("DVC", 6); c.setFillColor(hc("#90A4AE"))
            c.drawCentredString(pagesize[0] / 2, footer_y * mm, footer + ("   ·   RÜCKSEITEN" if mirror else ""))
        if marks:
            c.saveState(); c.setStrokeColor(hc("#000000")); c.setLineWidth(0.25)
            for k in range(cols):
                x0 = mx + k * (cw + gap)
                for x in (x0, x0 + cw):
                    for (ya, yb) in ((ph - my + bleed + 0.8, ph - my + bleed + 0.8 + min(3.5, my - bleed - 1.6)),
                                     (my - bleed - 0.8, my - bleed - 0.8 - min(3.5, my - bleed - 1.6))):
                        c.line(x * mm, ya * mm, x * mm, yb * mm)
            for k in range(rows):
                y0 = my + k * (ch + gap)
                for y in (y0, y0 + ch):
                    for (xa, xb) in ((mx - bleed - 0.8, mx - bleed - 0.8 - min(3.5, mx - bleed - 1.6)),
                                     (pw - mx + bleed + 0.8, pw - mx + bleed + 0.8 + min(3.5, mx - bleed - 1.6))):
                        c.line(xa * mm, y * mm, xb * mm, y * mm)
            c.restoreState()
        for k, d in enumerate(items):
            if d is None: continue
            col, row = k % cols, k // cols
            if mirror: col = cols - 1 - col
            cd = Card(c, mx + col * (cw + gap), my + (rows - 1 - row) * (ch + gap), cw, ch)
            c.saveState()
            p = c.beginPath()
            p.rect((cd.x - bleed - 0.1) * mm, (cd.y - bleed - 0.1) * mm, (cw + 2 * bleed + 0.2) * mm, (ch + 2 * bleed + 0.2) * mm)
            c.clipPath(p, stroke=0, fill=0)
            d(cd)
            c.restoreState()

    n = len(draws)
    for p0 in range(0, n, per):
        if p0: c.showPage()
        page(draws[p0:p0 + per], False)
        if backs is not None:
            c.showPage()
            bl = [backs] * len(draws[p0:p0 + per]) if callable(backs) else backs[p0:p0 + per]
            page(bl, True)
    c.save()

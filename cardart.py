# -*- coding: utf-8 -*-
"""Bilder, Kachelkarte und Platzhalter für die Karten."""
import os, csv
from lib import *
from data import REGION_LISTE, REGIONEN, LAENDER
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
BILD_DIR = os.path.join(BASE, "bilder")
CACHE = os.path.join(BILD_DIR, "_cache")
EXT = (".jpg", ".jpeg", ".png", ".webp")
LAND_COL = {"DE": "#37474F", "AT": "#C62828", "CH": "#1565C0"}


def quellen():
    """bilder/quellen.csv  ->  {id: {urheber, lizenz, quelle, titel}}"""
    fn = os.path.join(BILD_DIR, "quellen.csv")
    out = {}
    if os.path.exists(fn):
        with open(fn, encoding="utf-8-sig") as f:
            for row in csv.DictReader(f, delimiter=";"):
                out[row["id"]] = row
    return out

QUELLEN = quellen()


def bild_pfad(sid):
    for e in EXT:
        p = os.path.join(BILD_DIR, sid + e)
        if os.path.exists(p):
            return p
    return None


def bild_zugeschnitten(sid, w_mm, h_mm, dpi=300):
    """Liefert Pfad eines auf Seitenverhältnis zugeschnittenen JPEG (Cache) oder None."""
    p = bild_pfad(sid)
    if not p:
        return None
    os.makedirs(CACHE, exist_ok=True)
    out = os.path.join(CACHE, f"{sid}_{int(w_mm*10)}x{int(h_mm*10)}.jpg")
    if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(p):
        return out
    im = Image.open(p).convert("RGB")
    W, H = im.size
    ar = w_mm / h_mm
    if W / H > ar:
        nw = int(H * ar); x0 = (W - nw) // 2; im = im.crop((x0, 0, x0 + nw, H))
    else:
        nh = int(W / ar); y0 = int((H - nh) * 0.4); im = im.crop((0, y0, W, y0 + nh))
    tw = int(w_mm / 25.4 * dpi)
    if im.size[0] > tw:
        im = im.resize((tw, int(tw / ar)), Image.LANCZOS)
    im.save(out, "JPEG", quality=88)
    return out


def tile_map(cd, x, y, active, tile=3.0, hl=None):
    """Kachelkarte DACH: jede Region ein Quadrat. active = Menge Regionscodes (dort typisch)."""
    for r in REGION_LISTE:
        cx, cy = r["kachel"]
        on = r["code"] in active
        col = LAND_COL[r["land"]] if on else "#E0E4E7"
        cd.rect(x + cx * tile, y + cy * tile, tile - 0.35, tile - 0.35, fill=col, r=0.5)


def silhouette(cd, x, y, w, h, sp, kurz=False):
    """Platzhalter-Bild: tonfarbener Hintergrund mit stilisiertem Baum."""
    col = C_DECK[sp["deck"]]
    cd.rect(x, y, w, h, fill="#E8F0E6")
    cd.rect(x, y + h * 0.78, w, h * 0.22, fill="#C5D8BF")
    cx = x + w / 2
    trunk = "#6D4C41"
    if sp["grp"] == "Nadel":
        cd.rect(cx - 1.2, y + h * 0.66, 2.4, h * 0.14, fill=trunk)
        for i, (wd, top) in enumerate(((w * 0.42, 0.12), (w * 0.34, 0.27), (w * 0.26, 0.42))):
            ty = y + h * top
            by = ty + h * 0.30
            c = cd.c; c.saveState(); c.setFillColor(hc(col))
            p = c.beginPath()
            p.moveTo(cd.X(cx), cd.Y(ty)); p.lineTo(cd.X(cx - wd / 2), cd.Y(by)); p.lineTo(cd.X(cx + wd / 2), cd.Y(by)); p.close()
            c.drawPath(p, fill=1, stroke=0); c.restoreState()
    else:
        cd.rect(cx - 1.5, y + h * 0.5, 3.0, h * 0.30, fill=trunk)
        cd.circle(cx, y + h * 0.36, h * 0.27, fill=col)
        cd.circle(cx - w * 0.14, y + h * 0.46, h * 0.19, fill=col)
        cd.circle(cx + w * 0.14, y + h * 0.46, h * 0.19, fill=col)
    if not kurz:
        cd.text(cx, y + h - 1.6, "Foto folgt · bilder/" + sp["id"] + ".jpg", "DVC", 3.6, "#78909C", "c")


def zeichne_bild(cd, sid, sp, x, y, w, h, radius=0, kurz=False):
    """Foto (zugeschnitten) oder Platzhalter, auf Rechteck zugeschnitten."""
    p = bild_zugeschnitten(sid, w, h)
    c = cd.c
    c.saveState()
    pth = c.beginPath()
    if radius:
        pth.roundRect(cd.X(x), cd.Y(y + h), w * mm, h * mm, radius * mm)
    else:
        pth.rect(cd.X(x), cd.Y(y + h), w * mm, h * mm)
    c.clipPath(pth, stroke=0, fill=0)
    if p:
        c.drawImage(p, cd.X(x), cd.Y(y + h), w * mm, h * mm)
    else:
        silhouette(cd, x, y, w, h, sp, kurz)
    c.restoreState()
    return p is not None

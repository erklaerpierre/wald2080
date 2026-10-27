# -*- coding: utf-8 -*-
"""BASISSATZ · Konstanten (gelten für alle Editionen)

Standortachsen (1-5):  W = Wasser (1 sehr trocken … 5 nass)
                       N = Nährstoffe (1 arm … 5 sehr reich)
                       T = Wärme (1 kalt/Hochlage … 5 sehr warm)
Resistenzen (1-5, höher = robuster): DÜ Dürre, ST Sturm/Schnee, KÄ Käfer/Insekten,
                       PI Pilze/Krankheiten, FR Frost, FE Feuer, VE Verbiss
Eigenschaften: PIO Pionier, SCH Schattenbaumart, BOD Bodenverbesserer, INV invasiv
"""
RES_KEYS = ["DÜ", "ST", "KÄ", "PI", "FR", "FE", "VE"]
RES_NAMES = {"DÜ": "Dürre", "ST": "Sturm/Schnee", "KÄ": "Käfer", "PI": "Pilze",
             "FR": "Frost", "FE": "Feuer", "VE": "Verbiss"}

DECKS = {
    "basis":   ("Basis",                    "Heimisch, etabliert & Züchtungen (DE)"),
    "nachbar": ("Erweiterung Nachbarländer", "AT, CH, FR, CZ, PL, NL, DK …"),
    "europa":  ("Erweiterung Europa",        "Mittelmeer, Balkan, Kaukasus"),
    "welt":    ("Erweiterung Welt",          "Nordamerika, Asien, Nordafrika …"),
}

# Klimastufe k: Wärme +k (max 5), Wasser −(k//2) (min 1)
def klima(W, T, k):
    return max(1, W - k // 2), min(5, T + k)

KLIMAPFAD_STANDARD = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3}   # Runde -> Klimastufe
JAHRE = {i: 2020 + 10 * i for i in range(1, 9)}  # 2030 … 2100

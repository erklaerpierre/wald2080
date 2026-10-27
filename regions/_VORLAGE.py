# -*- coding: utf-8 -*-
"""VORLAGE für eine neue Edition (Datei beginnt mit '_' und wird nicht geladen).
Kopieren nach regions/<land>/<kuerzel>.py, z. B. regions/de/xy.py, und anpassen.
Alles, was nur für diese Region gilt, steht in DIESER Datei: Kürzel, Farbe, Arten, Zuschlag, Standorte.
"""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="XY", land="DE", name="Beispielland", farbe="#33691E", kachel=(0, 0),
       arten=" ".join([KERN, AUE, GAST]),     # Baumarten-IDs aus core/arten.py
       zuschlag={},                            # z. B. {"DÜ": 1} = Dürreereignisse sind hier +1 stärker
       hinweis="Ein Satz zur Region für die Spielleitung.")

# ST(Name, Landschaft, Wasser, Nährstoffe, Wärme, Besonderheiten, Start-Baumart, Beschreibung)
ST("Beispiel-Standort", "Sand, flach", 2, 2, 3, {"FE": -1}, "waldkiefer", "Kurze Beschreibung für die Karte.")

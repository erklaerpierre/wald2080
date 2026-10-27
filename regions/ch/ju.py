# -*- coding: utf-8 -*-
"""Edition Jura (CH-JU) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="JU", land="CH", name="Jura", farbe="#004D40", kachel=(0, 6),
       arten=" ".join([KERN, AUE, BERG, WARM, GAST, "flaumeiche fr_ahorn mannaesche"]),
       zuschlag={"DÜ": 3, "KÄ": 3},
       hinweis="Karstgebirge im Nordwesten: Kalk, Dolinen, wenig Oberflächenwasser.")

ST('Faltenjura (Hochlage)', 'Kalk, Karst', 4, 3, 2, {'DÜ': -1}, 'tanne',
   'Wasser versickert im Karst – Tannen-Buchenwald.')
ST('Jurasüdfuss (Weinbauklima)', 'Kalk, warm', 2, 4, 4, {'DÜ': -1}, 'traubeneiche',
   'Warm und trocken am Seeufer.')
ST('Tafeljura', 'Kalk, Hügelland', 3, 4, 3, {}, 'buche',
   'Buchenwald auf Kalk.')
ST('Freiberge (Weidwald)', 'Kalk, rau', 3, 3, 2, {}, 'fichte',
   'Fichten-Weidwälder.')
ST('Jura-Schluchten (Steilhang)', 'Kalk, trocken', 1, 3, 4, {'DÜ': -1, 'FE': -1}, 'feldahorn',
   'Trockener Fels mit Flaumeichen und Ahornen.')
ST('Neuenburgersee-Ufer', 'Kalk, mild', 3, 4, 4, {}, 'stieleiche',
   'Milde Seeluft.')

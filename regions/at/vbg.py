# -*- coding: utf-8 -*-
"""Edition Vorarlberg (AT-VBG) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="VBG", land="AT", name="Vorarlberg", farbe="#880E4F", kachel=(2, 6),
       arten=" ".join([KERN, AUE, BERG, GAST, "zirbe latsche"]),
       zuschlag={"DÜ": -1, "FE": -1},
       hinweis="Viel Regen, steile Hänge: Bregenzerwald und Schutzwälder im Montafon.")

ST('Bregenzerwald (Bergmischwald)', 'Flysch, sehr feucht', 5, 3, 2, {'ST': -1}, 'fichte',
   'Hohe Niederschläge – Tannen-Fichten-Buchenwald.')
ST('Rheintal (Auwald)', 'Aue, Auelehm', 4, 4, 4, {'PI': -1}, 'esche',
   'Mild und warm am Bodensee.')
ST('Montafon / Walgau (Schutzwald)', 'Silikat/Kalk', 4, 3, 2, {'ST': -1}, 'fichte',
   'Schutzwald für Siedlungen.')
ST('Kleinwalsertal (Hochlage)', 'Kalk, hochalpin', 5, 2, 1, {'ST': -1}, 'fichte',
   'Nass, kalt und steil.')
ST('Vorarlberger Vorland', 'Moräne, Hügel', 4, 4, 3, {}, 'buche',
   'Buchen-Tannen-Wälder.')

# -*- coding: utf-8 -*-
"""Edition Wien (AT-WIE) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="WIE", land="AT", name="Wien", farbe="#AD1457", kachel=(5, 4),
       arten=" ".join([KERN, AUE, "mehlbeere elsbeere schwarzkiefer flaumeiche zerreiche silberpappel", "robinie"]),
       zuschlag={"DÜ": 2, "FE": 1},
       hinweis="Kleine Edition: Wienerwald, Lobau und warme Hänge am Stadtrand.")

ST('Wienerwald (Flysch)', 'Flysch, Hügelland', 3, 3, 4, {}, 'buche',
   'Buchenwald auf Lehm im Westen der Stadt.')
ST('Lobau (Donau-Auen)', 'Aue, Auelehm', 5, 5, 4, {'PI': -1}, 'esche',
   'Teil des Nationalparks Donau-Auen – Eschentriebsterben ist ein Problem.')
ST('Kahlenberg (warm, Löss)', 'Löss, Südhang', 2, 4, 4, {'DÜ': -1}, 'traubeneiche',
   'Eichen-Hainbuchenwälder an warmen Hängen.')
ST('Bisamberg (Trockenhang)', 'Löss/Kalk, trocken', 1, 4, 5, {'DÜ': -1, 'FE': -1}, 'schwarzkiefer',
   'Pannonisch geprägt – Schwarzkiefern auf trockenem Hang.')

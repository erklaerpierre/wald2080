# -*- coding: utf-8 -*-
"""Edition Burgenland (AT-BGL) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="BGL", land="AT", name="Burgenland", farbe="#D84315", kachel=(5, 5),
       arten=" ".join([KERN, AUE, WARM, GAST_WARM, "schwarzkiefer flaumeiche zerreiche silberpappel mannaesche silberlinde"]),
       zuschlag={},
       hinweis="Pannonisches Klima: heiß, trocken, windig – der Neusiedler See und die Eichenwälder.")

ST('Leithagebirge (Eichenwald)', 'Kalk, warm', 2, 4, 5, {}, 'traubeneiche',
   'Warm-trocken – Eichen- und Hainbuchenwald.')
ST('Seewinkel (Sand)', 'Sand, sehr warm', 1, 3, 5, {'DÜ': -1}, 'zerreiche',
   'Pannonischer Steppenrand mit Salzlacken.')
ST('Südburgenland (Hügelland)', 'Silikat, mild', 3, 2, 4, {}, 'traubeneiche',
   'Esskastanien und Eichen auf sauren Böden.')
ST('Rosaliengebirge', 'Gneis, kühler', 3, 3, 3, {}, 'buche',
   'Buchenwald in höherer Lage.')
ST('Parndorfer Platte (Windschutz)', 'Schotter, windig', 1, 3, 5, {'DÜ': -1}, 'robinie',
   'Offene Landschaft; Feldgehölze und Robinie.')

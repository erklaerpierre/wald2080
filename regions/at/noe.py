# -*- coding: utf-8 -*-
"""Edition Niederösterreich (AT-NOE) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="NOE", land="AT", name="Niederösterreich", farbe="#C62828", kachel=(4, 4),
       arten=" ".join([KERN, AUE, BERG, WARM, GAST_WARM, "schwarzkiefer flaumeiche zerreiche silberpappel mannaesche", "latsche zirbe"]),
       zuschlag={"DÜ": 1},
       hinweis="Größtes Bundesland: Waldviertel, Wienerwald, Kalkalpen und das trockene Weinviertel.")

ST('Waldviertel (Granit)', 'Granit, rau-kühl', 3, 2, 2, {}, 'fichte',
   'Kühl und regenarm – Fichtenforste auf armen Böden.')
ST('Wienerwald (Flysch)', 'Flysch, Hügelland', 3, 3, 3, {}, 'buche',
   'Buchenwald, 1000 Jahre Nutzung.')
ST('Weinviertel (Löss, trocken)', 'Löss, warm-trocken', 1, 5, 4, {'DÜ': -1}, 'traubeneiche',
   'Eines der trockensten Gebiete Österreichs.')
ST('Donau-Auen', 'Aue, Auelehm', 5, 5, 4, {'PI': -1}, 'esche',
   'Auwald an der Donau, Nationalpark.')
ST('Niederösterreichische Kalkalpen', 'Kalk, steil', 5, 3, 2, {'ST': -1}, 'fichte',
   'Schutzwälder gegen Lawinen und Muren.')
ST('Steinfeld (Wiener Becken)', 'Schotter, sehr trocken', 1, 3, 4, {'DÜ': -1, 'FE': -1}, 'schwarzkiefer',
   'Größter Schwarzkiefernwald Österreichs.')
ST('Mostviertel (Hügelland)', 'Lehm, Hügelland', 4, 4, 3, {}, 'fichte',
   'Obstbaumland mit vielen Fichtenforsten.')
ST('Thermenlinie (warm, Kalk)', 'Kalk, warm-trocken', 1, 4, 5, {'DÜ': -1}, 'flaumeiche',
   'Wärmste Ecke am Alpenostrand – Flaumeichenwälder.')

# -*- coding: utf-8 -*-
"""Edition Saarland (DE-SL) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="SL", land="DE", name="Saarland", farbe="#5D4037", kachel=(0, 5),
       arten=" ".join([KERN, AUE, "tanne eibe mehlbeere elsbeere esskastanie", GAST]),
       zuschlag={"DÜ": 3, "KÄ": 3},
       hinweis="Kleine Edition: Saarkohlenwald, Warndt und Muschelkalk – Eichen- und Buchenwälder.")

ST('Saarkohlenwald (Buche-Eiche)', 'Karbon-Sandstein', 3, 3, 4, {}, 'buche',
   'Alte Bergbau-Landschaft, heute Mischwald.')
ST('Warndt (Buntsandstein)', 'Sand, trocken', 2, 2, 4, {'FE': -1}, 'waldkiefer',
   'Größtes Waldgebiet des Saarlands, arme Sande.')
ST('Saargau (Muschelkalk)', 'Kalk, warm', 2, 4, 4, {}, 'traubeneiche',
   'Warm-trockene Kalkböden.')
ST('Hochwald / Schwarzwälder Hochwald', 'Quarzit, kühl', 4, 2, 2, {}, 'fichte',
   'Rauer Höhenzug mit Fichten und Buchen.')

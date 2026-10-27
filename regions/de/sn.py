# -*- coding: utf-8 -*-
"""Edition Sachsen (DE-SN) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="SN", land="DE", name="Sachsen", farbe="#00838F", kachel=(3, 2),
       arten=" ".join([KERN, AUE, BERG, SAND, MOOR, GAST, "robinie"]),
       zuschlag={"KÄ": 2, "FE": 2},
       hinweis="Erzgebirge, Lausitz und Elbtal: Rauchschäden-Geschichte und Fichtenwälder.")

ST('Erzgebirge (Kammlagen)', 'Gneis, kalt', 4, 2, 1, {'ST': -1}, 'fichte',
   'Rauchschäden prägten die Kämme; Fichten dominieren, Sturm und Borkenkäfer drohen.')
ST('Tharandter Wald', 'Gneis, mittlere Lage', 4, 3, 3, {}, 'fichte',
   'Forstliche Ausbildungsstätte seit 1811 – Geburtsstätte der Nachhaltigkeit.')
ST('Sächsische Schweiz', 'Sandstein, Schluchten', 3, 1, 3, {'FE': -1}, 'fichte',
   'Trockene Sandsteinfelsen; Brand und Käfer hinterließen kahle Flächen.')
ST('Lausitzer Heide & Teichland', 'Sand, trocken', 1, 1, 4, {'DÜ': -1, 'FE': -1}, 'waldkiefer',
   'Armer Sand mit Kiefernforst – Wärmeinsel.')
ST('Zittauer Gebirge', 'Sandstein, feucht', 4, 3, 2, {}, 'buche',
   'Buchenwald im Dreiländereck.')
ST('Leipziger Auwald', 'Aue, Auelehm', 5, 5, 4, {'PI': -1}, 'esche',
   'Größter Auwald Mitteleuropas im Stadtgebiet – Eschentriebsterben.')
ST('Dresdner Heide', 'Sand und Lehm', 2, 2, 4, {'FE': -1}, 'waldkiefer',
   'Stadtnaher Kiefernforst, trocken-warm.')
ST('Lösshügelland (Mulde)', 'Löss, fruchtbar', 2, 5, 4, {}, 'traubeneiche',
   'Fruchtbarer Boden, wenig Wald.')
ST('Vogtland', 'Schiefer, kühl', 4, 2, 2, {'ST': -1}, 'fichte',
   'Fichtenwälder auf armen Schieferböden.')

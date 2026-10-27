# -*- coding: utf-8 -*-
"""Edition Nordrhein-Westfalen (DE-NW) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="NW", land="DE", name="Nordrhein-Westfalen", farbe="#4527A0", kachel=(0, 3),
       arten=" ".join([KERN, AUE, BERG, SAND, GAST, "mehlbeere elsbeere"]),
       zuschlag={"KÄ": 2, "ST": 2},
       hinweis="Fichtenland Sauerland, Sandsenne, Rheinaue – NRW traf Kyrill und Käfer besonders hart.")

ST('Sauerland (Fichtenland)', 'Schiefer, kühl', 4, 2, 2, {'ST': -1}, 'fichte',
   'Kyrill 2007 und der Käfer ab 2018 haben große Fichtenwälder vernichtet.')
ST('Rothaargebirge (Hochlage)', 'Schiefer, Kamm', 5, 2, 1, {'ST': -1}, 'fichte',
   'Hoher Niederschlag, Wind – Fichtenreinbestände sind besonders anfällig.')
ST('Bergisches Land', 'Hügelland, Lehm', 4, 3, 3, {}, 'buche',
   'Mildes, feuchtes Klima – Buchen-Eichen-Wald.')
ST('Nordeifel (Hohes Venn)', 'Sandstein, feucht', 4, 2, 2, {}, 'buche',
   'Kühl und feucht; Fichtenbestände werden umgebaut.')
ST('Teutoburger Wald', 'Kalk, Hanglage', 3, 4, 3, {}, 'buche',
   'Kalkbuchenwälder am Höhenzug.')
ST('Weserbergland (NRW)', 'Kalk und Ton', 3, 3, 3, {}, 'buche',
   'Buchen-Eichen-Mischwälder auf Lehm.')
ST('Münsterland (Geest)', 'Sand, Lehm', 3, 2, 3, {}, 'stieleiche',
   'Eichenwälder auf sandigen Böden.')
ST('Senne (Heide)', 'Sand, Heide', 2, 1, 3, {'FE': -1}, 'waldkiefer',
   'Trockener Sand, Truppenübungsplatz-Landschaft.')
ST('Sophienhöhe (Rekultivierung Tagebau)', 'Rekultiviert, Löss', 2, 4, 4, {'DÜ': -1}, 'traubeneiche',
   'Neu aufgeforsteter Wald auf Tagebauland.')
ST('Rheinaue (Niederrhein)', 'Aue, Auelehm', 5, 5, 4, {'PI': -1}, 'stieleiche',
   'Weichholzaue am Rhein mit Pappeln und Weiden.')

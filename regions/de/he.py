# -*- coding: utf-8 -*-
"""Edition Hessen (DE-HE) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="HE", land="DE", name="Hessen", farbe="#00695C", kachel=(1, 3),
       arten=" ".join([KERN, AUE, BERG, WARM, GAST_WARM]),
       zuschlag={"KÄ": 3, "DÜ": 2},
       hinweis="Buchenland Hessen: Mittelgebirge, Rhein-Main-Ebene und Fichtenflächen nach Dürre und Käfer.")

ST('Taunus (Hochlage)', 'Quarzit, kühl', 4, 3, 2, {}, 'buche',
   'Kühle Hochlagen mit Buchenwald, in Teilen noch Fichte.')
ST('Vogelsberg (Basalt)', 'Basalt, feucht-kühl', 4, 4, 2, {}, 'buche',
   'Größtes Vulkangebiet Mitteleuropas – nährstoffreiche Basaltböden.')
ST('Odenwald (Hessen)', 'Buntsandstein', 3, 2, 3, {}, 'buche',
   'Saure, ärmere Böden unter Buchen-Eichen-Wald.')
ST('Spessart (Hessen)', 'Buntsandstein, Eichen', 3, 2, 3, {}, 'traubeneiche',
   'Berühmt für starke Eichen – Wertholz seit Jahrhunderten.')
ST('Reinhardswald / Weserbergland', 'Sandstein, Staunässe', 3, 2, 2, {'ST': -1}, 'buche',
   'Großes Waldgebiet mit Staunässeböden; Sturm legte viele Fichten.')
ST('Kellerwald (Buchenwald)', 'Grauwacke, Hanglage', 4, 3, 2, {}, 'buche',
   'Uraltbuchenwälder – UNESCO-Weltnaturerbe.')
ST('Hessisches Ried (Rheinebene)', 'Sand, Kiefernwald', 1, 2, 4, {'DÜ': -1, 'FE': -1}, 'waldkiefer',
   'Trocken-warme Sande am Oberrhein – absinkendes Grundwasser.')
ST('Wetterau (Löss)', 'Löss, mild', 2, 5, 4, {}, 'traubeneiche',
   'Fruchtbare Lössböden – kleine Waldflächen mit Eichen.')
ST('Lahn-Dill-Bergland (Fichtenland)', 'Schiefer, kühl', 4, 2, 2, {}, 'fichte',
   'Hier standen große Fichtenforste – nach Käferjahren sind viele Flächen kahl.')

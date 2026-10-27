# -*- coding: utf-8 -*-
"""Edition Niedersachsen (DE-NI) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="NI", land="DE", name="Niedersachsen", farbe="#558B2F", kachel=(1, 2),
       arten=" ".join([KERN, AUE, BERG, SAND, MOOR, GAST, "robinie"]),
       zuschlag={"ST": 1},
       hinweis="Harz, Heide, Weser und Küste: vom Fichtenberg bis zum Kiefernsand.")

ST('Harz (Hochlage)', 'Granit/Grauwacke, kühl', 4, 2, 1, {'ST': -1}, 'fichte',
   'Rau und windig – der Harz verlor nach 2018 riesige Fichtenflächen an den Borkenkäfer.')
ST('Solling (Buntsandstein)', 'Sandstein, kühl-feucht', 4, 2, 2, {}, 'buche',
   'Buchenwald auf sauren Böden, Fichten als Beimischung.')
ST('Weserbergland (Kalk)', 'Muschelkalk', 3, 4, 3, {}, 'buche',
   'Kalkbuchenwälder an Hanglagen – trocken auf Südhängen.')
ST('Lüneburger Heide (Geest)', 'Sand, Heide', 1, 1, 3, {'DÜ': -1, 'FE': -1}, 'waldkiefer',
   'Arme Sandböden mit Kiefernforsten – Brandgefahr.')
ST('Südheide (Kiefern-Eichen-Wald)', 'Sand, mäßig', 2, 2, 3, {'FE': -1}, 'waldkiefer',
   'Sandige Böden; hier gelingt Umbau zu Eichen-Kiefernmischwald.')
ST('Elbe-Aue (Hartholzaue)', 'Aue, Auelehm', 5, 5, 3, {'PI': -1}, 'esche',
   'Überflutungsauwald mit Eichen und Eschen.')
ST('Ostfriesische Geest', 'Geest, Küstennähe', 4, 2, 3, {'ST': -1}, 'stieleiche',
   'Küstenwind und nasse Sandböden.')
ST('Hannoversches Wendland', 'Sand und Löss', 2, 3, 3, {}, 'stieleiche',
   'Trocken-kontinentales Klima mit Eichen und Kiefern.')
ST('Hildesheimer Börde (Löss)', 'Löss, trocken', 2, 5, 4, {}, 'traubeneiche',
   'Sehr fruchtbare Böden, wenig Wald, warm.')

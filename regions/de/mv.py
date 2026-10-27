# -*- coding: utf-8 -*-
"""Edition Mecklenburg-Vorpommern (DE-MV) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="MV", land="DE", name="Mecklenburg-Vorpommern", farbe="#0277BD", kachel=(3, 0),
       arten=" ".join([KERN, SAND, MOOR, AUE, "laerche douglasie roteiche japanlaerche hybridlaerche"]),
       zuschlag={"ST": 3, "FE": 3},
       hinweis="Ostseeküste, Seenplatte und Sandböden: Buche am Meer und Kiefer im Binnenland.")

ST('Jasmund (Kreideküste)', 'Kreide, Steilküste', 4, 4, 3, {'ST': -1}, 'buche',
   'Buchenwälder auf Kreide – windexponiert, UNESCO-Weltnaturerbe.')
ST('Darß (Küstenwald)', 'Dünen und Sand', 3, 2, 3, {'ST': -1}, 'waldkiefer',
   'Windgeformter Küstenwald auf nährstoffarmem Sand.')
ST('Müritz-Region (Sander)', 'Sand, Seen', 2, 2, 3, {'FE': -1}, 'waldkiefer',
   'Kiefernforste auf sandigen Ebenen zwischen den Seen.')
ST('Mecklenburgische Seenplatte', 'Endmoräne, Lehm', 3, 4, 3, {}, 'buche',
   'Gute Moränenböden – Buchenwald mit Seen und Söllen.')
ST('Warnow-Niederung (Bruchwald)', 'Niedermoor', 5, 3, 3, {'PI': -1}, 'schwarzerle',
   'Nasser Erlenbruch – Wasserhaushalt entscheidet.')
ST('Ueckermünder Heide', 'Sand, trocken', 2, 1, 3, {'FE': -1}, 'waldkiefer',
   'Großes Kiefernforstgebiet auf armen Sanden.')
ST('Griese Gegend (Sander)', 'Sand, sehr trocken', 1, 1, 3, {'DÜ': -1}, 'waldkiefer',
   'Eine der trockensten und ärmsten Regionen des Landes.')
ST('Vorpommersche Lehmplatte', 'Lehm, mild', 3, 4, 3, {}, 'stieleiche',
   'Gute Böden, wenig Wald – Eichen und Buchen in Restwäldern.')

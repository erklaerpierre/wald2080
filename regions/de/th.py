# -*- coding: utf-8 -*-
"""Edition Thüringen (DE-TH) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="TH", land="DE", name="Thüringen", farbe="#2E7D32", kachel=(2, 3),
       arten=" ".join([KERN, AUE, BERG, WARM, GAST]),
       zuschlag={"KÄ": 3, "DÜ": 3},
       hinweis="Grünes Herz Deutschlands: Thüringer Wald, Hainich-Buchenwald und trockenes Becken.")

ST('Thüringer Wald (Kamm)', 'Porphyr/Granit, kalt', 4, 2, 1, {'ST': -1}, 'fichte',
   'Fichtenwälder auf den Kammlagen – Sturm- und Käferflächen.')
ST('Thüringer Wald (Mittelhang)', 'Gneis/Schiefer', 4, 2, 2, {}, 'fichte',
   'Fichte und Buche im Wechsel.')
ST('Hainich (Muschelkalk)', 'Kalk, Buchenwald', 3, 4, 3, {}, 'buche',
   'UNESCO-Weltnaturerbe – Buchenurwald auf Kalk.')
ST('Thüringische Rhön', 'Basalt, kühl-feucht', 4, 4, 2, {}, 'buche',
   'Nährstoffreicher Basalt.')
ST('Thüringer Becken (Löss)', 'Löss, trocken', 1, 5, 4, {'DÜ': -1}, 'traubeneiche',
   'Regenschatten – eines der trockensten Gebiete Deutschlands.')
ST('Frankenwald / Schiefergebirge', 'Schiefer, rau', 4, 2, 2, {'ST': -1}, 'fichte',
   'Fichtenforste auf Schiefer; sturmanfällig.')
ST('Saaletal (Muschelkalk-Steilhänge)', 'Kalk, Südhang', 1, 4, 4, {'DÜ': -1, 'FE': -1}, 'traubeneiche',
   'Heiße Kalkhänge mit Trockenrasen.')
ST('Kyffhäuser / Südharz (Gips)', 'Gips, trocken', 2, 4, 4, {}, 'traubeneiche',
   'Gipskarst, warm-trocken, sehr artenreich.')

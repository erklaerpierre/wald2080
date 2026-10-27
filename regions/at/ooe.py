# -*- coding: utf-8 -*-
"""Edition Oberösterreich (AT-OOE) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="OOE", land="AT", name="Oberösterreich", farbe="#BF5B04", kachel=(3, 4),
       arten=" ".join([KERN, AUE, BERG, WARM, GAST, "zirbe latsche"]),
       zuschlag={"KÄ": 1, "ST": 1},
       hinweis="Mühlviertel, Innviertel, Salzkammergut und die Donau – viel Fichte, viel Sturm.")

ST('Mühlviertel (Granit)', 'Granit, rau', 3, 2, 2, {}, 'fichte',
   'Kühl und windreich, arme Böden.')
ST('Hausruck & Innviertel', 'Tertiär, Tonböden', 4, 3, 3, {}, 'fichte',
   'Fichtenforste auf schweren Böden – Staunässe.')
ST('Salzkammergut (Kalkalpen)', 'Kalk, Bergmischwald', 5, 3, 2, {'ST': -1}, 'fichte',
   'Viel Niederschlag; Schutzwald.')
ST('Eisenwurzen (Voralpen)', 'Kalk/Flysch', 4, 3, 2, {}, 'fichte',
   'Berühmt für Tannen-Buchen-Mischwald.')
ST('Traun-Enns-Platte (Schotter)', 'Schotter, trocken', 2, 3, 4, {'DÜ': -1}, 'fichte',
   'Durchlässig; Trockenstress für Fichten.')
ST('Donau-Auen (Eferdinger Becken)', 'Aue, Auelehm', 5, 5, 4, {'PI': -1}, 'esche',
   'Auwald, nährstoffreich.')
ST('Kobernaußerwald', 'Tertiär, Buchenwald', 4, 3, 3, {}, 'buche',
   'Großes zusammenhängendes Waldgebiet.')

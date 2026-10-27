# -*- coding: utf-8 -*-
"""Edition Wallis (CH-WAL) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="WAL", land="CH", name="Wallis", farbe="#BF360C", kachel=(0, 7),
       arten=" ".join([HOCH, ALPIN, "waldkiefer schwarzkiefer flaumeiche mannaesche hopfenbuche fr_ahorn esskastanie mehlbeere elsbeere speierling traubeneiche feldahorn buche tanne sommerlinde", GAST]),
       zuschlag={"DÜ": 2, "FE": 1},
       hinweis="Trockenstes Tal der Schweiz: Rhone-Föhn, Föhrenwälder und Lärchen-Arvenwälder.")

ST('Rhonetal (Föhrenwald, Pfynwald)', 'Schotter, extrem trocken', 1, 2, 4, {'DÜ': -1, 'FE': -1}, 'waldkiefer',
   'Waldföhren sterben schon heute durch Dürre – Eichen rücken nach.')
ST('Walliser Seitentäler (Lärche)', 'Silikat, kontinental', 2, 3, 2, {}, 'laerche',
   'Lärchenwiesen und -wälder.')
ST('Arven-Lärchenwald (Hochlage)', 'Silikat, subalpin', 2, 2, 1, {}, 'zirbe',
   'Aletsch-Gebiet.')
ST('Unterwallis / Chablais', 'Aue, Kalk', 4, 4, 4, {'PI': -1}, 'grauerle',
   'Auwälder am Genfersee.')
ST('Oberwallis (Schutzwald)', 'Silikat, steil', 2, 2, 2, {'ST': -1}, 'laerche',
   'Schutzwald oberhalb der Dörfer.')

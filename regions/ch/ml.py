# -*- coding: utf-8 -*-
"""Edition Mittelland (CH-ML) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="ML", land="CH", name="Mittelland", farbe="#1B5E20", kachel=(1, 6),
       arten=" ".join([KERN, AUE, BERG, WARM, GAST, "silberpappel"]),
       zuschlag={},
       hinweis="Dichtbesiedelt: Buchen- und Fichtenwälder auf Molasse und Moränen.")

ST('Berner Hügelland', 'Molasse, Moräne', 4, 4, 3, {'ST': -1}, 'fichte',
   'Fichtenforste; Lothar 1999 traf hier hart.')
ST('Zürcher Molasse (Buchenwald)', 'Molasse, Lehm', 4, 4, 3, {}, 'buche',
   'Buchenwald.')
ST('Aare-Auen', 'Aue, Auelehm', 5, 5, 4, {'PI': -1}, 'esche',
   'Auenwald.')
ST('Seeland / Reussebene', 'Ebene, Lehm', 3, 4, 4, {}, 'stieleiche',
   'Eichenwald im Tiefland.')
ST('Napf & Emmental (Nagelfluh)', 'Nagelfluh, steil', 5, 3, 2, {'ST': -1}, 'fichte',
   'Steile Hänge mit Fichtenwald.')
ST('Thurgau / Hörnli-Bergland', 'Molasse, Hügel', 4, 3, 3, {}, 'fichte',
   'Fichten und Buchen.')
ST('Genferseeraum', 'Moräne, mild', 3, 4, 4, {}, 'traubeneiche',
   'Milde Winter, trockene Sommer.')

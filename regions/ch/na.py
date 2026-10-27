# -*- coding: utf-8 -*-
"""Edition Voralpen & Nordalpen (CH-NA) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="NA", land="CH", name="Voralpen & Nordalpen", farbe="#0D47A1", kachel=(1, 7),
       arten=" ".join([KERN, BERG, HOCH, AUE, GAST, "zirbe spirke"]),
       zuschlag={"DÜ": -3, "FE": -2},
       hinweis="Hoher Niederschlag, steile Hänge, Schutzwald – von Entlebuch bis zum Säntis.")

ST('Voralpen (Bergmischwald)', 'Flysch, feucht', 5, 3, 2, {'ST': -1}, 'fichte',
   'Fichte, Tanne und Buche mischen.')
ST('Urner & Glarner Schutzwald', 'Kalk, steil', 5, 3, 1, {'ST': -1}, 'fichte',
   'Lawinenschutz für Täler und Strassen.')
ST('Berner Oberland (Bergwald)', 'Kalk/Silikat', 4, 3, 2, {}, 'fichte',
   'Mischwald und Weide.')
ST('Rigi & Pilatus', 'Kalk, Hänge', 5, 4, 2, {}, 'buche',
   'Bucheneben und Tannen.')
ST('Appenzell & Säntis', 'Kalk, nass', 5, 3, 2, {}, 'fichte',
   'Nass, windig, viel Schnee.')
ST('Entlebuch (Hochmoorwald)', 'Moor, Hochmoor', 5, 2, 2, {'PI': -1}, 'spirke',
   'UNESCO-Biosphäre – Moorwälder.')

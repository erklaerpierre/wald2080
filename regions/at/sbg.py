# -*- coding: utf-8 -*-
"""Edition Salzburg (AT-SBG) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="SBG", land="AT", name="Salzburg", farbe="#6D4C41", kachel=(3, 5),
       arten=" ".join([KERN, AUE, BERG, GAST, "zirbe latsche"]),
       zuschlag={"DÜ": -1},
       hinweis="Hohe Tauern, Pinzgau und Flachgau – Schutzwald und Schneebruch.")

ST('Hohe Tauern (Zirbe & Lärche)', 'Silikat, subalpin', 3, 2, 1, {}, 'zirbe',
   'Zirbelkiefer und Lärche an der Waldgrenze.')
ST('Pinzgau (Schutzwald)', 'Schiefer, steil', 4, 3, 2, {'ST': -1}, 'fichte',
   'Lawinenschutzwald.')
ST('Pongau (Kalkalpen)', 'Kalk, steil', 5, 3, 2, {'ST': -1}, 'fichte',
   'Steile Hänge, Schneedruck.')
ST('Lungau (kontinental)', 'Silikat, kalt-trocken', 2, 2, 1, {}, 'laerche',
   'Kalt, sonnenreich und trocken – Lärchen-Zirben-Wälder.')
ST('Flachgau (Alpenvorland)', 'Moräne, mild', 4, 4, 3, {}, 'fichte',
   'Nährstoffreiche Böden, viel Fichte.')
ST('Salzachauen', 'Aue, Auelehm', 5, 5, 3, {'PI': -1}, 'grauerle',
   'Grauerlen-Auwald.')

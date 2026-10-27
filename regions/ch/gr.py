# -*- coding: utf-8 -*-
"""Edition Graubünden (CH-GR) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="GR", land="CH", name="Graubünden", farbe="#4A148C", kachel=(2, 7),
       arten=" ".join([HOCH, ALPIN, KERN, BERG, "waldkiefer schwarzkiefer spirke mehlbeere flaumeiche hopfenbuche", GAST]),
       zuschlag={"DÜ": 1, "ST": 1},
       hinweis="Größter Kanton: Engadin, Rheintal, viele klimatische Kammern – Arven bis Föhn-Eichen.")

ST('Engadin (Arven-Lärchen)', 'Silikat, kontinental', 2, 2, 1, {}, 'zirbe',
   'Kalt, sonnig und trocken.')
ST('Unterengadin (inneralpin trocken)', 'Silikat/Dolomit', 1, 3, 2, {'DÜ': -1}, 'waldkiefer',
   'Eines der trockensten Täler der Alpen.')
ST('Davos & Prättigau (Schutzwald)', 'Silikat, steil', 3, 2, 1, {'ST': -1}, 'fichte',
   'Lawinenschutz.')
ST('Surselva (Bergwald)', 'Silikat/Kalk', 4, 3, 2, {'ST': -1}, 'fichte',
   'Bergsturzgebiet; Flimser Bergsturz.')
ST('Domleschg (Föhnlage)', 'Schotter, warm', 1, 4, 4, {'DÜ': -1, 'FE': -1}, 'waldkiefer',
   'Föhn, warm und trocken.')
ST('Bündner Rheintal', 'Aue, Schotter', 3, 4, 3, {}, 'fichte',
   'Föhn-Tal mit Fichte, Buche, Eiche.')

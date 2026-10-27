# -*- coding: utf-8 -*-
"""Edition Sachsen-Anhalt (DE-SA) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="SA", land="DE", name="Sachsen-Anhalt", farbe="#827717", kachel=(2, 2),
       arten=" ".join([KERN, AUE, SAND, BERG, "elsbeere mehlbeere speierling", GAST_WARM]),
       zuschlag={"DÜ": 3, "FE": 2},
       hinweis="Harz im Süden, trockene Börde in der Mitte und Elbe-Aue – trocken und kontinental.")

ST('Harz (Brocken-Hochlage)', 'Granit, extrem rau', 5, 2, 1, {'ST': -1}, 'fichte',
   'Fichtenwälder wurden durch den Käfer großflächig vernichtet – hier läuft Waldumbau im Eiltempo.')
ST('Harzvorland', 'Kalk und Ton', 3, 3, 3, {}, 'buche',
   'Kalkbuchenwälder, trockener als der Hochharz.')
ST('Fläming (Sachsen-Anhalt)', 'Sand und Moräne', 2, 2, 3, {'FE': -1}, 'waldkiefer',
   'Kiefernforste auf Sandböden.')
ST('Dübener Heide', 'Sand, Heide', 2, 2, 3, {'FE': -1}, 'waldkiefer',
   'Trocken und arm – Kiefer, Eiche und Birke.')
ST('Mittelelbe-Aue (Dessau-Wörlitz)', 'Aue, Auelehm', 5, 5, 4, {'PI': -1}, 'stieleiche',
   'Gartenreich und Auwald – Eichen, Ulmen, Eschen.')
ST('Magdeburger Börde (Schwarzerde)', 'Löss, trocken', 1, 5, 4, {'DÜ': -1}, 'traubeneiche',
   'Eine der trockensten und fruchtbarsten Regionen – kaum Wald.')
ST('Altmark (Sand)', 'Sand, kontinental', 2, 2, 3, {'FE': -1}, 'waldkiefer',
   'Trocken-kontinental, Kiefernforst auf armen Böden.')
ST('Saale-Unstrut (Kalk, warm)', 'Muschelkalk, Südhang', 1, 4, 4, {'DÜ': -1}, 'traubeneiche',
   'Weinbaugebiet – warm, trocken, Elsbeere und Trauben-Eiche.')

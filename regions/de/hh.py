# -*- coding: utf-8 -*-
"""Edition Hamburg (DE-HH) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="HH", land="DE", name="Hamburg", farbe="#C62828", kachel=(2, 1),
       arten=" ".join([KERN, "moorbirke schwarzerle silberweide flatterulme", "douglasie roteiche japanlaerche hybridlaerche"]),
       zuschlag={},
       hinweis="Kleine Edition: Stadtwälder auf Geest und Moor, Marsch an der Elbe.")

ST('Duvenstedter Brook (Bruchwald)', 'Moor, Bruchwald', 5, 2, 3, {'PI': -1}, 'moorbirke',
   'Nass und nährstoffarm – Moorbirke und Erle prägen den Brook.')
ST('Harburger Berge (Geest)', 'Sand, Endmoräne', 3, 2, 3, {}, 'buche',
   'Buchenwald auf Endmoräne mit sandigen Böden.')
ST('Klövensteen (Nadel-Mischwald)', 'Geest, Forst', 3, 2, 3, {}, 'fichte',
   'Alte Nadelholzforste, die zu Mischwald umgebaut werden.')
ST('Boberger Niederung (Dünen)', 'Dünensand, trocken', 2, 1, 3, {'FE': -1}, 'waldkiefer',
   'Binnendünen mit Kiefern und Birken – trocken und brandgefährdet.')

# -*- coding: utf-8 -*-
"""Edition Südschweiz (Tessin) (CH-TI) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="TI", land="CH", name="Südschweiz (Tessin)", farbe="#01579B", kachel=(1, 8),
       arten=" ".join([KERN, WARM, GAST_WARM, "tanne eibe laerche fichte grauerle", "mannaesche hopfenbuche flaumeiche fr_ahorn zerreiche silberlinde", "buche"]),
       zuschlag={"FE": 2, "ST": 2},
       hinweis="Südalpen: warm und niederschlagsreich, Kastanien- und Buchenwälder.")

ST('Kastanienselven', 'Silikat, warm-feucht', 4, 3, 5, {}, 'esskastanie',
   'Alte Kastanienkulturen, Rindenkrebs.')
ST('Südalpen-Buchenwald', 'Silikat, feucht', 5, 3, 3, {}, 'buche',
   'Nass und kühl in der Höhe.')
ST('Leventina / Maggiatal', 'Gneis, steil', 4, 2, 2, {'ST': -1}, 'fichte',
   'Lawinenschutz.')
ST('Luganer Hügel (Hopfenbuche)', 'Kalk, warm', 3, 3, 5, {}, 'hopfenbuche',
   'Südalpine Trockenheits-Spezialisten.')
ST('Mendrisiotto (Tiefland)', 'Moräne, warm', 3, 3, 5, {}, 'traubeneiche',
   'Wärmste Region der Schweiz.')
ST('Misox (Südbünden)', 'Gneis, steil', 3, 3, 4, {}, 'esskastanie',
   'Kastanien und Buchen.')

# -*- coding: utf-8 -*-
"""Edition Brandenburg (DE-BB) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="BB", land="DE", name="Brandenburg", farbe="#8D6E00", kachel=(3, 1),
       arten=" ".join([SAND, MOOR, AUE, "buche hainbuche winterlinde spitzahorn feldahorn vogelkirsche esche fichte laerche", GAST, "robinie"]),
       zuschlag={"DÜ": 3, "FE": 3},
       hinweis="Sandböden, wenig Niederschlag und viele Kiefernforste – Dürre und Feuer sind hier besonders gefährlich.")

ST('Schorfheide (Sander)', 'Nordbrandenburg, Sand', 1, 1, 3, {'DÜ': -1, 'FE': -1}, 'waldkiefer',
   'Sehr trockener, armer Sand – typischer Kiefernwald mit hoher Brandgefahr.')
ST('Märkische Heide', 'Sandrücken', 2, 2, 3, {'FE': -1}, 'waldkiefer',
   'Arme Sande – Kiefern prägen die Landschaft, Waldbrände sind häufig.')
ST('Fläming (Endmoräne)', 'Hügelland, Lehm-Sand', 2, 3, 3, {}, 'waldkiefer',
   'Hügelig, besser versorgt als die Heiden – hier sind Mischwälder möglich.')
ST('Niederlausitz (Bergbaufolge)', 'Kippenboden', 1, 1, 4, {'DÜ': -1}, 'roteiche',
   'Rekultivierte Tagebaukippe: nährstoffarm, sauer, extrem trocken.')
ST('Lausitzer Heide', 'Sandiger Heideboden', 1, 1, 4, {'FE': -1}, 'waldkiefer',
   'Warm und trocken – Kiefer, Birke und Eiche halten durch.')
ST('Spreewald (Erlenbruch)', 'Niedermoor, Fließe', 5, 4, 3, {'PI': -1, 'FE': 1}, 'schwarzerle',
   'Nass und nährstoffreich. Brandgefahr ist gering, Pilze sind häufiger.')
ST('Oderbruch / Odertal', 'Aue, Hochwasser', 5, 5, 4, {'PI': -1}, 'esche',
   'Wiederkehrende Überflutung, nährstoffreich – Auwald-Standort.')
ST('Uckermark (Jungmoräne)', 'Lehm, Hügelland', 3, 4, 3, {}, 'buche',
   'Gute Böden, mäßig trocken – klassischer Buchenstandort.')
ST('Barnim / Urstromtal', 'Talsand', 2, 2, 3, {'FE': -1}, 'waldkiefer',
   'Trockener Talsand nahe Berlin – hohe Waldbrandgefahr.')
ST('Havelländisches Luch', 'Niedermoor', 5, 3, 3, {'PI': -1}, 'moorbirke',
   'Nasse Moorböden – Wasserhaushalt entscheidet über alles.')
ST('Elbe-Elster (Sandlöss)', 'Sandlöss, warm-trocken', 2, 3, 4, {'DÜ': -1}, 'waldkiefer',
   'Warm und niederschlagsarm – eine der trockensten Ecken Deutschlands.')
ST('Märkische Schweiz', 'Hügelland, Lehm', 3, 4, 3, {}, 'douglasie',
   'Wellige Endmoräne mit guten Böden – hier wachsen Buchen und Douglasien.')

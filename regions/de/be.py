# -*- coding: utf-8 -*-
"""Edition Berlin (DE-BE) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="BE", land="DE", name="Berlin", farbe="#AD1457", kachel=(4, 1),
       arten=" ".join([SAND, AUE, "buche hainbuche winterlinde spitzahorn vogelkirsche esche", "douglasie roteiche robinie hybridlaerche"]),
       zuschlag={"DÜ": 3, "FE": 3},
       hinweis="Kleine Edition: Der Berliner Stadtwald mit Sand, Seen und viel Besucherdruck.")

ST('Grunewald (Kiefernforst)', 'Sand am Stadtrand', 1, 1, 4, {'DÜ': -1, 'FE': -1}, 'waldkiefer',
   'Trockener Sand, viele Besucher und hohe Waldbrandgefahr direkt an der Großstadt.')
ST('Tegeler Forst', 'Sand, Eichen-Kiefern-Wald', 2, 2, 4, {'FE': -1}, 'waldkiefer',
   'Nährstoffarme Sande mit Eichen – ein Umbau von Kiefernreinbeständen läuft.')
ST('Müggelspree-Aue (Köpenick)', 'Aue, Niedermoor', 5, 4, 4, {'PI': -1}, 'stieleiche',
   'Hoher Grundwasserstand, nährstoffreich – Eichen-Hainbuchen- und Erlenwälder.')
ST('Berliner Buchenwald (Moränenhänge)', 'Lehm, Hügel', 3, 3, 4, {}, 'buche',
   'Mäßig trockene Moränenhänge – Buche leidet unter der Stadtwärme.')

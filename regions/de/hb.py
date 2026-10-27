# -*- coding: utf-8 -*-
"""Edition Bremen (DE-HB) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="HB", land="DE", name="Bremen", farbe="#B71C1C", kachel=(1, 1),
       arten=" ".join([AUE, "stieleiche hainbuche buche esche sandbirke eberesche winterlinde moorbirke waldkiefer spitzahorn", "douglasie roteiche hybridlaerche"]),
       zuschlag={"ST": 1},
       hinweis="Kleine Edition: wenig Wald, viel Aue, Moor und Geest – Stadtstaat am Unterlauf von Weser.")

ST('Blockland (Niedermoor)', 'Moor, Grünland-Wald', 5, 3, 3, {'PI': -1}, 'schwarzerle',
   'Nasse Moorböden – Erlenbruch und Moorbirke.')
ST('Bürgerpark & Stadtwald (Geest)', 'Sand, Parkwald', 3, 2, 3, {}, 'stieleiche',
   'Sandige Geest mit alten Eichen und Buchen mitten in der Stadt.')
ST('Weser-Aue (Hartholzaue)', 'Aue, Auelehm', 5, 5, 3, {'PI': -1}, 'esche',
   'Zeitweise überflutet und nährstoffreich – Eschentriebsterben ist hier ein Thema.')

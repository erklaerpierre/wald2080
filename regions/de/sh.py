# -*- coding: utf-8 -*-
"""Edition Schleswig-Holstein (DE-SH) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="SH", land="DE", name="Schleswig-Holstein", farbe="#1565C0", kachel=(2, 0),
       arten=" ".join([KERN, AUE, MOOR, SAND, GAST]),
       zuschlag={"ST": 1, "FE": 1},
       hinweis="Zwischen den Meeren: Buchenwald im Osten, Geest und Moor in der Mitte, Marsch im Westen.")

ST('Östliches Hügelland (Jungmoräne)', 'Lehm, Moränen', 3, 4, 3, {}, 'buche',
   'Die klassische Buchenlandschaft Schleswig-Holsteins.')
ST('Sachsenwald / Lauenburg', 'Sand und Lehm', 3, 3, 3, {}, 'buche',
   'Größtes Waldgebiet des Landes, Mischwald.')
ST('Geest (Sand)', 'Sand, nährstoffarm', 3, 2, 3, {'ST': -1}, 'stieleiche',
   'Ärmer, windreich – Eichen und Kiefern.')
ST('Küstenwald (Wind & Salz)', 'Dünen, Sand', 3, 2, 3, {'ST': -1}, 'waldkiefer',
   'Windgeformte Küstenwälder.')
ST('Moore der Mittelholsteinischen Geest', 'Hochmoor, Niedermoor', 5, 3, 3, {'PI': -1}, 'moorbirke',
   'Nasse Moorböden – Wasserhaushalt entscheidet.')
ST('Elbmarsch (Aue)', 'Marsch, Aue', 5, 5, 3, {'PI': -1}, 'esche',
   'Weichholz- und Hartholzaue an der Unterelbe.')

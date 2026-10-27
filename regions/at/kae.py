# -*- coding: utf-8 -*-
"""Edition Kärnten (AT-KAE) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="KAE", land="AT", name="Kärnten", farbe="#00796B", kachel=(4, 6),
       arten=" ".join([KERN, AUE, BERG, WARM, GAST, "zirbe latsche schwarzkiefer mannaesche"]),
       zuschlag={},
       hinweis="Südalpen-Nähe: kontinentale Täler, Nockberge und Karawanken.")

ST('Karawanken (Kalk, Schutzwald)', 'Kalk, steil', 4, 3, 2, {'ST': -1}, 'fichte',
   'Rau und steil mit wichtigem Schutzwald.')
ST('Nockberge (Zirbe)', 'Silikat, subalpin', 3, 2, 1, {}, 'zirbe',
   'Zirben und Latschen an der Waldgrenze.')
ST('Gailtal & Lesachtal', 'Kalk/Schiefer', 5, 3, 2, {'ST': -1}, 'fichte',
   'Viel Niederschlag – Südstau; Vaia-Sturm 2018 zerstörte hier Wälder.')
ST('Klagenfurter Becken (Moräne)', 'Moräne, mild', 3, 3, 3, {}, 'fichte',
   'Fichte und Kiefer in warmer Beckenlage.')
ST('Lavanttal (warm)', 'Silikat, geschützt', 3, 3, 4, {}, 'buche',
   'Mildes Klima, Buchen-Tannen-Wald.')
ST('Drautal (Auwald)', 'Aue, Auelehm', 5, 4, 3, {'PI': -1}, 'grauerle',
   'Auwald mit Grauerlen am Alpenfluss.')
ST('Koralpe', 'Kristallin, rau', 3, 2, 2, {}, 'fichte',
   'Fichtenwald auf sauren Kristallinböden.')

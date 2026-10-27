# -*- coding: utf-8 -*-
"""Edition Steiermark (AT-STM) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="STM", land="AT", name="Steiermark", farbe="#2E7D32", kachel=(4, 5),
       arten=" ".join([KERN, AUE, BERG, WARM, GAST_WARM, "zirbe latsche schwarzkiefer"]),
       zuschlag={},
       hinweis="Das „grüne Herz“ Österreichs: höchster Waldanteil, Alpen bis Weinland.")

ST('Hochschwab & Gesäuse (Schutzwald)', 'Kalk, steil', 5, 3, 1, {'ST': -1}, 'fichte',
   'Schutzwald oberhalb der Täler.')
ST('Zirbitzkogel (Hochlage)', 'Silikat, subalpin', 3, 2, 1, {}, 'zirbe',
   'Zirbelkiefern bis zur Waldgrenze.')
ST('Obersteiermark (Nadelwald)', 'Silikat, rau', 4, 2, 2, {}, 'fichte',
   'Fichtenforste – Käfergefahr bei Wärme.')
ST('Oststeirisches Hügelland', 'Lehm, mild', 3, 4, 4, {}, 'fichte',
   'Warm, aber Fichtenanbau auf Standorten, die zu warm werden.')
ST('Weststeirisches Hügelland (Kastanie)', 'Silikat, warm', 4, 3, 4, {}, 'buche',
   'Buchen, Eichen und Esskastanien.')
ST('Südsteirisches Weinland', 'Lehm/Schotter, warm', 3, 4, 5, {}, 'traubeneiche',
   'Warm und mild – Eichen und Kastanien.')
ST('Murauen', 'Aue, Auelehm', 5, 5, 4, {'PI': -1}, 'esche',
   'Auwald mit Pilzdruck.')

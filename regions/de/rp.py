# -*- coding: utf-8 -*-
"""Edition Rheinland-Pfalz (DE-RP) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="RP", land="DE", name="Rheinland-Pfalz", farbe="#BF360C", kachel=(0, 4),
       arten=" ".join([KERN, AUE, BERG, WARM, GAST_WARM]),
       zuschlag={"DÜ": 3, "FE": 3},
       hinweis="Waldreichstes Bundesland: Pfälzerwald, Hunsrück, Eifel, Mosel und warme Rheinebene.")

ST('Pfälzerwald (Buntsandstein)', 'Sand, arm', 3, 1, 3, {'FE': -1}, 'waldkiefer',
   'Größtes zusammenhängendes Waldgebiet Deutschlands – arme Böden, Kiefer und Buche.')
ST('Hunsrück', 'Schiefer, Hochfläche', 4, 2, 2, {}, 'fichte',
   'Fichten und Buchen; große Käferschäden.')
ST('Vulkaneifel', 'Vulkangestein, kühl', 4, 3, 2, {}, 'buche',
   'Maare und vulkanische Böden – Buchenwald.')
ST('Westerwald', 'Basalt/Ton, feucht', 4, 3, 2, {}, 'fichte',
   'Rau und niederschlagsreich; starker Fichtenanbau.')
ST('Rheinhessen (Löss, warm)', 'Löss, trocken-warm', 1, 5, 5, {'DÜ': -1}, 'traubeneiche',
   'Weinbauklima – Eichen und Elsbeere statt Buche.')
ST('Mosel-Steillagen', 'Schiefer, Südhang', 1, 3, 5, {'DÜ': -1, 'FE': -1}, 'traubeneiche',
   'Sonnenexponierte Steilhänge – trocken und brandgefährdet.')
ST('Nahe / Soonwald', 'Quarzit, Eichen', 3, 2, 3, {}, 'traubeneiche',
   'Eichen-Buchen-Wälder – Wertholz aus dem Soonwald.')
ST('Pfälzer Rheinauen', 'Aue, Auelehm', 5, 5, 4, {'PI': -1}, 'esche',
   'Auenwald am Oberrhein – Pilzdruck.')
ST('Haardtrand (Esskastanie)', 'Sandstein, mild', 2, 3, 5, {}, 'traubeneiche',
   'Wärmstes Klima des Landes – Esskastanie wächst hier von selbst.')

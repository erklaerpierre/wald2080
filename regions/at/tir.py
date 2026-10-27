# -*- coding: utf-8 -*-
"""Edition Tirol (AT-TIR) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="TIR", land="AT", name="Tirol", farbe="#B71C1C", kachel=(3, 6),
       arten=" ".join([KERN, AUE, BERG, GAST, "zirbe latsche spirke schwarzkiefer"]),
       zuschlag={},
       hinweis="Hochgebirge: Schutzwald ist hier überlebenswichtig, Inneralpentäler sind trocken.")

ST('Zentralalpen (Zirbe-Lärche)', 'Silikat, hochalpin', 2, 2, 1, {}, 'zirbe',
   'Zirben- und Lärchenwald an der Waldgrenze.')
ST('Karwendel / Nordkette (Schutzwald)', 'Kalk, steil', 5, 3, 1, {'ST': -1}, 'fichte',
   'Bergmischwald und Lawinenschutz.')
ST('Inntal (Föhrenwälder)', 'Schotter/Dolomit, trocken', 1, 3, 3, {'DÜ': -1, 'FE': -1}, 'waldkiefer',
   'Inneralpin trocken – Waldkiefer und Schwarzkiefer.')
ST('Osttirol (Lärchen-Fichtenwald)', 'Silikat, rau', 3, 2, 2, {}, 'laerche',
   'Kontinental geprägt, lärchenreich.')
ST('Unterinntal (Mischwald)', 'Kalk/Schiefer', 4, 3, 3, {}, 'fichte',
   'Warmes Tal, Fichtenanbau.')
ST('Kaisergebirge (Bergmischwald)', 'Kalk', 5, 3, 2, {}, 'fichte',
   'Tannen-Fichten-Buchenwald.')
ST('Zillertal (Bergwald)', 'Schiefer, steil', 4, 2, 2, {'ST': -1}, 'fichte',
   'Fichtenwald, Lawinenstriche.')

# -*- coding: utf-8 -*-
"""Edition Baden-Württemberg (DE-BW) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="BW", land="DE", name="Baden-Württemberg", farbe="#33691E", kachel=(1, 4),
       arten=" ".join([KERN, AUE, BERG, WARM, GAST_WARM]),
       zuschlag={},
       hinweis="Vom Hochschwarzwald bis zum Kaiserstuhl – sehr unterschiedliche Standorte auf kleinem Raum.")

ST('Schwarzwald-Hochlage', 'Feldberg-Region, Podsol', 4, 2, 1, {'ST': -1}, 'fichte',
   'Kühl, schneereich und sturmexponiert. Saure, flachgründige Böden.')
ST('Nordschwarzwald (Buntsandstein)', 'Saure Sandsteinböden', 3, 1, 2, {}, 'fichte',
   'Sehr nährstoffarm und sauer – nur genügsame Arten kommen zurecht.')
ST('Schwarzwald-Mittelhang', 'Tannen-Buchen-Zone', 4, 3, 2, {}, 'fichte',
   'Kühl und niederschlagsreich. Hier wuchs ursprünglich ein Tannen-Buchen-Wald.')
ST('Schwäbische Alb (Hochfläche)', 'Kalk, flachgründig', 2, 3, 2, {'DÜ': -1}, 'fichte',
   'Wasser versickert im Kalk – flachgründige Böden trocknen schnell aus.')
ST('Albtrauf (Südhang)', 'Steilhang, Kalk', 1, 3, 4, {'DÜ': -1, 'FE': -1}, 'buche',
   'Sonnenexponierter Steilhang – heiß, trocken, brandgefährdet.')
ST('Oberrhein-Auenwald', 'Aue, Auelehm', 5, 5, 4, {'PI': -1}, 'esche',
   'Überflutungsgeprägt und nährstoffreich. Pilze haben leichtes Spiel.')
ST('Hardtwald (Rheinebene)', 'Sand, Kiesterrasse', 1, 2, 4, {'DÜ': -1, 'FE': -1}, 'waldkiefer',
   'Trockener, warmer Sandboden – Kiefernwald und Waldbrandgefahr.')
ST('Kaiserstuhl', 'Löss auf Vulkangestein', 2, 5, 5, {}, 'traubeneiche',
   'Wärmster Ort Deutschlands, nährstoffreicher Löss.')
ST('Kraichgau (Lösshügel)', 'Löss, mild', 3, 5, 4, {}, 'buche',
   'Mildes Klima und tiefgründige Lössböden – sehr produktiv.')
ST('Odenwald / Spessart', 'Buntsandstein, Mittelgebirge', 3, 2, 3, {}, 'buche',
   'Saure, ärmere Böden unter Buchenwald.')
ST('Oberschwaben (Jungmoräne)', 'Moränenland', 4, 4, 3, {'ST': -1}, 'fichte',
   'Viel Niederschlag, gute Böden – viel Fichte. Sturmwurf-gefährdet.')
ST('Allgäuer Bergmischwald', 'Voralpen, Hanglage', 5, 4, 2, {'ST': -1}, 'fichte',
   'Hohe Niederschläge, steile Hänge. Bergmischwald aus Fichte, Tanne, Buche.')
ST('Keuperbergland (Schönbuch)', 'Tonboden, Staunässe', 4, 3, 3, {'PI': -1}, 'stieleiche',
   'Schwere Tonböden mit Staunässe – Wurzelpilze und Fäule treten häufiger auf.')

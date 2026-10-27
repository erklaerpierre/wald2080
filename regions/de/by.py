# -*- coding: utf-8 -*-
"""Edition Bayern (DE-BY) – lokale Besonderheiten."""
from regions.api import REGION, ST
from regions.sets import *

REGION(code="BY", land="DE", name="Bayern", farbe="#01579B", kachel=(2, 4),
       arten=" ".join([KERN, AUE, BERG, WARM, GAST_WARM, "moorbirke latsche"]),
       zuschlag={"ST": 1},
       hinweis="Von den Alpen bis Mainfranken; Sturm und Schnee haben im Gebirge besonderes Gewicht.")

ST('Bayerische Alpen (Hochlage)', 'Bergmischwald, Karwendel/Berchtesgaden', 5, 3, 1, {'ST': -1}, 'fichte',
   'Steil, kühl und niederschlagsreich – Schutzwald gegen Lawinen und Steinschlag.')
ST('Oberbayerische Voralpen', 'Hanglagen, Flysch und Kalk', 5, 4, 2, {'ST': -1}, 'fichte',
   'Sehr viel Regen, wüchsige Hänge. Fichte prägt, Tanne und Buche fehlen oft.')
ST('Münchner Schotterebene', 'Kiesböden, flachgründig', 2, 2, 3, {'DÜ': -1}, 'fichte',
   'Wasser versickert im Kies. Fichten leiden hier früh unter Trockenstress.')
ST('Bayerischer Wald (Hochlage)', 'Granit/Gneis, kühl', 4, 2, 1, {'ST': -1}, 'fichte',
   'Rau und schneereich. Hier zeigte der Borkenkäfer im Nationalpark, was Wald ohne Eingriff macht.')
ST('Bayerischer Wald (Mittelhang)', 'Saure Silikatböden', 4, 2, 2, {}, 'fichte',
   'Nährstoffarm und sauer; ursprünglich Bergmischwald aus Buche, Tanne und Fichte.')
ST('Fränkische Alb', 'Jurakalk, trocken', 2, 3, 3, {'DÜ': -1}, 'waldkiefer',
   'Flachgründiger Kalk – Kiefer und Buche, aber Wasser ist knapp.')
ST('Steigerwald / Keuper', 'Tonige Lehme, Hügelland', 3, 3, 3, {}, 'buche',
   'Bekannte Buchen-Eichen-Wälder. Mäßig warm, gut versorgt.')
ST('Rhön (Basalt)', 'Mittelgebirge, kühl-feucht', 4, 4, 2, {}, 'buche',
   'Nährstoffreicher Basalt unter Buchenwald, viel Niederschlag.')
ST('Mainfranken', 'Muschelkalk, warm-trocken', 1, 4, 4, {'DÜ': -1, 'FE': -1}, 'waldkiefer',
   'Eine der wärmsten und trockensten Ecken Bayerns – Weinbauklima.')
ST('Nürnberger Reichswald', 'Sandböden, Kiefernforst', 1, 1, 3, {'DÜ': -1, 'FE': -1}, 'waldkiefer',
   'Arme Sande unter Kiefernreinbeständen – Waldbrand- und Käfergefahr.')
ST('Donau-Auen', 'Aue, Überflutung', 5, 5, 4, {'PI': -1}, 'esche',
   'Nährstoffreicher Auwald – Eschentriebsterben und Pilze setzen zu.')
ST('Niederbayerisches Hügelland', 'Lehm, Tertiär', 3, 4, 3, {}, 'fichte',
   'Gute Böden, mäßig trocken, viel Fichtenanbau auf Standorten, die zu warm werden.')
ST('Fichtelgebirge / Oberpfälzer Wald', 'Granit, kühl', 4, 2, 2, {'ST': -1}, 'fichte',
   'Raues Mittelgebirge. Fichtenforste auf armen Böden, sturmgefährdet.')

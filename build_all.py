# -*- coding: utf-8 -*-
"""Baut das komplette Spielmaterial: python3 build_all.py   (Gewinnquoten neu rechnen: python3 balancing.py)"""
import build_cards, build_boards, build_docs, build_bilder, build_editionen, balancing
from data import pruefe

pruefe()
build_cards.build()
build_boards.revierplan(); build_boards.leitstelle(); build_boards.etiketten()
bal = balancing.lade()
build_docs.csvs(); build_docs.regelheft(); build_docs.uebersicht()
build_bilder.bildnachweis()
for r in build_editionen.REGION_LISTE:
    build_editionen.baue(r, bal[r["code"]])
print("alles gebaut")

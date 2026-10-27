# -*- coding: utf-8 -*-
"""
Wald 2080 – Fassade: führt den BASISSATZ (core/) und alle EDITIONEN (regions/) zusammen.
Alle Karten, Tabellen und Simulationen importieren weiterhin aus data.py.

  core/      Baumarten, Ereignisse, Fachkarten, Konstanten  – gilt für alles
  regions/   eine Datei je Bundesland/Region               – nur lokale Besonderheiten
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core.konstanten import *
from core.arten import SPECIES, SPECIES_LIST
from core.ereignisse import *
from core.fachkarten import FACH
import regions
from regions.api import REGIONEN, STANDORTE

STANDORT_MAP = {s["id"]: s for s in STANDORTE}
LAENDER = {"DE": "Deutschland", "AT": "Österreich", "CH": "Schweiz"}
# Reihenfolge der Editionen: Land, dann Name
REGION_LISTE = sorted(REGIONEN.values(), key=lambda r: (["DE", "AT", "CH"].index(r["land"]), r["name"]))
REGION_ORDER = {r["code"]: i for i, r in enumerate(REGION_LISTE)}

# Abgeleitet aus den Regionsdateien: in welchen Regionen ist eine Art typisch?
for sp in SPECIES_LIST:
    sp["regionen"] = [r["code"] for r in REGION_LISTE if sp["id"] in r["arten"]]
    sp["laender"] = sorted({REGIONEN[c]["land"] for c in sp["regionen"]}, key=["DE", "AT", "CH"].index)


def pruefe():
    """Konsistenzprüfung: wirft AssertionError mit klarer Meldung."""
    for r in REGION_LISTE:
        for a in r["arten"]:
            assert a in SPECIES, f'{r["code"]}: unbekannte Art "{a}"'
        assert r["code"].isascii(), r["code"]
    for s in STANDORTE:
        assert s["start"] in SPECIES, f'{s["id"]}: Startart "{s["start"]}" unbekannt'
        assert s["start"] in REGIONEN[s["reg"]]["arten"] or SPECIES[s["start"]]["deck"] == "basis", \
            f'{s["id"]}: Startart {s["start"]} nicht in ARTEN von {s["reg"]}'
        for ax in "WNT":
            assert 1 <= s[ax] <= 5, s["id"]
        for k in s["mods"]:
            assert k in RES_KEYS, s["id"]
    kachel = [r["kachel"] for r in REGION_LISTE]
    assert len(set(kachel)) == len(kachel), "Kachelposition doppelt"
    return True

if __name__ == "__main__":
    pruefe()
    print(len(SPECIES_LIST), "Arten,", len(REGIONEN), "Regionen,", len(STANDORTE), "Standorte")

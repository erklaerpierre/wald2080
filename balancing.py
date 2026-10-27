# -*- coding: utf-8 -*-
"""Simuliert alle Editionen (Strategie "solide") und speichert Gewinnquoten in _balance.json."""
import json, os, sys
import sim
from data import REGION_LISTE

FN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_balance.json")
FORMATE = (("kurz", 3, 3, 12), ("standard", 6, 7, 12), ("lang", 8, 7, 14))


def rechne(N=800):
    out = {}
    for r in REGION_LISTE:
        row = {}
        for name, rounds, nf, ziel in FORMATE:
            res = [sim.play(r["code"], "solide", rounds, seed=i, nfields=nf)[0] for i in range(N)]
            row[name] = round(100 * sum(1 for x in res if x >= ziel) / N)
        res = [sim.play(r["code"], "passiv", 6, seed=i, nfields=7)[0] for i in range(N)]
        row["passiv"] = round(100 * sum(1 for x in res if x >= 12) / N)
        out[r["code"]] = row
        print(r["code"], row, flush=True)
    json.dump(out, open(FN, "w"), indent=1)
    return out


def lade():
    if os.path.exists(FN):
        return json.load(open(FN))
    return rechne()


if __name__ == "__main__":
    rechne(int(sys.argv[1]) if len(sys.argv) > 1 else 800)

# -*- coding: utf-8 -*-
"""Schnittstelle für Regionsdateien. Eine Regionsdatei = eine Edition.

So legst du eine neue Edition an: regions/_VORLAGE.py kopieren nach regions/<land>/<kuerzel>.py,
Kopf ausfüllen, Standorte eintragen, fertig. Es ist keine andere Datei anzufassen.
"""
REGIONEN = {}      # code -> dict
STANDORTE = []     # alle Standorte aller Editionen
_cur = [None]


def REGION(code, land, name, farbe, kachel, arten, zuschlag=None, hinweis=""):
    """code     – kurzes eindeutiges Kürzel (z. B. 'BW')
    land     – 'DE' | 'AT' | 'CH'
    farbe    – Farbe der Standortkarten (dunkel genug für weiße Schrift)
    kachel   – (Spalte, Zeile) auf der Kachelkarte (siehe regions/kachelkarte.py)
    arten    – Baumarten-IDs, die in dieser Region typisch/anbauwürdig sind (Leerzeichen-getrennt)
    zuschlag – Regionale Zusatzstärke für Ereignisse, z. B. {"DÜ": 3, "FE": 3} (Balancing-Stellschraube)
    """
    r = dict(code=code, land=land, name=name, farbe=farbe, kachel=kachel,
             arten=sorted(set(arten.split())), zuschlag=dict(zuschlag or {}), hinweis=hinweis, n=0)
    assert code not in REGIONEN, f"Regionskürzel doppelt: {code}"
    REGIONEN[code] = r
    _cur[0] = r
    return r


def ST(name, land, W, N, T, mods, start, text):
    """Standort der aktuell geladenen Region. ID wird automatisch vergeben (z. B. bw01)."""
    r = _cur[0]
    r["n"] += 1
    sid = f'{r["code"].lower()}{r["n"]:02d}'
    STANDORTE.append(dict(id=sid, reg=r["code"], name=name, land=land, W=W, N=N, T=T,
                          mods=mods, start=start, text=text))

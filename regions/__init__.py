# -*- coding: utf-8 -*-
"""Lädt alle Editionen (regions/<land>/<kuerzel>.py). Dateien mit '_' am Anfang werden ignoriert."""
import importlib, pkgutil, os
from regions.api import REGIONEN, STANDORTE

def lade_alle():
    if REGIONEN:
        return
    base = os.path.dirname(__file__)
    for land in sorted(os.listdir(base)):
        d = os.path.join(base, land)
        if not os.path.isdir(d) or land.startswith(("_", ".")):
            continue
        for m in sorted(pkgutil.iter_modules([d]), key=lambda m: m.name):
            if not m.name.startswith("_"):
                importlib.import_module(f"regions.{land}.{m.name}")

lade_alle()

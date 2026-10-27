# -*- coding: utf-8 -*-
"""Balance-Simulation für Wald 2080 (Basis-Regeln). Nutzt data.py als Datenquelle."""
import random, statistics, sys
from data import *

START_SP = 8
SOFF = 0
SP_MAX = 20
START_KASSE = 4
INCOME = 3
E_BONUS = {3: 2, 2: 0, 1: -2, 0: -4}
NEIGH = {0: [1, 2, 3, 4, 5, 6]}
for i in range(1, 7):
    NEIGH[i] = [0, (i % 6) + 1, ((i - 2) % 6) + 1]

def in_range(v, r): return r[0] <= v <= r[1]

def eignung(sp, site, k, extra_n=0, bod=False):
    W, T = klima(site["W"], site["T"], k)
    n = site["N"] + extra_n
    c = int(in_range(W, sp["W"])) + int(in_range(T, sp["T"])) + int(in_range(min(5, n), sp["N"]))
    if bod and not in_range(min(5, n), sp["N"]):
        c += 1
    return c

def matches(filt, f, site, k):
    sp = SPECIES.get(f["main"]);
    if not sp: return False
    if filt == "alle": return True
    if filt == "nadel": return sp["grp"] == "Nadel"
    if filt == "laub": return sp["grp"] == "Laub"
    if filt == "jung": return f["jung"]
    if filt == "E<3": return eignung(sp, site, k, f["kalk"], mix_bod(f)) < 3
    return f["main"] in GRUPPEN[filt]

def mix_bod(f):
    return bool(f["mix"]) and "BOD" in SPECIES[f["mix"]]["eig"]

class Revier:
    def __init__(self, region, rnd, nfields=7):
        ids = [s["id"] for s in STANDORTE if s["reg"] == region]
        rnd.shuffle(ids)
        self.f = []
        for i in range(nfields):
            site = STANDORT_MAP[ids[i % len(ids)]]
            self.f.append(dict(site=site, main=site["start"], mix=None, h=3, jung=False,
                               mjung=False, kalk=0, schutz=0))
        self.region = region
        self.sp = START_SP
        self.kasse = START_KASSE
        self.n = nfields
        self.nb = {i: [j for j in NEIGH[i] if j < nfields] for i in range(nfields)}

def probe_vals(r, f, kind, S_, k, die):
    """Liefert (P_main, P_mix|None)."""
    site = f["site"]
    msp = SPECIES[f["main"]]
    bodm = mix_bod(f)
    Em = E_BONUS[eignung(msp, site, k, f["kalk"], bodm)]
    mod = site["mods"].get(kind, 0)
    sch = f["schutz"] if kind == "VE" else 0
    jm = -1 if (f["jung"] and "PIO" not in msp["eig"]) else 0
    Pm = die + msp["res"][kind] + Em + mod + jm + sch
    Px = None
    if f["mix"]:
        xsp = SPECIES[f["mix"]]
        Ex = E_BONUS[eignung(xsp, site, k, f["kalk"], False)]
        jx = -1 if (f["mjung"] and "PIO" not in xsp["eig"] and "SCH" not in xsp["eig"]) else 0
        Px = die + xsp["res"][kind] + Ex + mod + jx + sch
    return Pm, Px

def resolve_damage(r, ev, k, die, extra_prot=None):
    S_ = ev["S"]
    if ev["kind"] in ("DÜ",) and False: pass
    S_eff = S_ + SOFF
    if k >= 2 and ev["kind"] in ("DÜ", "KÄ", "FE"):
        S_eff += 1
    S_eff += REGIONEN[r.region]["zuschlag"].get(ev["kind"], 0)
    kind = ev["kind"]
    failed = set(); damage = {}
    tested = set()
    def test(i, extra=0):
        f = r.f[i]
        Pm, Px = probe_vals(r, f, kind, S_eff, k, die)
        Pm += extra
        if Px is not None:
            Px += extra
            xsp_aff = matches_species(ev["filt"], f["mix"])
            # Mischbaum nicht betroffen -> rettet das Feld
            if not xsp_aff and ev["filt"] not in ("alle", "nadel", "laub", "jung", "E<3"):
                return 0
            best = max(Pm, Px)
        else:
            best = Pm
        if best >= S_eff: return 0
        return 2 if S_eff - best >= 4 else 1
    for i, f in enumerate(r.f):
        if f["main"] is None: continue
        if not matches(ev["filt"], f, f["site"], k): continue
        tested.add(i)
        d = test(i)
        if d: failed.add(i); damage[i] = d
    if ev["spread"]:
        frontier = set(failed)
        while frontier:
            new = set()
            for i in frontier:
                fi = r.f[i]
                if fi["mix"]: continue
                for j in r.nb[i]:
                    if j in tested: continue
                    fj = r.f[j]
                    if fj["main"] == fi["main"] and not fj["mix"] and fj["main"]:
                        tested.add(j)
                        d = test(j, extra=-1)
                        if d: new.add(j); damage[j] = d; failed.add(j)
            frontier = new
    return damage

def matches_species(filt, sid):
    if filt in ("alle", "nadel", "laub", "jung", "E<3"): return True
    return sid in GRUPPEN[filt]

def apply_damage(r, damage, prot=None):
    for i, d in damage.items():
        f = r.f[i]
        if prot and i in prot: d = max(0, d - 1)
        f["h"] -= d
        if f["h"] <= 0:
            f.update(main=None, mix=None, h=0, jung=False, mjung=False)

def end_round(r, k):
    sp = r.sp
    species = set(); mixed = 0
    for f in r.f:
        if f["main"] is None: sp -= 2; continue
        msp = SPECIES[f["main"]]
        species.add(f["main"])
        if f["mix"]: species.add(f["mix"])
        if f["h"] in (1, 2) and eignung(msp, f["site"], k, f["kalk"], mix_bod(f)) == 3:
            f["h"] += 1
        if f["h"] == 1: sp -= 1
        if f["mix"] and f["h"] >= 2: mixed += 1
        if "INV" in msp["eig"] or (f["mix"] and "INV" in SPECIES[f["mix"]]["eig"]): sp -= 1
        f["jung"] = False; f["mjung"] = False; f["schutz"] = 0
    if mixed >= (r.n + 1) // 2: sp += 1
    if len({s for s in species if "INV" not in SPECIES[s]["eig"]}) >= 5: sp += 1
    r.sp = max(0, min(SP_MAX, sp))
    r.kasse += INCOME

# ------------------------------------------------------------ Strategien
def best_candidates(r, i, k, pool, as_mix=False, avoid=()):
    f = r.f[i]; site = f["site"]
    out = []
    for sid in pool:
        sp = SPECIES[sid]
        if "INV" in sp["eig"]: continue
        e = eignung(sp, site, k, f["kalk"], False)
        if e < 3: continue
        score = sum(sp["res"].values()) / 7 + 0.25 * sp["hw"] - 0.35 * sp["cost"]
        if sid in avoid: score -= 1.0
        out.append((score, sid))
    out.sort(reverse=True)
    return [s for _, s in out]

def plan_smart(r, k, pool, rnd, upcoming=None):
    used = {f["main"] for f in r.f if f["main"]} | {f["mix"] for f in r.f if f["mix"]}
    # 1 Kahlflächen bepflanzen
    for i, f in enumerate(r.f):
        if f["main"] is None and r.kasse > 0:
            c = best_candidates(r, i, k, pool, avoid=used)
            for sid in c:
                cost = SPECIES[sid]["cost"]
                if cost <= r.kasse:
                    r.kasse -= cost; f.update(main=sid, h=2, jung="PIO" not in SPECIES[sid]["eig"])
                    used.add(sid); break
    # 2 ungeeignete Bestände ernten und umbauen (nur wenn Erlös + Kasse für Neupflanzung reichen)
    cand = []
    for i, f in enumerate(r.f):
        if f["main"] is None: continue
        sp = SPECIES[f["main"]]
        e = eignung(sp, f["site"], k, f["kalk"], mix_bod(f))
        if e <= 1 and f["h"] >= 2:
            cand.append((e, i))
    cand.sort()
    for e, i in cand:
        f = r.f[i]
        sp = SPECIES[f["main"]]
        gain = sp["hw"] + (1 if f["h"] == 3 else 0)
        c = best_candidates(r, i, k, pool, avoid=used)
        if not c: continue
        sid = next((s for s in c if SPECIES[s]["cost"] <= r.kasse + gain), None)
        if sid is None: continue
        r.kasse += gain
        r.kasse -= SPECIES[sid]["cost"]
        f.update(main=sid, mix=None, h=2, jung="PIO" not in SPECIES[sid]["eig"], mjung=False)
        used.add(sid)
    # 3 Mischbaumarten ergänzen (Reinbestände mit Eignung < 3 oder anfällig zuerst)
    order = sorted(range(r.n), key=lambda i: (r.f[i]["main"] is None,
                   eignung(SPECIES[r.f[i]["main"]], r.f[i]["site"], k, r.f[i]["kalk"], False) if r.f[i]["main"] else 9))
    for i in order:
        f = r.f[i]
        if f["main"] is None or f["mix"] or f["h"] < 1: continue
        if r.kasse < 1: break
        c = best_candidates(r, i, k, pool, as_mix=True, avoid=used | {f["main"]})
        c = [s for s in c if s != f["main"]]
        for sid in c:
            cost = SPECIES[sid]["cost"]
            if cost <= r.kasse - 0:
                r.kasse -= cost; f["mix"] = sid; f["mjung"] = True; used.add(sid); break
    # 4 Pflege
    for f in r.f:
        if f["main"] and f["h"] < 3 and r.kasse >= 1 and f["h"] <= 1:
            r.kasse -= 1; f["h"] += 1

def plan_passive(r, k, pool, rnd, upcoming=None):
    for i, f in enumerate(r.f):
        if f["main"] is None:
            sid = f["site"]["start"]; cost = SPECIES[sid]["cost"]
            if cost <= r.kasse:
                r.kasse -= cost; f.update(main=sid, h=2, jung="PIO" not in SPECIES[sid]["eig"])
    for f in r.f:
        if f["main"] and f["h"] < 3 and r.kasse >= 1:
            r.kasse -= 1; f["h"] += 1

def plan_random(r, k, pool, rnd, upcoming=None):
    for i, f in enumerate(r.f):
        if f["main"] is None and r.kasse > 0:
            sid = rnd.choice(pool)
            if SPECIES[sid]["cost"] <= r.kasse and eignung(SPECIES[sid], f["site"], k, 0, False) >= 1:
                r.kasse -= SPECIES[sid]["cost"]; f.update(main=sid, h=2, jung="PIO" not in SPECIES[sid]["eig"])
    for f in r.f:
        if f["main"] and not f["mix"] and r.kasse > 1 and rnd.random() < 0.4:
            sid = rnd.choice(pool)
            if SPECIES[sid]["cost"] <= r.kasse and sid != f["main"]:
                r.kasse -= SPECIES[sid]["cost"]; f["mix"] = sid; f["mjung"] = True

def plan_solid(r, k, pool, rnd, upcoming=None):
    """Gutes menschliches Team: plant sinnvoll, kennt aber nur einen Teil der Arten und handelt nicht immer optimal."""
    sub = rnd.sample(pool, max(8, int(len(pool) * 0.45)))
    plan_smart(r, k, sub, rnd)

STRATS = {"smart": plan_smart, "solide": plan_solid, "passiv": plan_passive, "zufall": plan_random}

# ------------------------------------------------------------ Spiel
def draw_events(rnd, nrounds, per_round=2):
    need = nrounds * per_round
    n_good = max(1, round(need * 0.2))
    bad = rnd.sample(SCHADEN, need - n_good)
    good = rnd.sample(GUTE, n_good)
    deck = bad + good
    rnd.shuffle(deck)
    return deck

def play(region="BW", strat="smart", rounds=6, seed=None, pool_decks=("basis",), nfields=7, verbose=False):
    rnd = random.Random(seed)
    r = Revier(region, rnd, nfields)
    pool = [s["id"] for s in SPECIES_LIST if s["deck"] in pool_decks or (s["id"] in REGIONEN[region]["arten"] and "basis" in pool_decks)]
    deck = draw_events(rnd, rounds)
    ki = 0
    for rd in range(1, rounds + 1):
        k = KLIMAPFAD_STANDARD[rd]
        STRATS[strat](r, k, pool, rnd)
        kround = k
        prot = None
        evs = [deck[ki], deck[ki + 1]]; ki += 2
        for ev in evs:
            die = rnd.randint(1, 6)
            if ev["id"] == "heiss": kround = k + 1; continue
            if ev["id"] == "kuehl": kround = max(0, k - 1); continue
            if ev["kind"] in RES_KEYS:
                dmg = resolve_damage(r, ev, kround, die)
                apply_damage(r, dmg)
            else:
                if ev["id"] == "foerder": r.kasse += 3
                elif ev["id"] == "mast":
                    for f in r.f:
                        if f["main"] in ("buche", "traubeneiche", "stieleiche"): f["h"] = min(3, f["h"] + 1)
                elif ev["id"] == "regen":
                    for f in r.f:
                        if f["main"] and f["site"]["W"] <= 2: f["h"] = min(3, f["h"] + 1)
                elif ev["id"] == "schule": r.sp = min(SP_MAX, r.sp + 1)
        end_round(r, kround)
        if verbose: print(rd, JAHRE[rd], r.sp, r.kasse, [f["main"] for f in r.f])
    kahl = sum(1 for f in r.f if f["main"] is None)
    return r.sp, kahl

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
    for region in ("BW", "BB"):
        for strat in ("passiv", "zufall", "smart"):
            res = [play(region, strat, 6, seed=i) for i in range(N)]
            sps = [a for a, _ in res]
            print(f"{region:3} {strat:7} Ø SP {statistics.mean(sps):5.1f} | P10 {sorted(sps)[N//10]:2} P50 {sorted(sps)[N//2]:2} "
                  f"P90 {sorted(sps)[9*N//10]:2} | Ø Kahl {statistics.mean(k for _, k in res):.2f}")

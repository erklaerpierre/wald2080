# -*- coding: utf-8 -*-
"""BASISSATZ · Ereigniskarten und Artengruppen für Ereignisfilter. Gilt für ALLE Editionen."""
from core.konstanten import RES_KEYS

# filter: Beschreibung + Schlüssel
EVENTS = []
def EV(id, name, kind, S_, filt, filtertext, spread, text, lehr, n=1, effekt=None):
    EVENTS.append(dict(id=id, name=name, kind=kind, S=S_, filt=filt, filtertext=filtertext,
                       spread=spread, text=text, lehr=lehr, n=n, effekt=effekt))

NADEL = "nadel"; LAUB = "laub"
EV("duerre1","Trockensommer","DÜ",8,"alle","Alle Felder",False,
   "Wochenlang kein Regen. Wasserstress überall.","Tiefwurzler und trockenheitsfeste Arten haben Vorteile.")
EV("duerre2","Jahrhundertdürre","DÜ",10,"alle","Alle Felder",False,
   "Mehrere Dürrejahre in Folge – so wie 2018 bis 2020.","Mehrjährige Dürre schwächt auch robuste Bestände.")
EV("hitze","Hitzewelle & Sonnenbrand","DÜ",8,LAUB,"Alle Laubholz-Felder",False,
   "Rindenschäden durch pralle Sonne bei freigestellten Stämmen.","Mischbestände und Schirm schützen die Rinde.")
EV("sturm1","Sturmtief","ST",8,"alle","Alle Felder",False,
   "Winterstürme fegen übers Land.","Flachwurzler fallen zuerst.")
EV("sturm2","Orkan","ST",10,"alle","Alle Felder",False,
   "Wie „Lothar“ 1999 im Schwarzwald: großflächiger Windwurf.","Reine Fichtenbestände sind besonders gefährdet.")
EV("schnee","Nassschnee","ST",7,NADEL,"Alle Nadelholz-Felder",False,
   "Schwerer Schnee bricht Kronen und Äste.","Nadelholz hält Schnee länger – mehr Bruch.")
EV("buchdrucker","Buchdrucker-Massenvermehrung","KÄ",9,"picea","Alle Felder mit Fichten-Arten",True,
   "Der Borkenkäfer vermehrt sich explosionsartig.","Reinbestände stecken sich gegenseitig an.")
EV("prachtkaefer","Kiefernprachtkäfer","KÄ",8,"pinus","Alle Felder mit Kiefern-Arten",True,
   "Käfer befallen dürregeschwächte Kiefern.","Vorgeschädigte Bäume sind die ersten Opfer.")
EV("eps","Eichenprozessionsspinner","KÄ",8,"quercus","Alle Felder mit Eichen-Arten",True,
   "Raupen fressen die Blätter kahl.","Wärme begünstigt viele Schadinsekten.")
EV("schwammspinner","Schwammspinner-Gradation","KÄ",8,LAUB,"Alle Laubholz-Felder",True,
   "Raupenfraß in warmen, trockenen Jahren.","Gradationen kommen in Wellen.")
EV("nonne","Nonnen-Fraß","KÄ",8,NADEL,"Alle Nadelholz-Felder",True,
   "Raupen fressen Nadeln – ganze Bestände können kahl werden.","Monokulturen sind die ideale Futterfläche.")
EV("esche_t","Eschentriebsterben","PI",10,"fraxinus","Alle Felder mit Eschen",True,
   "Ein eingeschleppter Pilz lässt Triebe und Kronen absterben.","Eingeschleppte Krankheiten treffen ganze Baumarten.")
EV("russrinde","Rußrindenkrankheit","PI",9,"acer_big","Alle Felder mit Berg-/Spitzahorn",True,
   "Ein Pilz nutzt die Dürreschwäche des Ahorns aus.","Erst Trockenstress, dann Pilz.")
EV("ulme_t","Ulmensterben","PI",9,"ulmus","Alle Felder mit Ulmen",True,
   "Ulmensplintkäfer übertragen einen Pilz.","Käfer und Pilz arbeiten zusammen.")
EV("erlen_t","Phytophthora-Erlensterben","PI",9,"alnus","Alle Felder mit Erlen",True,
   "Ein wasserbürtiger Erreger befällt Erlenwurzeln.","Nasse Standorte bringen eigene Krankheiten mit.")
EV("hallimasch","Hallimasch & Wurzelfäule","PI",8,"E<3","Alle Felder ohne volle Eignung (E < 3)",False,
   "Schwächeparasiten befallen gestresste Bestände.","Nicht standortgerechte Bäume sind anfälliger.")
EV("diplodia","Diplodia-Triebsterben","PI",8,"pinus","Alle Felder mit Kiefern-Arten",True,
   "Pilzkrankheit – häufig nach Hitze und Trockenheit.","Stress öffnet das Tor für Pilze.")
EV("spaetfrost","Spätfrost im Mai","FR",7,"alle","Alle Felder",False,
   "Frische Triebe erfrieren nach dem Austrieb.","Wärmeres Frühjahr = früherer Austrieb = mehr Frostrisiko.")
EV("kaelte","Kälteeinbruch","FR",6,"alle","Alle Felder",False,
   "Ein ungewöhnlich strenger Winter.","Klimawandel heißt nicht: nie wieder Frost.")
EV("brand1","Waldbrandgefahr Stufe 5","FE",7,"alle","Alle Felder",False,
   "Trockener Waldboden und starker Wind.","Kiefernreinbestände brennen besonders gut.")
EV("brand2","Großer Waldbrand","FE",9,"alle","Alle Felder",False,
   "Ein Feuer breitet sich über mehrere Hektar aus.","Laubmischwald brennt deutlich seltener als Nadelforst.")
EV("verbiss","Wildverbiss","VE",7,"jung","Alle Jungwuchs-Felder",False,
   "Rehe verbeißen die frischen Knospen.","Ohne Schutz haben Jungpflanzen es schwer.")
EV("schaele","Schälschäden durch Rotwild","VE",7,NADEL,"Alle Nadelholz-Felder",False,
   "Rotwild schält die Rinde ab – Eintrittspforte für Fäulepilze.","Wildmanagement ist Waldschutz.")
EV("foerder","Förderprogramm Waldumbau","GUT",0,"alle","Alle Reviere",False,
   "Das Land fördert den Umbau zum klimastabilen Mischwald.","Förderung kann Risiken abfedern.",
   effekt="Jedes Revier erhält sofort +3 T€.")
EV("mast","Mastjahr","GUT",0,"alle","Felder mit Buche oder Eiche",False,
   "Bucheckern und Eicheln fallen reichlich – Naturverjüngung!","Naturverjüngung ist kostenlos – wenn die Mutterbäume stehen.",
   effekt="Jedes Feld mit Buche oder Eiche als Hauptbaumart erhält +1 Herz (max. 3).")
EV("holzpreis","Guter Holzpreis","GUT",0,"alle","Alle Reviere",False,
   "Die Nachfrage nach Holz steigt.","Wer sein Holz zur richtigen Zeit nutzt, finanziert den Umbau.",
   effekt="Alle Nutzungen (Ernten) dieser Runde bringen +1 T€ je Feld.")
EV("regen","Regenreiches Jahr","GUT",0,"alle","Felder mit Wasser 1–2",False,
   "Endlich wieder Wasser im Boden.","Ein nasses Jahr macht noch keinen Wald klimafit.",
   effekt="Jedes Feld mit Wasser 1–2 erhält +1 Herz (max. 3).")
EV("schule","Waldschulprojekt","GUT",0,"alle","Alle Reviere",False,
   "Schulklassen pflanzen mit – Gesellschaft und Wald profitieren.","Waldumbau gelingt nur gemeinsam.",
   effekt="Jedes Revier erhält +1 Stabilität.")
EV("fortbildung","Forstliche Fortbildung","GUT",0,"alle","Alle Reviere",False,
   "Neues Fachwissen aus Forschung und Praxis.","Wissen ist ein Schutzfaktor.",
   effekt="Jedes Team zieht sofort 1 Fachkarte.")
EV("heiss","Heißes Jahrzehnt","KL",0,"alle","Alle Reviere",False,
   "Ein Rekordjahrzehnt – das Klima eilt voraus.","Klimaprognosen sind Wahrscheinlichkeiten.",
   effekt="Die Klimastufe zählt in dieser Runde +1.")
EV("kuehl","Kühles Jahrzehnt","KL",0,"alle","Alle Reviere",False,
   "Eine kühle Phase – aber der Trend bleibt.","Natürliche Schwankungen überlagern den Trend.",
   effekt="Die Klimastufe zählt in dieser Runde −1 (mindestens 0).")

EVENT_MAP = {e["id"]: e for e in EVENTS}
SCHADEN = [e for e in EVENTS if e["kind"] in RES_KEYS]
GUTE = [e for e in EVENTS if e["kind"] in ("GUT", "KL")]

# Artengruppen für Ereignisfilter
GRUPPEN = {
    "picea":   {"fichte", "serb_fichte", "sitkafichte"},
    "pinus":   {"waldkiefer", "schwarzkiefer", "seestrandkiefer", "zirbe", "spirke", "rumel_kiefer",
                "aleppokiefer", "gelbkiefer", "strobe", "radiata"},
    "quercus": {"traubeneiche", "stieleiche", "roteiche", "zerreiche", "flaumeiche", "korkeiche",
                "steineiche", "ungar_eiche", "sumpfeiche"},
    "fraxinus": {"esche", "resistente_esche", "schmal_esche"},
    "acer_big": {"bergahorn", "spitzahorn"},
    "ulmus":   {"flatterulme", "bergulme"},
    "alnus":   {"schwarzerle", "grauerle"},
}

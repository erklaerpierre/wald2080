# -*- coding: utf-8 -*-
"""BASISSATZ · Baumarten. Gilt für ALLE Editionen.
Hier steht NICHT, wo eine Art vorkommt – das steht in den Regionsdateien (regions/…, Liste ARTEN).
Spalten: id, Name, Latein, deck, Gruppe, Kategorie, W, N, T, Resistenzen(7), Holzwert, Kosten T€, Eigenschaften, Merksatz
"""
from core.konstanten import RES_KEYS

_S = []
def S(id, name, latin, deck, grp, kat, W, N, T, res, hw, cost, eig, note):
    _S.append(dict(id=id, name=name, latin=latin, deck=deck, grp=grp, kat=kat,
                   W=W, N=N, T=T, res=dict(zip(RES_KEYS, res)), hw=hw, cost=cost,
                   eig=eig, note=note))

H, E, Z = "heimisch", "etabliert", "Züchtung"
S("fichte","Fichte","Picea abies","basis","Nadel",H,(3,4),(2,4),(1,3),(1,1,1,2,4,2,2),3,1,[],
  "Flachwurzler und „Brotbaum“ – bei Hitze und Trockenheit im Tiefland sehr anfällig.")
S("waldkiefer","Waldkiefer","Pinus sylvestris","basis","Nadel",H,(1,3),(1,3),(1,5),(4,3,2,2,5,1,2),3,1,["PIO"],
  "Genügsam auf Sand – aber brandgefährdet, Reinbestände leiden unter Schädlingen.")
S("tanne","Weißtanne","Abies alba","basis","Nadel",H,(3,4),(3,5),(1,3),(3,4,4,3,3,3,1),3,2,["SCH"],
  "Tiefwurzler und sturmfest – das Reh frisst sie besonders gern.")
S("laerche","Europäische Lärche","Larix decidua","basis","Nadel",H,(2,3),(2,4),(1,3),(3,3,3,3,4,3,2),4,1,["PIO"],
  "Nadelbaum mit Herbstabwurf – Lichtbaumart mit wertvollem Holz.")
S("eibe","Eibe","Taxus baccata","basis","Nadel",H,(2,4),(3,5),(2,4),(3,4,5,4,3,3,2),3,2,["SCH"],
  "Sehr langsam und uralt, giftig – verträgt tiefen Schatten.")
S("buche","Rotbuche","Fagus sylvatica","basis","Laub",H,(3,4),(3,5),(2,4),(2,3,4,3,2,4,2),3,1,["SCH"],
  "Dominante Waldbaumart Mitteleuropas – leidet unter Hitze und Sonnenbrand.")
S("traubeneiche","Traubeneiche","Quercus petraea","basis","Laub",H,(1,4),(2,4),(3,5),(4,4,3,3,3,4,2),5,2,[],
  "Tiefwurzelnd und trockenheitstolerant – Hoffnungsträger für warme Standorte.")
S("stieleiche","Stieleiche","Quercus robur","basis","Laub",H,(3,5),(3,5),(3,5),(3,4,3,3,3,4,2),5,2,[],
  "Bevorzugt frische bis wechselfeuchte Lehmböden und Auen.")
S("hainbuche","Hainbuche","Carpinus betulus","basis","Laub",H,(1,4),(2,5),(3,5),(3,4,4,4,4,3,3),2,1,["SCH","BOD"],
  "Zäh, schattenverträglich und bodenverbessernd – ideale Mischbaumart.")
S("bergahorn","Bergahorn","Acer pseudoplatanus","basis","Laub",H,(3,5),(4,5),(1,3),(2,3,3,2,3,3,2),4,2,[],
  "Braucht kühle, frische, nährstoffreiche Standorte – Rußrindenkrankheit nimmt zu.")
S("spitzahorn","Spitzahorn","Acer platanoides","basis","Laub",H,(2,4),(3,5),(3,5),(3,3,4,3,3,3,2),3,2,[],
  "Wärmeliebender als der Bergahorn – robuster Mischbaum auf guten Böden.")
S("feldahorn","Feldahorn","Acer campestre","basis","Laub",H,(1,3),(3,5),(3,5),(4,3,4,4,3,3,3),2,1,["SCH"],
  "Kleiner Baum, trockenheitsverträglich – gute Unterstandsart.")
S("esche","Gemeine Esche","Fraxinus excelsior","basis","Laub",H,(3,5),(4,5),(2,4),(2,3,3,1,3,3,2),4,2,[],
  "Das Eschentriebsterben (Pilz) bedroht die Art großflächig.")
S("schwarzerle","Schwarzerle","Alnus glutinosa","basis","Laub",H,(4,5),(3,5),(2,4),(1,3,4,2,3,3,3),2,1,["PIO","BOD"],
  "Bindet Stickstoff über Wurzelknöllchen – Spezialistin für nasse Böden.")
S("sandbirke","Sandbirke","Betula pendula","basis","Laub",H,(1,3),(1,3),(1,5),(4,2,3,3,5,3,2),1,1,["PIO"],
  "Pionier auf armen Sanden – kurzlebig, aber Wegbereiter für andere Arten.")
S("moorbirke","Moorbirke","Betula pubescens","basis","Laub",H,(4,5),(1,3),(1,3),(1,2,3,3,5,3,2),1,1,["PIO"],
  "Pionier auf nassen, nährstoffarmen Moorböden.")
S("winterlinde","Winterlinde","Tilia cordata","basis","Laub",H,(2,4),(3,5),(3,5),(3,4,4,4,3,4,2),2,2,["SCH","BOD"],
  "Tiefwurzelnd und humusbildend – gilt als Klimawandel-Baumart.")
S("flatterulme","Flatterulme","Ulmus laevis","basis","Laub",H,(4,5),(4,5),(3,5),(3,3,3,2,3,3,3),3,2,[],
  "Verträgt Überflutung – das Ulmensterben setzt ihr weniger zu als anderen Ulmen.")
S("vogelkirsche","Vogelkirsche","Prunus avium","basis","Laub",H,(2,4),(3,5),(3,5),(3,3,3,2,3,3,2),4,2,[],
  "Wertholzbaum – braucht nährstoffreiche, lockere Böden.")
S("elsbeere","Elsbeere","Sorbus torminalis","basis","Laub",H,(1,3),(3,5),(4,5),(5,4,4,4,3,4,2),5,3,[],
  "Selten und trockenheitsresistent – liefert sehr wertvolles Holz.")
S("speierling","Speierling","Sorbus domestica","basis","Laub",H,(1,3),(3,5),(4,5),(5,4,4,4,2,4,2),5,3,[],
  "Eine der seltensten Baumarten Deutschlands – wärme- und trockenheitstolerant.")
S("espe","Zitterpappel (Espe)","Populus tremula","basis","Laub",H,(2,4),(2,4),(1,4),(3,2,3,3,5,4,1),1,1,["PIO"],
  "Pionier mit Wurzelbrut – Verbiss-Liebling.")
S("schwarzpappel","Schwarzpappel","Populus nigra","basis","Laub",H,(4,5),(3,5),(3,5),(2,2,3,3,3,3,2),2,2,["PIO"],
  "Baum der Weichholzaue – heute selten geworden.")
S("silberweide","Silberweide","Salix alba","basis","Laub",H,(4,5),(3,5),(2,5),(1,2,3,3,4,3,2),1,1,["PIO"],
  "Verträgt Hochwasser – typische Art der Weichholzaue.")
S("eberesche","Eberesche (Vogelbeere)","Sorbus aucuparia","basis","Laub",H,(2,4),(1,4),(1,4),(3,3,4,4,5,3,1),1,1,["PIO"],
  "Pionier mit Beeren für Vögel – aber vom Wild gern verbissen.")
S("mehlbeere","Mehlbeere","Sorbus aria","basis","Laub",H,(1,2),(3,5),(3,5),(5,3,4,4,3,4,2),2,2,[],
  "Kalk- und trockenheitsliebend – Zukunftsart für Südhänge.")
# ---------------------------------------------------------------- BASIS: etablierte Gastbaumarten
S("douglasie","Douglasie","Pseudotsuga menziesii","basis","Nadel",E,(2,4),(2,4),(2,4),(3,3,3,3,2,2,2),4,2,[],
  "Wuchsstark und trockenheitsverträglicher als die Fichte – aber nicht heimisch.")
S("kuestentanne","Küstentanne","Abies grandis","basis","Nadel",E,(3,5),(3,5),(2,4),(2,3,3,3,3,2,2),3,2,["SCH"],
  "Sehr wuchsstark und schattenverträglich – stammt aus Nordamerika.")
S("roteiche","Roteiche","Quercus rubra","basis","Laub",E,(1,4),(2,4),(3,5),(4,3,4,4,3,3,2),3,2,[],
  "Robust, aber ihr Laub zersetzt sich schlecht – ökologisch umstritten.")
S("robinie","Robinie","Robinia pseudoacacia","basis","Laub",E,(1,3),(1,4),(3,5),(5,3,5,4,2,3,3),3,1,["PIO","BOD","INV"],
  "Extrem trockenheitsfest, aber invasiv – verändert den Boden durch Stickstoff.")
S("esskastanie","Esskastanie","Castanea sativa","basis","Laub",E,(2,3),(2,4),(4,5),(4,3,3,2,2,3,2),3,2,[],
  "Wärmeliebend, seit den Römern bei uns – Rindenkrebs droht.")
S("japanlaerche","Japanlärche","Larix kaempferi","basis","Nadel",E,(3,4),(2,4),(2,4),(2,2,3,3,4,3,2),3,1,["PIO"],
  "Schnellwüchsig und robuster als die Europäische Lärche – nicht heimisch.")
# ---------------------------------------------------------------- BASIS: Hybride & Züchtungen
S("hybridlaerche","Hybridlärche","Larix × eurolepis","basis","Nadel",Z,(2,4),(2,4),(2,4),(3,3,3,4,4,3,2),4,2,["PIO"],
  "Kreuzung aus Europäischer und Japanischer Lärche – schnell und robust.")
S("hybridpappel","Hybridpappel (z. B. ‚Max‘)","Populus × canadensis u. a.","basis","Laub",Z,(3,5),(4,5),(3,5),(2,2,3,2,3,3,2),2,2,["PIO"],
  "Extrem schnellwüchsig – für Kurzumtrieb und Biomasse, aber anspruchsvoll.")
S("hybridaspe","Hybridaspe","Populus tremula × tremuloides","basis","Laub",Z,(2,4),(3,5),(2,4),(3,2,3,3,4,3,1),2,2,["PIO"],
  "Kreuzung zweier Zitterpappeln – wächst deutlich schneller als die Espe.")
S("hybridnuss","Hybridnuss","Juglans × intermedia","basis","Laub",Z,(3,4),(4,5),(3,5),(3,3,4,3,2,3,2),5,3,[],
  "Kreuzung aus Walnuss und Schwarznuss – wertvolles Holz, wärmeliebend.")
S("resistente_esche","Resistente Esche (Zucht)","Fraxinus excelsior (selektiert)","basis","Laub",Z,(3,5),(4,5),(2,4),(2,3,3,3,3,3,2),4,3,[],
  "Auf Toleranz gegen Eschentriebsterben selektiert – Hoffnung, aber der Erfolg ist offen.")

# ---------------------------------------------------------------- NACHBARLÄNDER
N = "Nachbarland"
S("zirbe","Zirbelkiefer","Pinus cembra","nachbar","Nadel",N+" AT/CH",(2,3),(1,3),(1,1),(2,4,3,3,5,2,2),4,3,[],
  "Hochgebirgsbaum der Alpen – braucht kühle Lagen, hitzeempfindlich.")
S("schwarzkiefer","Schwarzkiefer","Pinus nigra","nachbar","Nadel",N+" AT",(1,3),(2,5),(3,5),(5,4,3,2,3,2,3),3,3,["PIO"],
  "Aus Österreich: sehr trockenheitsfest, wächst auch auf Kalk.")
S("zerreiche","Zerreiche","Quercus cerris","nachbar","Laub",N+" AT/CZ",(1,3),(2,4),(4,5),(5,4,4,4,2,4,2),3,3,[],
  "Wärme- und trockenheitsliebende Eiche aus Südosteuropa und Österreich.")
S("flaumeiche","Flaumeiche","Quercus pubescens","nachbar","Laub",N+" CH/FR",(1,2),(3,5),(4,5),(5,3,4,4,2,4,2),3,3,[],
  "Sehr trockenheitsfest und wärmeliebend – in der Schweiz und Frankreich zu Hause.")
S("mannaesche","Manna-Esche","Fraxinus ornus","nachbar","Laub",N+" AT/CH",(1,3),(3,5),(4,5),(5,3,4,4,2,3,3),3,3,[],
  "Wärmeliebende Esche der Südalpen – eine Option, aber kein 1:1-Ersatz für die Gemeine Esche.")
S("hopfenbuche","Hopfenbuche","Ostrya carpinifolia","nachbar","Laub",N+" CH/AT",(1,3),(3,5),(4,5),(5,3,4,4,2,3,3),2,3,["SCH"],
  "Südalpine Trockenheitskünstlerin mit hopfenähnlichen Früchten.")
S("seestrandkiefer","Seestrandkiefer","Pinus pinaster","nachbar","Nadel",N+" FR",(1,3),(1,3),(4,5),(4,3,3,3,1,1,2),3,3,["PIO"],
  "Aus Frankreich: Sandböden und Wärme – aber frostempfindlich und brandgefährdet.")
S("fr_ahorn","Französischer Ahorn","Acer monspessulanum","nachbar","Laub",N+" FR/CH",(1,2),(3,5),(4,5),(5,3,4,4,2,3,3),2,3,[],
  "Kleiner, sehr trockenheitsverträglicher Ahorn aus Südfrankreich.")
S("silberpappel","Silberpappel","Populus alba","nachbar","Laub",N+" AT/CZ",(3,5),(3,5),(3,5),(2,2,3,3,3,3,2),2,3,["PIO"],
  "Auwaldart aus Österreich und Tschechien – wüchsig, mit Wurzelbrut.")
S("spirke","Spirke (Bergkiefer)","Pinus mugo ssp. uncinata","nachbar","Nadel",N+" AT/CH",(2,5),(1,2),(1,2),(2,4,3,3,5,2,3),1,3,[],
  "Hoch- und Moorkiefer der Alpen – kühl, nass, nährstoffarm.")

# ---------------------------------------------------------------- WEITERE EUROPÄISCHE
EU = "Europa"
S("korkeiche","Korkeiche","Quercus suber","europa","Laub",EU+" (Iberien)",(1,3),(1,2),(5,5),(5,3,3,3,1,5,3),3,3,[],
  "Mittelmeer-Eiche mit feuerfester Borke – sehr frostempfindlich.")
S("steineiche","Steineiche","Quercus ilex","europa","Laub",EU+" (Mittelmeer)",(1,2),(2,4),(5,5),(5,3,4,4,1,4,3),3,3,[],
  "Immergrüne Mittelmeereiche – braucht milde Winter.")
S("ungar_eiche","Ungarische Eiche","Quercus frainetto","europa","Laub",EU+" (Balkan)",(1,3),(2,4),(4,5),(5,4,4,4,2,4,2),4,3,[],
  "Wärmeliebende Eiche vom Balkan – sehr trockenheitsfest.")
S("rumel_kiefer","Rumelische Kiefer","Pinus peuce","europa","Nadel",EU+" (Balkan)",(3,4),(2,3),(1,3),(2,4,4,4,5,2,2),3,3,[],
  "Balkan-Kiefer, frosthart und stabil – bevorzugt frische Lagen.")
S("aleppokiefer","Aleppokiefer","Pinus halepensis","europa","Nadel",EU+" (Mittelmeer)",(1,2),(1,4),(5,5),(5,3,3,3,1,1,2),2,3,["PIO"],
  "Mittelmeerkiefer: sehr hitze- und trockenheitsfest, aber nicht frosthart und hoch brandgefährdet.")
S("orientbuche","Orientbuche","Fagus orientalis","europa","Laub",EU+" (Kaukasus/Balkan)",(3,4),(3,5),(3,5),(3,3,4,3,2,4,2),3,3,["SCH"],
  "Östliche Schwester der Rotbuche – kommt womöglich besser mit Wärme klar.")
S("silberlinde","Silberlinde","Tilia tomentosa","europa","Laub",EU+" (Balkan/Ungarn)",(1,3),(3,5),(4,5),(5,4,4,4,2,4,2),2,3,["SCH","BOD"],
  "Balkan-Linde, hitze- und trockenheitsverträglich – ein „Klimabaum“.")
S("walnuss","Walnuss","Juglans regia","europa","Laub",EU+" (Südosteuropa)",(2,4),(4,5),(4,5),(3,3,4,3,1,3,2),5,3,[],
  "Wärmeliebendes Wertholz aus Südosteuropa – spätfrostgefährdet.")
S("nordmanntanne","Nordmanntanne","Abies nordmanniana","europa","Nadel",EU+" (Kaukasus)",(3,4),(3,5),(3,5),(3,4,4,3,2,3,1),3,3,["SCH"],
  "Kaukasus-Tanne: wärme- und trockenheitsverträglicher als die Weißtanne.")
S("serb_fichte","Serbische Fichte","Picea omorika","europa","Nadel",EU+" (Balkan)",(2,4),(2,5),(2,4),(3,3,2,3,4,2,2),3,3,[],
  "Balkan-Fichte: kommt mit Trockenheit besser klar als unsere Fichte.")
S("schmal_esche","Schmalblättrige Esche","Fraxinus angustifolia","europa","Laub",EU+" (Südosteuropa)",(3,5),(3,5),(4,5),(3,3,3,2,2,3,2),3,3,[],
  "Südosteuropäische Esche für warme Auenstandorte.")
S("zuergelbaum","Zürgelbaum","Celtis australis","europa","Laub",EU+" (Mittelmeer)",(1,2),(2,4),(5,5),(5,3,4,4,1,3,3),2,3,[],
  "Mittelmeerbaum mit extremer Trockenheitstoleranz – nur an sehr warmen Orten.")
S("baumhasel","Baumhasel","Corylus colurna","europa","Laub",EU+" (Südosteuropa/Türkei)",(2,4),(3,5),(3,5),(4,4,5,4,4,3,3),3,3,[],
  "Robuster, trockenheitsfester Stadt- und Forstbaum aus Südosteuropa.")

# ---------------------------------------------------------------- WELT
WE = "Welt"
S("riesenmammut","Riesenmammutbaum","Sequoiadendron giganteum","welt","Nadel",WE+" (Kalifornien)",(3,4),(3,4),(3,4),(3,4,5,4,2,5,3),3,4,[],
  "Kalifornischer Riese: dicke Borke, feuerfest, wuchsstark bei Wärme.")
S("kuestenmammut","Küstenmammutbaum","Sequoia sempervirens","welt","Nadel",WE+" (Kalifornien)",(4,5),(3,5),(4,5),(2,3,5,4,1,4,3),3,4,[],
  "Kalifornische Küste: braucht Nebel und milde Winter, hier frostgefährdet.")
S("atlaszeder","Atlaszeder","Cedrus atlantica","welt","Nadel",WE+" (Nordafrika)",(1,3),(2,5),(4,5),(5,4,4,4,2,3,2),3,4,[],
  "Aus dem Atlasgebirge: extrem trockenheitsfest.")
S("libanonzeder","Libanonzeder","Cedrus libani","welt","Nadel",WE+" (Libanon/Türkei)",(1,3),(2,5),(3,5),(5,4,4,4,3,3,2),4,4,[],
  "Gebirgsbaum aus dem Taurus: trockenheits- und mäßig frostfest.")
S("thuja","Riesenlebensbaum","Thuja plicata","welt","Nadel",WE+" (Nordamerika)",(3,5),(3,5),(2,4),(2,4,5,4,3,2,2),4,4,["SCH"],
  "Schattentolerant, rasch wachsend, sehr dauerhaftes Holz.")
S("sitkafichte","Sitkafichte","Picea sitchensis","welt","Nadel",WE+" (Nordamerika)",(4,5),(2,4),(1,3),(1,2,2,3,3,2,2),3,4,[],
  "Küstenbaum Nordamerikas: braucht viel Regen – hier nur im Norden/Westen.")
S("gelbkiefer","Gelbkiefer","Pinus ponderosa","welt","Nadel",WE+" (Nordamerika)",(1,3),(1,4),(3,5),(5,3,2,3,3,4,2),3,4,["PIO"],
  "Trockenheitsfeste Kiefer aus dem Westen Nordamerikas.")
S("strobe","Weymouthskiefer","Pinus strobus","welt","Nadel",WE+" (Nordamerika)",(3,4),(2,4),(2,4),(2,3,3,1,4,2,2),3,4,[],
  "Wüchsig, aber der Blasenrost bedroht sie stark.")
S("schwarznuss","Schwarznuss","Juglans nigra","welt","Laub",WE+" (Nordamerika)",(3,4),(4,5),(3,5),(3,3,4,4,2,3,2),5,4,[],
  "Wertholz aus Nordamerika – braucht tiefgründige, nährstoffreiche Böden.")
S("tulpenbaum","Tulpenbaum","Liriodendron tulipifera","welt","Laub",WE+" (Nordamerika)",(3,4),(3,5),(3,5),(3,3,4,4,3,3,2),3,4,[],
  "Hochwachsend und wüchsig – mag Wärme und tiefe Böden.")
S("gleditschie","Gleditschie","Gleditsia triacanthos","welt","Laub",WE+" (Nordamerika)",(1,4),(2,5),(3,5),(5,3,4,4,3,3,3),3,4,[],
  "Trocken- und salztolerant – bewehrt mit Dornen.")
S("sumpfeiche","Sumpfeiche","Quercus palustris","welt","Laub",WE+" (Nordamerika)",(4,5),(2,4),(3,5),(2,3,4,4,3,3,2),3,4,[],
  "Nordamerikanische Eiche für nasse Böden.")
S("paulownia","Blauglockenbaum","Paulownia tomentosa","welt","Laub",WE+" (Ostasien)",(3,4),(4,5),(4,5),(2,1,4,3,1,3,2),2,4,["PIO","INV"],
  "Ostasiatischer Schnellwuchsbaum – sehr frostempfindlich, invasiv.")
S("goetterbaum","Götterbaum","Ailanthus altissima","welt","Laub",WE+" (Ostasien)",(1,3),(1,5),(3,5),(5,2,5,4,2,3,5),1,4,["PIO","INV"],
  "Extrem anpassungsfähig – gilt als invasive Problemart.")
S("traubenkirsche","Spätblühende Traubenkirsche","Prunus serotina","welt","Laub",WE+" (Nordamerika)",(2,4),(1,3),(2,5),(4,3,5,4,4,3,5),1,4,["SCH","INV"],
  "In Brandenburgs Kiefernforsten zur Problemart geworden.")
S("eukalyptus","Mostgummibaum (Eukalyptus)","Eucalyptus gunnii","welt","Laub",WE+" (Australien)",(3,4),(2,4),(4,5),(3,2,4,4,2,1,3),2,4,["PIO"],
  "Frostresistentester Eukalyptus – in Mitteleuropa nur experimentell.")
S("radiata","Monterey-Kiefer","Pinus radiata","welt","Nadel",WE+" (Kalifornien)",(2,4),(2,4),(5,5),(3,2,3,3,1,1,2),3,4,["PIO"],
  "Weltweit häufigste Plantagenkiefer – frostempfindlich.")

# ---------------------------------------------------------------- Ergänzungen v0.4 (Alpen & Auen)
S("grauerle","Grauerle","Alnus incana","basis","Laub",H,(3,5),(2,4),(1,3),(2,3,4,3,4,2,3),1,1,["PIO","BOD"],
  "Pionier der Gebirgsbäche und Alpentäler – bindet wie alle Erlen Stickstoff.")
S("bergulme","Bergulme","Ulmus glabra","basis","Laub",H,(3,5),(4,5),(1,3),(2,3,3,1,3,3,2),4,2,[],
  "Braucht kühle, frische Schluchtwälder – das Ulmensterben setzt ihr stark zu.")
S("latsche","Latsche (Bergkiefer)","Pinus mugo","basis","Nadel",H,(2,4),(1,3),(1,1),(3,4,4,4,5,2,3),1,1,["PIO"],
  "Strauchförmige Kiefer der Hochlagen – schützt vor Lawinen und Erosion.")
S("sommerlinde","Sommerlinde","Tilia platyphyllos","basis","Laub",H,(2,4),(3,5),(2,4),(3,4,4,4,3,4,2),2,2,["SCH","BOD"],
  "Etwas feuchtigkeitsliebender als die Winterlinde – gute Humusbildnerin.")

SPECIES = {s["id"]: s for s in _S}
SPECIES_LIST = _S

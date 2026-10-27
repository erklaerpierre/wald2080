# -*- coding: utf-8 -*-
"""BASISSATZ · Fachkarten. Gilt für ALLE Editionen."""

# ============================================================== FACHKARTEN
# name, Kosten (T€), Effekt, Anzahl im Stapel, Lehrsatz
FACH = [
    ("Pheromonfalle", 1, "Käfer- und Pilz-Proben +2 für 1 Feld in dieser Runde. Das Feld steckt keine Nachbarn an.", 2, "Monitoring und Fallen helfen beim Schadensmanagement."),
    ("Wildschutz-Zaun", 1, "Verbiss-Proben +3 für 1 Feld in dieser Runde.", 2, "Schutz ist günstiger als Neupflanzung."),
    ("Brandschneise", 1, "Feuer-Proben +2 für 1 Feld in dieser Runde.", 2, "Schneisen und Wasserstellen sind Vorsorge."),
    ("Schirmstellung", 0, "Pflanze 1 Mischbaum ohne Jungwuchs-Malus (Schattenbaum-Effekt).", 2, "Der Altbestand schützt die Jungpflanzen."),
    ("Bodenschutzkalkung", 2, "1 Feld: Nährstoffe +1 bis Spielende (max. 5).", 1, "Kalkung gleicht saure Böden aus."),
    ("Saatguttausch", 0, "Tausche 1 Baumkarte mit einem anderen Team oder nimm 1 Karte aus der Saatgutbörse.", 2, "Saatgut wird international gehandelt."),
    ("Forstamts-Beratung", 0, "Sieh dir die verdeckte Ereigniskarte dieser Runde an und sag es allen.", 2, "Beratung und Prognosen verbessern Entscheidungen."),
    ("Gemeinschaftswerk", 0, "Gib bis zu 2 T€ in den Fördertopf oder nimm bis zu 2 T€ heraus.", 2, "Zusammenarbeit zwischen Revieren."),
    ("Rückegassen-Konzept", 0, "Eine Kahlfläche verursacht in dieser Bilanz keinen Stabilitätsverlust.", 1, "Bodenschutz bei der Holzernte."),
    ("Habitatbaum markieren", 0, "+1 Stabilität (Biodiversität).", 2, "Alt- und Totholz sind Lebensraum."),
    ("Sofort-Aufarbeitung", 1, "Wähle 1 Feld: Der Schaden dieser Runde (Sturm, Käfer, Pilz) wird um 1 Herz verringert.", 2, "Schnelles Handeln begrenzt Folgeschäden."),
    ("Zuchtprogramm", 0, "Pflanzkosten für Züchtungen und Hybride sind in dieser Runde −1 T€ (min. 0).", 1, "Forstpflanzenzüchtung als Chance."),
    ("Holz-Vorverkauf", 0, "Du erhältst sofort +2 T€.", 2, "Vorverträge sichern Einnahmen."),
    ("Praktikumstag", 0, "1 Pflege (Durchforstung) in dieser Runde kostenlos.", 1, "Ausbildung und Praxis zusammen."),
    ("Naturverjüngung", 0, "1 Kahlfläche neben einem Feld mit 3 Herzen: Lege dort dieselbe Baumart gratis als Hauptbaum (2 Herzen).", 2, "Naturverjüngung ist der günstigste Waldumbau."),
]

# -*- coding: utf-8 -*-
import os, sys, csv, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
from data import *
import sim
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
GREEN = "#2E7D32"

H1 = ParagraphStyle("H1", fontName="DVB", fontSize=22, leading=26, textColor=hc(GREEN), spaceAfter=2)
SUB = ParagraphStyle("SUB", fontName="DVC", fontSize=10.5, leading=14, textColor=hc("#546E7A"), spaceAfter=8)
H2 = ParagraphStyle("H2", fontName="DVB", fontSize=12.5, leading=16, textColor=hc(GREEN), spaceBefore=9, spaceAfter=3)
BODY = ParagraphStyle("B", fontName="DV", fontSize=9, leading=12.6, textColor=hc("#263238"), spaceAfter=3)
BUL = ParagraphStyle("BUL", parent=BODY, leftIndent=11, bulletIndent=2, spaceAfter=1.5)
SMALL = ParagraphStyle("S", fontName="DVC", fontSize=7.6, leading=9.4, textColor=hc("#37474F"))
SMALLB = ParagraphStyle("SB", parent=SMALL, fontName="DVCB")
CELL = ParagraphStyle("C", fontName="DVC", fontSize=8.2, leading=10.2, textColor=hc("#263238"))
CELLB = ParagraphStyle("CB", parent=CELL, fontName="DVCB")
BOXS = ParagraphStyle("BOX", parent=BODY, fontName="DV", fontSize=8.8, leading=12)


def P(t, s=BODY): return Paragraph(t, s)
def B(t): return Paragraph(t, BUL, bulletText="•")


def tbl(data, widths, head=True, zebra=True, font=CELL, hbg=GREEN):
    rows = [[Paragraph(str(c), CELLB if (head and i == 0) else font) if not hasattr(c, "wrap") else c
             for c in r] for i, r in enumerate(data)]
    t = Table(rows, colWidths=[w * mm for w in widths], repeatRows=1 if head else 0)
    st = [("VALIGN", (0, 0), (-1, -1), "TOP"), ("GRID", (0, 0), (-1, -1), 0.3, hc("#CFD8DC")),
          ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3),
          ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]
    if head:
        st += [("BACKGROUND", (0, 0), (-1, 0), hc(hbg))]
        for j in range(len(data[0])):
            rows[0][j] = Paragraph(f'<font color="#FFFFFF">{data[0][j]}</font>', CELLB)
        t = Table(rows, colWidths=[w * mm for w in widths], repeatRows=1)
    if zebra:
        for i in range(1, len(data)):
            if i % 2 == 0: st.append(("BACKGROUND", (0, i), (-1, i), hc("#F5F7F8")))
    t.setStyle(TableStyle(st))
    return t


def box(text_flowables, bg="#E8F5E9", border="#A5D6A7", w=174):
    t = Table([[text_flowables]], colWidths=[w * mm])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), hc(bg)), ("BOX", (0, 0), (-1, -1), 0.6, hc(border)),
                           ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                           ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    return t


def balance_table():
    """Simulationsergebnisse (Basis-Karten) für das Dokument."""
    N = 1200
    out = []
    for label, rounds, nf, ziel in (("Kurz (3 Felder, 3 Runden)", 3, 3, 12), ("Standard (7 Felder, 6 Runden)", 6, 7, 12),
                                    ("Lang (7 Felder, 8 Runden)", 8, 7, 14)):
        for region in ("BW", "BY", "BB"):
            row = [label if region == "BW" else "", region]
            for strat in ("passiv", "zufall", "solide", "smart"):
                res = [sim.play(region, strat, rounds, seed=i, nfields=nf)[0] for i in range(N)]
                row.append(f"{100 * sum(1 for x in res if x >= ziel) / N:.0f} %")
            out.append(row)
    return out


def footer(canv, doc):
    canv.saveState()
    canv.setFont("DVC", 7); canv.setFillColor(hc("#90A4AE"))
    canv.drawString(18 * mm, 10 * mm, "Wald 2080 · Regelheft v0.4 (Entwurf) · Spielwerte didaktisch vereinfacht – fachliche Prüfung empfohlen")
    canv.drawRightString(192 * mm, 10 * mm, f"Seite {doc.page}")
    canv.restoreState()


def regelheft():
    fn = f"{OUT}/01_Regelheft.pdf"
    doc = BaseDocTemplate(fn, pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm, bottomMargin=17 * mm,
                          title="Wald 2080 – Regelheft", author="Wald 2080")
    doc.addPageTemplates([PageTemplate(id="p", frames=[Frame(18 * mm, 17 * mm, 174 * mm, 264 * mm, id="f", leftPadding=0,
                                                              rightPadding=0, topPadding=0, bottomPadding=0)], onPage=footer)])
    n_events = len([e for e in EVENTS if e["kind"] in RES_KEYS]); n_good = len(GUTE)
    n_reg = len(REGIONEN); n_st = len(STANDORTE)
    n_basis = len([s for s in SPECIES_LIST if s["deck"] == "basis"])
    S = []
    S += [P("WALD 2080", H1),
          P("Das kooperative Waldumbau-Spiel für Auszubildende zur Forstwirtin / zum Forstwirt · 1–25 Personen · 10–120 Minuten · drinnen", SUB)]
    S += [box([P("<b>Euer Auftrag:</b> Ihr bewirtschaftet gemeinsam einen Forstbetrieb. Von heute (2030) bis 2080 oder 2100 "
                 "bringen Klimawandel, Stürme, Käfer, Pilze, Feuer und Wild euren Wald unter Druck. Ihr spielt <b>nicht gegeneinander</b>, "
                 "sondern <b>alle zusammen gegen die Ereigniskarten</b>. Gewonnen habt ihr, wenn die Reviere am Ende stabil genug sind.", BOXS)])]
    S += [P("1  Material", H2)]
    S += [tbl([["Material", "Menge", "Datei"],
               ["Baumkarten Basis (heimisch, etabliert, Züchtungen) – Vorder- und Rückseite (Foto + Verbreitungskarte)", f"{n_basis} Karten – 1 Set je Team", "02_Baumkarten_Basis"],
               ["Baumkarten Erweiterungen (Nachbarländer 10 · Europa 13 · Welt 17)", "1 Set je Klasse („Saatgutbörse“)", "03 – 05"],
               [f"Standortkarten – {n_st} Karten in {n_reg} Editionen (16 Bundesländer DE, 9 Bundesländer AT, 6 Regionen CH)", "Eine Edition (Region) je Spielrunde, 1 Set je Team", "Editionen/ (je Region) · 06_Standortkarten_alle"],
               ["Ereigniskarten (mit einheitlicher Rückseite)", f"{len(EVENTS)} Karten – 1 Stapel je Klasse", "07_Ereigniskarten"],
               ["Fachkarten", f"{sum(f[3] for f in FACH)} Karten – 1 Stapel je Klasse", "08_Fachkarten"],
               ["Revierplan A3 (Vorderseite Plan, Rückseite Spickzettel)", "1 je Team (am besten laminieren)", "09_Revierplan_A3"],
               ["Leitstelle A3 (Runden, Klima, Ereignisse, Stabilitätstabelle)", "1 je Klasse", "10_Leitstelle_A3"],
               ["Baum-Etiketten (2 je Art, Vorderseite Name – Rückseite Foto)", "1 Seitenpaar je Team", "11_Baum-Etiketten"],
               ["Würfel W6 (einer für die ganze Klasse) · Münzen für Herzen und Kasse · Marker", "je Team ca. 25 Münzen", "–"]],
              [80, 56, 38])]
    S += [P("2  Formate und Gruppengrößen", H2)]
    S += [tbl([["Format", "Dauer", "Revier", "Runden", "Ziel (SP)"],
               ["Kurz (Schnupperspiel)", "10–20 Min.", "3 Felder (1, 2, 3)", "3 Runden: 2030 · 2050 · 2080", "12"],
               ["Standard", "45–60 Min.", "7 Felder", "6 Runden: 2030 bis 2080", "12"],
               ["Lang", "90–120 Min.", "7 Felder + Erweiterungen", "8 Runden: 2030 bis 2100", "14"]],
              [34, 24, 40, 56, 20])]
    S += [Spacer(1, 3), P("<b>Gruppengrößen:</b> 1–5 Personen spielen ein Revier gemeinsam. Ab 6 Personen bilden sich Teams zu je 3–5 Personen "
                          "(2–5 Reviere); eine ganze Klasse mit 25 Personen spielt also 5 Reviere zu je 5 Personen. Optionale Rollen im Team: "
                          "<i>Revierleitung</i> (moderiert), <i>Standortkunde</i> (liest Eignung), <i>Waldschutz</i> (Proben), "
                          "<i>Finanzen</i> (Kasse). Der Einzelspieler-Modus folgt in einer späteren Version.")]
    S += [P("3  Aufbau", H2)]
    for t in [f"<b>Edition wählen:</b> Eines der {n_reg} Bundesländer bzw. Regionen aus Deutschland, Österreich oder der Schweiz (Ordner „Editionen“). Jede Edition hat einen Steckbrief mit Standorten, typischen Baumarten und regionalem Gefahrenzuschlag.",
              "<b>Reviere anlegen:</b> Jedes Team legt seinen Revierplan aus, zieht zufällig 7 Standortkarten (Kurzspiel: 3) der Region und legt sie in die Slots 1–7.",
              "<b>Ausgangsbestand:</b> Auf jedem Feld steht die auf der Standortkarte genannte Baumart als Reinbestand mit 3 Herzen. "
              "Legt dazu ein Baum-Etikett als Hauptbaumart auf das Feld und drei Münzen auf die Herzen.",
              "<b>Startwerte:</b> Stabilität (SP) 8, Kasse 4 T€ (Tausend Euro). Rundenmarker auf 2030, Klimastufe 0.",
              f"<b>Ereignisstapel bauen:</b> Aus {n_events} Schadenskarten und {n_good} Glücks-/Klimakarten zufällig auswählen: "
              "Kurz 5+1, Standard 10+2, Lang 13+3 Karten. Mischen und auf die Leitstelle legen.",
              "<b>Fachkarten</b> mischen, jedes Team zieht 1 Karte. <b>Baumkarten:</b> Das Basis-Set liegt offen beim Team. "
              "Die Erweiterungskarten liegen in der Mitte (Saatgutbörse)."]:
        S.append(B(t))
    S += [P("4  Eine Runde = ein Jahrzehnt", H2)]
    S += [tbl([["Phase", "Was passiert"],
               ["A  Vorschau", "Oberste Ereigniskarte aufdecken – eure <b>Vorwarnung</b>. Die zweite bleibt verdeckt. Klimastufe der Runde prüfen."],
               ["B  Einnahmen", "Jedes Revier erhält +3 T€. Jedes Team zieht 1 Fachkarte (maximal 3 auf der Hand)."],
               ["C  Planen & Handeln", "Gemeinsam beraten (Teams dürfen sich absprechen, tauschen und Münzen weitergeben), dann Maßnahmen umsetzen."],
               ["D  Ereignisse", "Beide Karten nacheinander. Eine Person würfelt den W6 <b>für die ganze Klasse</b>. Jedes Team prüft seine Felder."],
               ["E  Bilanz", "Erholung, Jungwuchs endet, Stabilität (SP) berechnen. Rundenmarker weiter."]],
              [36, 138])]
    S += [Spacer(1, 4), P("<b>Maßnahmen in Phase C</b>")]
    S += [tbl([["Maßnahme", "Kosten", "Wirkung"],
               ["Pflanzen (Hauptbaumart)", "Kosten auf der Baumkarte", "Nur auf Kahlfläche. Feld erhält 2 Herzen und ist Jungwuchs."],
               ["Mischbaum ergänzen", "Kosten auf der Baumkarte", "Feld mit mindestens 1 Herz, noch ohne Mischbaum. Mischbaum ist Jungwuchs."],
               ["Pflege / Durchforstung", "1 T€", "+1 Herz auf einem Feld (maximal 3)."],
               ["Wildschutz", "1 T€", "Verbiss-Proben +2 auf einem Feld in dieser Runde."],
               ["Nutzung (Ernte)", "–", "Feld mit mindestens 2 Herzen: Einnahme = Holzwert der Hauptbaumart (+1 bei 3 Herzen). Danach Kahlfläche, Karten ablegen."],
               ["Fachkarte ausspielen", "Kosten auf der Karte", "Wirkung steht auf der Karte, danach ablegen."]],
              [38, 40, 96])]
    S += [P("5  Die Probe: Wie wirkt ein Ereignis?", H2)]
    S += [P("Jede Ereigniskarte nennt die <b>Stärke</b>, die <b>betroffenen Felder</b> und den <b>Widerstandswert</b>, gegen den geprüft wird "
            "(Dürre, Sturm, Käfer, Pilze, Frost, Feuer oder Verbiss). Für jedes betroffene Feld rechnet ihr:")]
    S += [box([P("<b>W6 + Widerstandswert + Eignungsbonus + Standort-Modifikator − Jungwuchs ≥ Stärke</b>", BOXS)], "#FFFDE7", "#FBC02D")]
    S += [Spacer(1, 3)]
    for t in ["<b>Eignung E:</b> Zählt, wie viele der drei Achsen (Wasser, Nährstoffe, Wärme) im markierten Bereich der Baumkarte liegen – "
              "<b>mit aktueller Klimastufe</b>: Wärme +Stufe (max. 5), Wasser −Stufe/2 (abgerundet, min. 1). "
              "E 3 = +2 · E 2 = 0 · E 1 = −2 · E 0 = −4 (nicht pflanzbar).",
              "<b>Standort-Modifikator:</b> Steht auf der Standortkarte (z. B. „Dürre −1“).",
              "<b>Jungwuchs:</b> −1 für frisch gepflanzte Bäume in der Pflanzrunde. Pionierarten nie; Schattenbaumarten nicht als Mischbaum.",
              "<b>Mischbestand – ein Wurf, zwei Bäume:</b> Das Feld verliert nur dann Herzen, wenn <b>beide</b> Baumarten die Probe verfehlen. "
              "Ist die Mischbaumart vom Ereignis gar nicht betroffen (z. B. Käfer an Fichte, aber Buche daneben), rettet sie das Feld.",
              "<b>Verfehlt:</b> −1 Herz. Um 4 oder mehr verfehlt: −2 Herzen. Bei 0 Herzen ist das Feld eine <b>Kahlfläche</b>: Baumkarten ablegen.",
              "<b>Befallskette</b> (Käfer, Pilze mit dem Hinweis auf der Karte): Gleiche Reinbestände neben einem geschädigten Feld werden mit −1 "
              "erneut geprüft – so lange, bis nichts Neues passiert. Mischbestände bremsen die Kette.",
              "<b>Klimazuschlag:</b> Ab Klimastufe 2 haben Dürre-, Käfer- und Feuerereignisse +1 Stärke. <b>Regionaler Zuschlag:</b> Der Steckbrief der Edition kann zusätzlich für einzelne Ereignisarten die Stärke dauerhaft anheben (z. B. Dürre und Feuer in Brandenburg) oder – in nassen Alpenregionen – senken."]:
        S.append(B(t))
    S += [Spacer(1, 4)]
    S += [KeepTogether([P("<b>Beispiel (Klimastufe 1, Jahr 2050):</b> Feld „Albtrauf-Südhang“ (Wasser 1, Nährstoffe 3, Wärme 4 → mit Klima Wärme 5; "
                          "Standort: Dürre −1, Feuer −1). Dort steht eine <b>Rotbuche</b> (Wasser 3–4 ✗, Nährstoffe 3–5 ✓, Wärme 2–4 ✗) → E = 1, Bonus −2. "
                          "Ereignis <i>Trockensommer</i>, Stärke 7, Wurf 4: 4 + 2 (Dürre) − 2 (E) − 1 (Standort) = 3. Verfehlt um 4 → <b>−2 Herzen</b>. "
                          "Hätte das Team zuvor eine <b>Mehlbeere</b> als Mischbaum ergänzt (E 3 → +2, Dürre 5, Jungwuchs −1): 4 + 5 + 2 − 1 − 1 = 9 ≥ 7 → "
                          "<b>Feld gerettet</b>. Genau das ist Waldumbau.", SMALL)])]
    S += [P("6  Bilanz, Ziel und Notfallhilfe", H2)]
    S += [P("<b>Bilanz am Ende jeder Runde</b> (pro Revier):")]
    for t in ["<b>Erholung:</b> Felder mit 1–2 Herzen und voller Eignung (E 3) erhalten +1 Herz.",
              "<b>−2 SP</b> je Kahlfläche · <b>−1 SP</b> je Feld mit nur 1 Herz · <b>−1 SP</b> je Feld mit invasiver Art.",
              "<b>+1 SP</b>, wenn mindestens die Hälfte der Felder Mischbestand mit mindestens 2 Herzen hat.",
              "<b>+1 SP</b>, wenn mindestens 5 verschiedene nicht-invasive Baumarten im Revier stehen.",
              "Jungwuchs-, Schutz- und Befall-Marker entfernen. SP bleibt zwischen 0 und 20."]:
        S.append(B(t))
    S += [Spacer(1, 3), box([P("<b>Gewonnen:</b> Nach der letzten Runde erreicht der <b>Durchschnitt aller Reviere</b> das Ziel (Kurz und Standard: 12 SP, "
                               "Lang: 14 SP) und <b>kein Revier steht bei 0 SP</b>.<br/><b>Kollaps:</b> Ein Revier bei 0 SP ist kollabiert. Die anderen Teams "
                               "dürfen es retten: Je 2 T€ aus eigener Kasse oder dem Fördertopf ergeben +1 SP. "
                               "<b>Verloren:</b> Mehr als die Hälfte der Reviere kollabiert oder das Ziel wird verfehlt.", BOXS)], "#E8F5E9", "#A5D6A7")]
    S += [P("7  Erweiterungen und Varianten", H2)]
    for t in ["<b>Saatgutbörse:</b> Die Erweiterungsdecks (Nachbarländer, Europa, Welt) liegen in der Mitte. Wer eine Art pflanzen will, holt sich die Karte "
              "und legt sie danach zurück. Erweiterungsarten sind teurer (3–4 T€), bringen aber oft die passende Eignung für Klimastufe 2–3.",
              "<b>Invasive Arten</b> (Robinie, Götterbaum, Blauglockenbaum, Spätblühende Traubenkirsche) sind robust, kosten aber Stabilität. "
              "Sie zählen nicht für die Artenvielfalt.",
              "<b>Eigene Editionen:</b> Der Basissatz (Baumarten, Ereignisse, Fachkarten) gilt überall; lokale Besonderheiten stehen in einer eigenen Datei je Region (siehe LIESMICH). So lässt sich eine neue Edition anlegen, ohne andere zu berühren.",
              "<b>Später geplant:</b> Einzelspieler-Modus, Outdoor-Variante im Gelände, zweiter Schwierigkeitsgrad."]:
        S.append(B(t))
    S += [P("8  Was lernen die Auszubildenden hier?", H2)]
    S += [tbl([["Spielmechanik", "Lernziel"],
               ["Eignung E (Wasser, Nährstoffe, Wärme)", "Standortansprüche der Baumarten lesen und auf Standorte anwenden."],
               ["Klimastufen", "Eignung ist nicht statisch: Was heute passt, kann 2060 am Limit sein."],
               ["Widerstandswerte und Ereignisse", "Risiken kennen: Dürre, Sturm, Käfer, Pilze, Frost, Feuer, Verbiss."],
               ["Mischbestand und Befallskette", "Risikostreuung: Warum Reinbestände sich gegenseitig anstecken."],
               ["Kasse, Ernte, Förderung", "Waldumbau finanzieren: Ernte, Pflanzkosten, Fördermittel abwägen."],
               ["Invasive Arten, Erweiterungsdecks", "Chancen und Risiken von Gastbaumarten, Herkünften und Züchtungen."]],
              [62, 112])]
    S += [Spacer(1, 4), P("<b>Reflexionsfragen für die Nachbesprechung (10–15 Min.):</b>")]
    for t in ["Welche Baumarten haben euren Wald gerettet, welche haben euch überrascht?",
              "Wo habt ihr Reinbestände umgebaut, und wann war der richtige Zeitpunkt?",
              "Welche Ereignisse waren vorhersehbar, welche nicht? Was hätte eine bessere Vorbereitung gebracht?",
              "Was würdet ihr in eurem Ausbildungsbetrieb als Erstes ändern? Was ist dort tatsächlich möglich?"]:
        S.append(B(t))
    S += [PageBreak(), P("Hinweise für die Spielleitung", H2)]
    S += [P("<b>Balance-Test (Simulation):</b> Je 1.200 simulierte Spiele pro Zelle mit den Basiskarten. Angegeben ist der Anteil Revier-Endstände, "
            "die das Ziel erreichen. <b>Passiv</b>: ersetzt nur Kahlflächen durch den Ausgangsbaum. <b>Zufällig</b>: pflanzt ohne Plan. "
            "<b>Solide</b>: plant standortgerecht (Umbau, Mischung, Vielfalt), kennt aber nur knapp die Hälfte der Arten. "
            "<b>Optimal</b>: Computerstrategie mit voller Regel- und Artenkenntnis, also die Obergrenze.")]
    rows = [["Format", "Region", "passiv", "zufällig", "solide", "optimal"]] + balance_table()
    S += [tbl(rows, [58, 20, 24, 24, 24, 24]), Spacer(1, 3)]
    S += [P("<b>Einordnung:</b> Kooperative Spiele werden meist so ausgelegt, dass erfahrene Gruppen mit guter Strategie etwa 50–70 % gewinnen. "
            "Hier liegt das bei „solide“ im Standard- und Langspiel in diesem Bereich; das Kurzspiel ist als Einstieg bewusst etwas leichter. "
            "Reines Abwarten oder Raten führt fast nie zum Sieg. Ein Klassenteam mit wenig Vorerfahrung wird erfahrungsgemäß darunter liegen.", SMALL)]
    sim.SOFF = 0
    st = [["Stellschraube (Standardspiel, Region BW, „solide“)", "Ziel 10 SP", "Ziel 12 SP (Standard)", "Ziel 14 SP"]]
    row = ["Gewinnquote"]
    for z in (10, 12, 14):
        res = [sim.play("BW", "solide", 6, seed=i, nfields=7)[0] for i in range(1200)]
        row.append(f"{100 * sum(1 for x in res if x >= z) / 1200:.0f} %")
    st.append(row)
    S += [Spacer(1, 3), tbl(st, [78, 30, 36, 30]), Spacer(1, 2)]
    S += [P("Weitere Stellschrauben: Startkapital und Einkommen (4 T€ / +3 T€), Zahl der Schadenskarten im Stapel, Regionszuschläge. "
            "Für Gruppen, die es leichter möchten: Ziel um 2 SP senken. Für Fortgeschrittene: Ziel erhöhen oder Erweiterungsdecks nur eingeschränkt zulassen.", SMALL)]
    S += [P("<b>Fachliche Hinweise:</b> Alle Spielwerte (Standortbereiche 1–5, Widerstandswerte 1–5, Holzwerte, Kosten) sind <b>didaktisch vereinfacht</b>. "
            "Sie orientieren sich an gängigen forstlichen Standortansprüchen, ersetzen aber keine Standortkartierung oder Baumartenempfehlung "
            "(z. B. FVA Baden-Württemberg, LWF Bayern, LFE Brandenburg). Vor dem Einsatz im Unterricht empfehlen wir eine fachliche Durchsicht durch Ausbilder:innen. "
            "Tropische Baumarten sind bewusst nicht enthalten, weil sie in der Klimaspanne bis 2100 keine Rolle spielen.", SMALL)]
    S += [Spacer(1, 4), P("<b>Druckhinweise:</b> Karten im Format 63 × 88 mm (Standortkarten 45 × 63 mm, Etiketten 26 × 12 mm) auf 200–250 g Papier drucken, "
                          "auf Wunsch in Kartenhüllen stecken. A3-Pläne laminieren und mit abwischbaren Stiften nutzen. "
                          "Alle Kartenbögen haben 2 mm Anschnitt und Schneidemarken: Die Farbe läuft über die Schnittkante, es bleibt kein weißer Rand. Entlang der Marken schneiden, Ecken mit dem Eckenrunder (Radius 3–3,5 mm) abrunden. Karten mit Rückseite <b>beidseitig auf A4 drucken, Wenden an der langen Kante</b> – die Rückseiten sind spaltengespiegelt (3 2 1), sodass Vorder- und Rückseite genau übereinander liegen. Vor dem Massendruck eine Probeseite prüfen. Bei Klassenspielen: Basis-Baumkarten und Standortkarten je Team einmal drucken.", SMALL)]
    doc.build(S)


def uebersicht():
    fn = f"{OUT}/12_Spielleitung_Uebersicht.pdf"
    doc = BaseDocTemplate(fn, pagesize=landscape(A4), leftMargin=10 * mm, rightMargin=10 * mm, topMargin=12 * mm, bottomMargin=12 * mm,
                          title="Wald 2080 – Übersicht Baumarten & Standorte")
    def foot(c, d):
        c.saveState(); c.setFont("DVC", 7); c.setFillColor(hc("#90A4AE"))
        c.drawString(10 * mm, 6 * mm, "Wald 2080 · Spielleitung · Übersicht der Spielwerte (didaktisch vereinfacht)")
        c.drawRightString(287 * mm, 6 * mm, f"Seite {d.page}"); c.restoreState()
    doc.addPageTemplates([PageTemplate(id="p", frames=[Frame(10 * mm, 12 * mm, 277 * mm, 186 * mm, id="f", leftPadding=0, rightPadding=0,
                                                              topPadding=0, bottomPadding=0)], onPage=foot)])
    import balancing
    bal = balancing.lade()
    S = [P("Editionen im Überblick", H1), P("31 Editionen: 16 Bundesländer Deutschland, 9 Bundesländer Österreich, 6 Regionen Schweiz. Gewinnquote = Anteil gewonnener Spiele eines „soliden“ Teams (je 800 Simulationen), Standardspiel Ziel 12 SP; Kurz Ziel 12 SP, Lang Ziel 14 SP. Zuschlag = regionaler Gefahrenzuschlag auf die Ereignisstärke.", SUB)]
    rows = [["Land", "Kürzel", "Edition", "Standorte", "Typ. Arten", "Zuschlag", "Kurz", "Standard", "Lang", "passiv (Std.)", "Hinweis"]]
    for r in REGION_LISTE:
        b = bal[r["code"]]
        rows.append([r["land"], r["code"], f'<b>{r["name"]}</b>', r["n"], len(r["arten"]),
                     ", ".join(f'{RES_NAMES[k].split("/")[0]} {v:+d}'.replace("-", "−") for k, v in r["zuschlag"].items()) or "–",
                     f'{b["kurz"]} %', f'{b["standard"]} %', f'{b["lang"]} %', f'{b["passiv"]} %', r["hinweis"]])
    S += [tbl(rows, [10, 12, 36, 19, 15, 28, 12, 18, 12, 17, 98], font=ParagraphStyle("c0", parent=CELL, fontSize=6.8, leading=8.0))]
    S += [Spacer(1, 3), P("Hinweis: Die Langvariante ist in einzelnen Alpen- und Voralpenregionen sowie im Mittelland anspruchsvoller (ca. 40 %), das Kurzspiel ist als Einstieg durchgehend leichter. Alle Werte sind Modellrechnungen mit vereinfachten Teamstrategien und ersetzen keinen Praxistest.", SMALL)]
    S += [PageBreak(), P("Baumarten – alle Werte", H1), P("W Wasser · N Nährstoffe · T Wärme (Bereich 1–5, in dem die Art voll geeignet ist) · Widerstandskraft 1–5: DÜ Dürre, ST Sturm/Schnee, KÄ Käfer, PI Pilze, FR Frost, FE Feuer, VE Verbiss · Holz = Holzwert 1–5 · T€ = Pflanzkosten", SUB)]
    hdr = ["Baumart", "Deck", "Kategorie", "W", "N", "T", "DÜ", "ST", "KÄ", "PI", "FR", "FE", "VE", "Holz", "T€", "Eigenschaften", "Verbreitung"]
    rows = [hdr]
    def rg(r): return f"{r[0]}–{r[1]}" if r[0] != r[1] else f"{r[0]}"
    for s in SPECIES_LIST:
        rows.append([f'<b>{s["name"]}</b><br/><font size="6" color="#78909C"><i>{s["latin"]}</i></font>', DECKS[s["deck"]][0].replace("Erweiterung ", "Erw. "),
                     s["kat"], rg(s["W"]), rg(s["N"]), rg(s["T"])] + [s["res"][k] for k in RES_KEYS] +
                    [s["hw"], s["cost"], ", ".join({"PIO": "Pionier", "SCH": "Schatten", "BOD": "Bodenverb.", "INV": "invasiv"}[e] for e in s["eig"]),
                      " · ".join(f'{l} {sum(1 for c in s["regionen"] if REGIONEN[c]["land"] == l)}' for l in ("DE", "AT", "CH")) if s["regionen"] else "–"])
    w = [49, 22, 34, 12, 12, 12, 9, 9, 9, 9, 9, 9, 9, 9, 8, 26, 31]
    S += [tbl(rows, w, font=ParagraphStyle("c2", parent=CELL, fontSize=7.2, leading=8.6))]
    S += [PageBreak(), P("Standorte und Klimapfad", H1)]
    rows = [["ID", "Region", "Standort", "Landschaft", "W", "N", "T", "Modifikator", "Start", "E bei Klimastufe 0 / 1 / 2 / 3", "Beschreibung"]]
    for s in sorted(STANDORTE, key=lambda s: (REGION_ORDER[s["reg"]], s["id"])):
        sp = SPECIES[s["start"]]
        mods = ", ".join(f'{RES_NAMES[k].split("/")[0]} {v:+d}'.replace("-", "−") for k, v in s["mods"].items()) or "–"
        rows.append([s["id"], s["reg"], s["name"], s["land"], s["W"], s["N"], s["T"], mods, sp["name"],
                     " / ".join(str(sim.eignung(sp, s, k)) for k in range(4)), s["text"]])
    S += [tbl(rows, [11, 11, 38, 30, 7, 7, 7, 25, 22, 22, 97], font=ParagraphStyle("c3", parent=CELL, fontSize=7.2, leading=8.6))]
    S += [Spacer(1, 6), P("Vollgeeignete Basisarten je Standort (E 3) – wie stark schrumpft die Auswahl mit dem Klima?", H2)]
    rows = [["ID", "Standort", "Klimastufe 0", "Klimastufe 1", "Klimastufe 2", "Klimastufe 3", "Mit allen Erweiterungen (Stufe 2)"]]
    for s in sorted(STANDORTE, key=lambda s: (REGION_ORDER[s["reg"]], s["id"])):
        row = [s["id"], s["name"]]
        for k in range(4):
            row.append(sum(1 for x in SPECIES_LIST if x["deck"] == "basis" and sim.eignung(x, s, k) == 3))
        row.append(sum(1 for x in SPECIES_LIST if sim.eignung(x, s, 2) == 3))
        rows.append(row)
    S += [tbl(rows, [14, 60, 30, 30, 30, 30, 50], font=ParagraphStyle("c4", parent=CELL, fontSize=7.4, leading=8.8))]
    doc.build(S)


def csvs():
    def w(name, header, rows):
        with open(f"{OUT}/{name}", "w", newline="", encoding="utf-8-sig") as f:
            cw = csv.writer(f, delimiter=";"); cw.writerow(header); cw.writerows(rows)
    w("daten_baumarten.csv", ["id", "name", "latein", "deck", "gruppe", "kategorie", "W_min", "W_max", "N_min", "N_max", "T_min", "T_max"] + RES_KEYS +
      ["holzwert", "kosten_Teur", "regionen_typisch", "eigenschaften", "merksatz"],
      [[s["id"], s["name"], s["latin"], s["deck"], s["grp"], s["kat"], *s["W"], *s["N"], *s["T"], *[s["res"][k] for k in RES_KEYS],
        s["hw"], s["cost"], " ".join(s["regionen"]), " ".join(s["eig"]), s["note"]] for s in SPECIES_LIST])
    w("daten_regionen.csv", ["kuerzel", "land", "name", "farbe", "kachel_spalte", "kachel_zeile", "zuschlag", "anzahl_standorte", "arten", "hinweis"],
      [[r["code"], r["land"], r["name"], r["farbe"], *r["kachel"], " ".join(f"{k}{v:+d}" for k, v in r["zuschlag"].items()), r["n"], " ".join(r["arten"]), r["hinweis"]] for r in REGION_LISTE])
    w("daten_standorte.csv", ["id", "region", "name", "landschaft", "W", "N", "T", "modifikatoren", "start_baumart", "beschreibung"],
      [[s["id"], s["reg"], s["name"], s["land"], s["W"], s["N"], s["T"], " ".join(f"{k}{v:+d}" for k, v in s["mods"].items()), s["start"], s["text"]]
       for s in STANDORTE])
    w("daten_ereignisse.csv", ["id", "name", "art", "staerke", "betroffen", "spread", "text", "effekt", "waldwissen"],
      [[e["id"], e["name"], e["kind"], e["S"], e["filtertext"], int(e["spread"]), e["text"], e["effekt"] or "", e["lehr"]] for e in EVENTS])
    w("daten_fachkarten.csv", ["name", "kosten_Teur", "effekt", "anzahl", "waldwissen"], [list(f) for f in FACH])


if __name__ == "__main__":
    csvs(); regelheft(); uebersicht()
    print("fertig")

# Liste aller Noten, Euro in Cent
geld_einheiten = [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

#--------------------------------------------------------------------------

# Funktion zur Berechnung des Rückgelds
def rueckgeld_berechnen(betrag):
    # Betrag wird in Cent umgewandelt; Cent ist Euro mal hundert
    rest = int(round(betrag * 100))
    ergebnis = {}

    # Berechnung der benötigten Einheiten
    for einheit in geld_einheiten:
        anzahl = rest // einheit  # Wie oft passt die Einheit in den Rest
        if anzahl > 0:  # Nur wenn mindestens eine Einheit gebraucht wird
            ergebnis[einheit] = anzahl
            rest = rest - (anzahl * einheit)

    return ergebnis  # Gib das Ergebnis als Output zurück

# Benutzer gibt einen Betrag ein
eingabe = input("Gib einen Betrag ein:")
betrag = float(eingabe)

# Rückgeld berechnen
ausgabe = rueckgeld_berechnen(betrag)

# Ausgabe der Ergebnisse
print("Es werden folgende Banknoten/Münzen benötigt:")
for einheit, anzahl in ausgabe.items():
    if einheit >= 100:
        print(f"{anzahl} x {einheit // 100} Euro")
    else:
        print(f"{anzahl} x {einheit} Cent")

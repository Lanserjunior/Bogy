# Liste aller Noten, euro in cent
geld_einheiten = [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

# Gruppen ding wie man berechnet
def rueckgeld_berechnen(betrag):
    # Betrag wird in Cent umgewandelt; Cent ist euro mal hundert
    rest = int(round(betrag * 100))
    ergebnis = {}

#funktion für rückgabe
for einheit in geld_einheiten:
    anzahl = rest // einheit  # Wie oft passt die Einheit in den Rest
    if anzahl > 0:  # Nur wenn min eine Einheit gebraucht wird
        ergebnis[einheit] = anzahl  # Speichern der Anzahl dieser Einheit
        rest = rest - (anzahl * einheit)  # Ziehe die anzahl dieser Einheiten vom Restbetrag ab

return ergebnis  # Gib das Ergebnis als output zurück


    return ergebnis

# Benutzer gibt einen Betrag ein
eingabe = input("Gib einen Betrag ein (z.B. 12.73): ")
betrag = float(eingabe)

# Rückgeld berechnen
ausgabe = rueckgeld_berechnen(betrag)

# Ausgabe der Ergebnisse
print("Es werden folgende Banknoten benötigt:")
for einheit, anzahl in ausgabe.items():  # Gehe alle Einheiten im Ergebnis durch
    if einheit >= 100:  # Wenn die Einheit min 100 C ist, also 1 € oder mehr
        print(f"{anzahl} x {einheit // 100} Euro")  # Teile durch 100, wegen euro und cent
    else:
        print(f"{anzahl} x {einheit} Cent")  # Sonst als Cent


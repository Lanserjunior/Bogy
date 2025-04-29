# -*- coding: utf-8 -*-
#"""
#Created on Tue Apr 29 06:50:38 2025

#@author: FelixLanser
#"""
#-----------------------------------------------------------------------

# Copyright (c) 2025 Felix Lanser. Alle Rechte vorbehalten.
# Diese Software darf nicht ohne Erlaubnis weiterverbreitet oder kommerziell genutzt werden.

# Sprachoptionen zur Auswahl
sprachen = {"1": "de", "2": "en", "3": "fr", "4": "es", "5": "gb"}

# Sprachspezifische Texte
nachrichten = {
    "de": {
        "start": "Hinweis: Nach einer Eingabe muss das Programm neu gestartet werden.\n",
        "frage": "Wie viele Fibonacci-Zahlen möchtest du sehen? ",
        "fehler_zahl": "Gib bitte eine ganze Zahl ein!",
        "fehler_klein": "Die Zahl muss größer als 0 sein.",
        "fehler_groß": "Bitte wähle eine kleinere Zahl (max. 10.000 erlaubt).",
        "warnung_konsole": "Achtung: Große Zahlen können die Anzeige sehr langsam machen!",
        "fibo": "Fibonacci-Zahl"
    },
    "en": {
        "start": "Note: After entering a number, restart the program.\n",
        "frage": "How many Fibonacci numbers would you like to see? ",
        "fehler_zahl": "Please enter a whole number!",
        "fehler_klein": "The number must be greater than 0.",
        "fehler_groß": "Please choose a smaller number (maximum is 10,000).",
        "warnung_konsole": "Warning: Large numbers may slow down the output!",
        "fibo": "Fibonacci number"
    },
    "fr": {
        "start": "Remarque : redémarrez le programme après la saisie.\n",
        "frage": "Combien de nombres de Fibonacci voulez-vous voir ? ",
        "fehler_zahl": "Veuillez entrer un nombre entier valide !",
        "fehler_klein": "Le nombre doit être supérieur à 0.",
        "fehler_groß": "Veuillez entrer un nombre plus petit (maximum : 10 000).",
        "warnung_konsole": "Attention : de très grands nombres peuvent ralentir l'affichage !",
        "fibo": "Nombre de Fibonacci"
    },
    "es": {
        "start": "Nota: reinicie el programa después de ingresar.\n",
        "frage": "¿Cuántos números de Fibonacci desea ver? ",
        "fehler_zahl": "¡Ingrese un número entero válido!",
        "fehler_klein": "El número debe ser mayor que 0.",
        "fehler_groß": "Por favor, elija un número menor (máximo 10.000).",
        "warnung_konsole": "Advertencia: ¡los números grandes pueden ralentizar la salida!",
        "fibo": "Número de Fibonacci"
    },
    "gb": {  # Deutsche Zahlenräume für "gb"
        "start": "Meesa warnin': After you input, restart meesa program. \n",
        "frage": "Meesa wanna know: How many Fibonacci numbers meesa gonna see? Hmmm? ",
        "fehler_zahl": "Meesa no understand! You gotta enter whole number, yeah!",
        "fehler_klein": "Meesa say: number bigger than zero, okay? Got it?",
        "fehler_groß": "Too big! Meesa no compute, you need max 10,000! No way!",
        "warnung_konsole": "Meesa warn! Big numbers make meesa slow down da show, hmmm!",
        "fibo": "Fibo-bubble, meesa love it!"  # Jabba's cool twist on Fibonacci
    }
}

# Funktion für deutsche Zahlenräume
def schöne_zahl(n, sprache):
    text = f"{n:,}".replace(",", ".")  # Setzt Punkte für bessere Lesbarkeit
    größen = {
        "de": [(10**24, "Quadrilliarde", "Quadrilliarden"), (10**21, "Trilliarde", "Trilliarden"),
               (10**18, "Trillion", "Trillionen"), (10**15, "Billiarde", "Billiarden"),
               (10**12, "Billion", "Billionen"), (10**9, "Milliarde", "Milliarden"),
               (10**6, "Million", "Millionen")],
        "en": [(10**24, "Septillion", "Septillions"), (10**21, "Sextillion", "Sextillions"),
               (10**18, "Quintillion", "Quintillions"), (10**15, "Quadrillion", "Quadrillions"),
               (10**12, "Trillion", "Trillions"), (10**9, "Billion", "Billions"),
               (10**6, "Million", "Millions")],
        "fr": [(10**24, "Quadrilliarde", "Quadrilliardes"), (10**21, "Trilliarde", "Trilliardes"),
               (10**18, "Trillion", "Trillions"), (10**15, "Billiarde", "Billiardes"),
               (10**12, "Billion", "Billions"), (10**9, "Milliard", "Milliards"),
               (10**6, "Million", "Millions")],
        "es": [(10**24, "Cuatrillardo", "Cuatrillardos"), (10**21, "Trillardo", "Trillardos"),
               (10**18, "Trillón", "Trillones"), (10**15, "Billardo", "Billardos"),
               (10**12, "Billón", "Billones"), (10**9, "Mil millones", "Mil millones"),
               (10**6, "Millón", "Millones")],
        "gb": [(10**24, "Quadrilliarde", "Quadrilliarden"), (10**21, "Trilliarde", "Trilliarden"),
               (10**18, "Trillion", "Trillionen"), (10**15, "Billiarde", "Billiarden"),
               (10**12, "Billion", "Billionen"), (10**9, "Milliarde", "Milliarden"),
               (10**6, "Million", "Millionen")]
    }
    stufen = größen.get(sprache, größen["de"])
    for grenze, singular, plural in stufen:
        if n >= grenze:
            menge = n / grenze
            wort = singular if round(menge, 1) == 1 else plural
            return f"{text} (~{menge:.1f}".replace(".", ",") + f" {wort})"
    return text

# Hauptfunktion für die Benutzereingabe und Fibonacci-Berechnung
def fibonacci():
    # Copyright-Hinweis und Warnung zu Beginn
    print("\n------------------------------------")
    print("Copyright (c) 2025 Felix Lanser. Alle Rechte vorbehalten.")
    print("Warnung: Große Zahlen können die Ausgabe verlangsamen!")
    print("Das Programm muss nach jeder Nutzung neu gestartet werden.\n------------------------------------")

    print("Wähle deine Sprache:")
    print("1: Deutsch, 2: Englisch, 3: Französisch, 4: Spanisch, 5: Galactic Basic")
    sprache_auswahl = input("Gib die Zahl der gewünschten Sprache ein: ")

    sprache = nachrichten.get(sprachen.get(sprache_auswahl, "de"), nachrichten["de"])

    print(sprache["start"])

    while True:
        try:
            # Eingabe der Anzahl der Fibonacci-Zahlen
            anzahl = int(input(sprache["frage"]))
            if anzahl <= 0:
                print(sprache["fehler_klein"])
            elif anzahl > 10000:
                print(sprache["fehler_groß"])
            else:
                break
        except ValueError:
            print(sprache["fehler_zahl"])

    print(sprache["warnung_konsole"])  # Warnung wegen der Verlangsamung

    fibo = [0, 1]
    for i in range(2, anzahl):
        fibo.append(fibo[i - 1] + fibo[i - 2])

    print(f"{sprache['fibo']}:")
    for i, num in enumerate(fibo):
        print(f"{i + 1}: {schöne_zahl(num, sprache_auswahl)}")

# Das Programm startet hier
fibonacci()

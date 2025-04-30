# -*- coding: utf-8 -*-
#"""
#Created on Tue Apr 29 06:50:38 2025
#
#@author: FelixLanser
#"""
#-----------------------------------------------------------------------
# Version 1.0
# Copyright (c) 2025 Felix Lanser. Alle Rechte vorbehalten.
#-----------------------------------------------------------------------

# Ausgabe der Trennlinien und Hinweise
def print_intro():
    # Trennlinie oben
    print("-" * 60)
    # Versions- und Copyright Hinweis
    print("Version 1.0")
    print("Copyright (c) 2025 Felix Lanser. Alle Rechte vorbehalten.")
    # Trennlinie unten
    print("-" * 60)

# Ausgabe der Sprache und Auswahlmöglichkeiten in der jeweiligen Sprache
def sprache_waehlen():
    print("\nWähle eine Sprache:")
    print("1. Deutsch")
    print("2. English")
    print("3. Français")
    print("4. Español")
    print("5. Galactic Basic")
    print("Drücke 'x' zum Beenden.")

# Funktion zum Starten der Berechnung der Fibonacci-Zahlen
def fibonacci_berechnen(sprache):
    # Hier kommt der Code zum Berechnen der Fibonacci-Zahlen
    print(f"Berechnung in {sprache}...")

# Hauptfunktion
def main():
    # Zuerst die Einführung und Hinweise ausgeben
    print_intro()

    # Sprachauswahl
    while True:
        # Spracchauswahl in Deutsch
        sprache_waehlen()
        sprache = input("Wähle die Zahl für die Sprache oder 'x' zum Beenden: ").strip().lower()

        if sprache == '1':
            sprache = 'Deutsch'
        elif sprache == '2':
            sprache = 'English'
        elif sprache == '3':
            sprache = 'Français'
        elif sprache == '4':
            sprache = 'Español'
        elif sprache == '5':
            sprache = 'Galactic Basic'
        elif sprache == 'x':
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Eingabe. Bitte wähle eine gültige Zahl (1-5) oder 'x' zum Beenden.")
            continue
        
        # Weiter mit der Berechnung
        fibonacci_berechnen(sprache)

# Start des Programms
if __name__ == "__main__":
    main()

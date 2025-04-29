# -*- coding: utf-8 -*-
# --------------------------------------------------
# Created on: Tue Apr 29 2025
# Author: Felix Lanser
# Copyright (c) 2025 Felix Lanser. All rights reserved.
# --------------------------------------------------

# This program calculates Fibonacci numbers in various languages.
# Max allowed: 100 numbers. You can return to language menu by typing 'x'.

import sys

# Language dictionaries
languages = {
    "1": "Deutsch",
    "2": "English",
    "3": "Français",
    "4": "Español",
    "5": "Galactic Basic"
}

# Messages in different languages
messages = {
    "choose_language": {
        "1": "Bitte wähle eine Sprache (1=Deutsch, 2=Englisch, 3=Französisch, 4=Spanisch, 5=Galactic Basic): ",
        "2": "Please choose a language (1=German, 2=English, 3=French, 4=Spanish, 5=Galactic Basic): ",
        "3": "Veuillez choisir une langue (1=Allemand, 2=Anglais, 3=Français, 4=Espagnol, 5=Galactic Basic): ",
        "4": "Por favor, elige un idioma (1=Alemán, 2=Inglés, 3=Francés, 4=Español, 5=Galactic Basic): ",
        "5": "Ootmanchoo peekpa peetee (1=Doytcha, 2=Basic, 3=Fronk, 4=Espanyola, 5=GB): "
    },
    "invalid_language": {
        "1": "Ungültige Auswahl. Bitte wähle eine Zahl zwischen 1 und 5.",
        "2": "Invalid selection. Please choose a number between 1 and 5.",
        "3": "Sélection invalide. Choisissez un chiffre entre 1 et 5.",
        "4": "Selección inválida. Elige un número del 1 al 5.",
        "5": "Mochabba! No goota. Choosa one-of-five o wan wanga."
    },
    "input_info": {
        "1": "Bitte gib eine natürliche Zahl zwischen 1 und 100 ein (oder 'x' zum Sprachmenü): ",
        "2": "Please enter a natural number between 1 and 100 (or 'x' to go back): ",
        "3": "Veuillez entrer un nombre naturel entre 1 et 100 (ou 'x' pour revenir): ",
        "4": "Por favor, introduce un número natural entre 1 y 100 (o 'x' para volver): ",
        "5": "Noba jujum 1-100, or type 'x' bakawan: "
    },
    "invalid_number": {
        "1": "Ungültige Eingabe. Nur natürliche Zahlen zwischen 1 und 100 erlaubt.",
        "2": "Invalid input. Only natural numbers between 1 and 100 allowed.",
        "3": "Entrée invalide. Seuls les nombres naturels entre 1 et 100 sont autorisés.",
        "4": "Entrada inválida. Solo se permiten números naturales entre 1 y 100.",
        "5": "Mee choppa! Only 1-100 jujums valid."
    },
    "try_again": {
        "1": "Möchtest du eine weitere Berechnung durchführen? (ja/nein): ",
        "2": "Would you like to calculate again? (yes/no): ",
        "3": "Voulez-vous refaire un calcul ? (oui/non): ",
        "4": "¿Quieres hacer otro cálculo? (sí/no): ",
        "5": "Moocha do it again? (yes/no): "
    },
    "invalid_answer": {
        "1": "Ungültige Antwort. Bitte 'ja' oder 'nein' eingeben.",
        "2": "Invalid answer. Please enter 'yes' or 'no'.",
        "3": "Réponse invalide. Veuillez taper 'oui' ou 'non'.",
        "4": "Respuesta inválida. Escribe 'sí' o 'no'.",
        "5": "Nogga right. Say 'yes' o 'no'."
    },
    "exit": {
        "1": "Programm beendet.",
        "2": "Program exited.",
        "3": "Programme terminé.",
        "4": "Programa terminado.",
        "5": "Wanga done."
    }
}

# Number system for rounding
number_units = {
    "1": [("Quadrilliarde", 10**27), ("Quadrillion", 10**24), ("Trilliarde", 10**21), ("Trillion", 10**18),
          ("Billiarde", 10**15), ("Billion", 10**12), ("Milliarde", 10**9), ("Million", 10**6), ("Tausend", 10**3)],
    "2": [("Octillion", 10**27), ("Septillion", 10**24), ("Sextillion", 10**21), ("Quintillion", 10**18),
          ("Quadrillion", 10**15), ("Trillion", 10**12), ("Billion", 10**9), ("Million", 10**6), ("Thousand", 10**3)],
    "3": [("Quadrilliard", 10**27), ("Quadrillion", 10**24), ("Trilliard", 10**21), ("Trillion", 10**18),
          ("Billiard", 10**15), ("Billion", 10**12), ("Milliard", 10**9), ("Million", 10**6), ("Mille", 10**3)],
    "4": [("Cuatrillardo", 10**27), ("Cuatrillón", 10**24), ("Trillardo", 10**21), ("Trillón", 10**18),
          ("Billardo", 10**15), ("Billón", 10**12), ("Mil millones", 10**9), ("Millón", 10**6), ("Mil", 10**3)],
    "5": [("Duggamill", 10**27), ("Jabbillion", 10**24), ("Biggaboom", 10**21), ("Banthillion", 10**18),
          ("Rancillarde", 10**15), ("Sarlaccilliarde", 10**12), ("Yaddleon", 10**9), ("Yodillion", 10**6), ("Wookiee", 10**3)]
}

def choose_language():
    while True:
        lang = input(messages["choose_language"]["2"])
        if lang in languages:
            print(f"Language set to: {languages[lang]}\n")
            return lang
        else:
            for msg in messages["invalid_language"].values():
                print(msg)

def get_count(lang):
    while True:
        entry = input(messages["input_info"][lang])
        if entry.lower() == 'x':
            return 'x'
        if entry.isdigit():
            count = int(entry)
            if 1 <= count <= 100:
                return count
        print(messages["invalid_number"][lang])

def fibonacci(n):
    fibs = [0, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:n]

def format_number(num, lang):
    for name, value in number_units[lang]:
        if num >= value:
            return f"~{format(num / value, ',.3f').replace(',', '.')} {name}"
    return str(num)

def main():
    while True:
        print("Note: You can return to this menu by entering 'x' before calculation.\n")
        lang = choose_language()
        while True:
            count = get_count(lang)
            if count == 'x':
                break
            fibs = fibonacci(count)
            print("\nFibonacci-Zahlen:\n")
            for i, num in enumerate(fibs):
                num_str = f"{num:,}".replace(",", ".")
                rounded = format_number(num, lang)
                print(f"{i+1}: {num_str} ({rounded})")
            while True:
                again = input(messages["try_again"][lang]).strip().lower()
                if again in ['ja', 'yes', 'oui', 'sí', 'si']:
                    break
                elif again in ['nein', 'no', 'non']:
                    print(messages["exit"][lang])
                    sys.exit()
                else:
                    print(messages["invalid_answer"][lang])

if __name__ == "__main__":
    main()

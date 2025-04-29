# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------
# Created on Tue Apr 29 06:50:38 2025
# @author: Felix Lanser
# Copyright (c) 2025 Felix Lanser. All rights reserved.
# -----------------------------------------------------------------------

# This program calculates Fibonacci numbers with optional rounding.
# Please restart the program after each complete run.
# ⚠️ MAXIMUM: You can calculate up to 100 Fibonacci numbers.
# ℹ️ Press 'x' during number input to return to language selection.

# Select your language / Choisissez votre langue / Seleccione su idioma / Wähle deine Sprache / Poy ooma uma?
print("------------------------------------------------------------")
print("Bitte wähle eine Sprache / Please select a language / Veuillez choisir une langue / Selecciona un idioma / Poy ooma uma?")
print("1 = Deutsch | 2 = English | 3 = Français | 4 = Español | 5 = Galactic Basic (Star Wars)")
print("------------------------------------------------------------")

# Define language strings
language_strings = {
    "de": {
        "lang_name": "Deutsch",
        "invalid": "Ungültige Eingabe! Bitte gib eine Zahl zwischen 1 und 100 ein.",
        "limit_warn": "⚠️ Zu hohe Werte können das Programm stark verlangsamen!",
        "max_info": "Du kannst maximal 100 Fibonacci-Zahlen berechnen.",
        "how_many": "Wie viele Fibonacci-Zahlen sollen berechnet werden (max. 100)? (x = zurück): ",
        "result": "Fibonacci-Zahlen:",
        "approx": "ungefähr",
        "again": "Möchtest du noch einmal berechnen? (ja/nein): ",
        "goodbye": "Auf Wiedersehen!",
        "gb_warning": "Galactic Basic ist eine fiktive Sprache aus Star Wars und dient nur zur Unterhaltung. Fehler sind möglich.",
        "x_hint": "Du kannst jederzeit 'x' eingeben, um zur Sprachauswahl zurückzukehren.",
        "invalid_lang": "Ungültige Spracheingabe. Sprache wurde auf Deutsch gesetzt."
    },
    "en": {
        "lang_name": "English",
        "invalid": "Invalid input! Please enter a number between 1 and 100.",
        "limit_warn": "⚠️ High values can slow down the program!",
        "max_info": "You can calculate up to 100 Fibonacci numbers.",
        "how_many": "How many Fibonacci numbers should be calculated (max. 100)? (x = back): ",
        "result": "Fibonacci numbers:",
        "approx": "approx.",
        "again": "Do you want to calculate again? (yes/no): ",
        "goodbye": "Goodbye!",
        "gb_warning": "Galactic Basic is a fictional language from Star Wars and only for fun. Errors may occur.",
        "x_hint": "You can always type 'x' to return to language selection.",
        "invalid_lang": "Invalid language choice. Defaulting to English."
    },
    "fr": {
        "lang_name": "Français",
        "invalid": "Entrée invalide ! Veuillez entrer un nombre entre 1 et 100.",
        "limit_warn": "⚠️ Des valeurs trop élevées peuvent ralentir le programme !",
        "max_info": "Vous pouvez calculer jusqu'à 100 nombres de Fibonacci.",
        "how_many": "Combien de nombres de Fibonacci faut-il calculer (max. 100) ? (x = retour) : ",
        "result": "Nombres de Fibonacci :",
        "approx": "environ",
        "again": "Voulez-vous recommencer ? (oui/non) : ",
        "goodbye": "Au revoir !",
        "gb_warning": "Galactic Basic est une langue fictive de Star Wars utilisée uniquement pour le plaisir. Des erreurs peuvent se produire.",
        "x_hint": "Tapez 'x' à tout moment pour revenir à la sélection de la langue.",
        "invalid_lang": "Choix de langue invalide. Français sélectionné par défaut."
    },
    "es": {
        "lang_name": "Español",
        "invalid": "¡Entrada inválida! Ingresa un número entre 1 y 100.",
        "limit_warn": "⚠️ Valores altos pueden ralentizar el programa.",
        "max_info": "Puedes calcular hasta 100 números de Fibonacci.",
        "how_many": "¿Cuántos números de Fibonacci quieres calcular (máx. 100)? (x = volver): ",
        "result": "Números de Fibonacci:",
        "approx": "aprox.",
        "again": "¿Quieres calcular otra vez? (sí/no): ",
        "goodbye": "¡Adiós!",
        "gb_warning": "Galactic Basic es un idioma ficticio de Star Wars, solo con fines de entretenimiento. Pueden ocurrir errores.",
        "x_hint": "Puedes escribir 'x' en cualquier momento para volver al menú de idioma.",
        "invalid_lang": "Idioma no válido. Español seleccionado por defecto."
    },
    "gb": {
        "lang_name": "Galactic Basic",
        "invalid": "Jee oto bah! Wanga numba 1 en 100!",
        "limit_warn": "⚠️ Too moocha peedoo... system go slooooow!",
        "max_info": "You maxee 100 fibo-numba calculate.",
        "how_many": "How many Fibo-numba you want? (x = backa) : ",
        "result": "Fibo-numba list:",
        "approx": "likee",
        "again": "One more timeee? (yes/no): ",
        "goodbye": "Bye bye!",
        "gb_warning": "Galactic Basic is-a Star Wars fun speaky! Mistake happen, okieday?",
        "x_hint": "You say 'x', you go back menu, huh.",
        "invalid_lang": "No speaka that lang. Using Galactic Basic."
    }
}

# Choose language
lang_code = input("→ Auswahl: ").strip()
lang_map = {"1": "de", "2": "en", "3": "fr", "4": "es", "5": "gb"}
lang = lang_map.get(lang_code, "de")
msg = language_strings.get(lang, language_strings["de"])

# Show GB warning if needed
if lang == "gb":
    print(msg["gb_warning"])

# Show limit and restart warnings clearly
print("=" * 60)
print("🔁 " + msg["x_hint"])
print("🚨 " + msg["limit_warn"])
print("📌 " + msg["max_info"])
print("🔁 Please restart the program after use.")
print("=" * 60)

# Function to calculate Fibonacci numbers
def get_fibonacci(n):
    fib = [1, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# Function to round large numbers (German scale)
def round_number(n, lang):
    units = [("Quadrilliarden", 10**27), ("Trilliarden", 10**21), ("Billiarden", 10**15), ("Milliarden", 10**9), ("Millionen", 10**6), ("Tausend", 10**3)]
    en_units = [("quadrillion", 10**15), ("trillion", 10**12), ("billion", 10**9), ("million", 10**6), ("thousand", 10**3)]
    for name, value in (units if lang in ["de", "fr", "es", "gb"] else en_units):
        if n >= value:
            return f"~{n // value}.{(n % value) // (value // 10)} {name}"
    return str(n)

# Loop to allow repeat
while True:
    count = input(msg["how_many"]).strip()
    if count.lower() == "x":
        exec(open(__file__).read())  # Restart program (not ideal in all editors)
        break
    if not count.isdigit() or int(count) < 1 or int(count) > 100:
        print(msg["invalid"])
        continue
    count = int(count)
    fibs = get_fibonacci(count)

    print(msg["result"])
    for i, num in enumerate(fibs, start=1):
        formatted = f"{num:,}".replace(",", ".")  # dot separator
        print(f"{i}: {formatted} ({msg['approx']} {round_number(num, lang)})")

    again = input(msg["again"]).strip().lower()
    if again not in ["ja", "yes", "oui", "sí", "si"]:
        print(msg["goodbye"])
        break

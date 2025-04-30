# -*- coding: utf-8 -*-
# Created on Tue Apr 29 06:50:38 2025
# @author: Felix Lanser
# -----------------------------------------------------------------------

def fibonacci(n):
    fibo_list = [0, 1]
    for _ in range(2, n):
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    return fibo_list[:n]

def language_selection():
    print("=" * 60)
    print("Version 1.0.0")
    print("Copyright (c) 2025 Felix Lanser. Alle Rechte vorbehalten.")
    print("=" * 60)
    print()
    print("Bitte wähle eine Sprache / Please choose a language:")
    print("1: Deutsch")
    print("2: English")
    print("3: Français")
    print("4: Español")
    print("5: Galactic Basic")

    while True:
        choice = input("Eingabe / Input: ").strip()
        if choice == "1":
            return "de"
        elif choice == "2":
            return "en"
        elif choice == "3":
            return "fr"
        elif choice == "4":
            return "es"
        elif choice == "5":
            return "gb"
        else:
            print("Ungültige Eingabe. Bitte erneut versuchen.")

def print_language_hints(language):
    warnings = {
        "de": [
            "Hinweis: Sehr große Zahlen können die Berechnung verlangsamen.",
            "Du kannst auch 'x' drücken, um zur Sprachauswahl zurückzukehren."
        ],
        "en": [
            "Note: Very large numbers can slow down calculation.",
            "You can also press 'x' to return to the language selection."
        ],
        "fr": [
            "Remarque : Les très grands nombres peuvent ralentir le calcul.",
            "Vous pouvez également appuyer sur 'x' pour revenir au choix de la langue."
        ],
        "es": [
            "Nota: Los números muy grandes pueden ralentizar el cálculo.",
            "También puedes pulsar 'x' para volver a la selección de idioma."
        ],
        "gb": [
            "Yo, big numbers might slow ya down, just sayin'.",
            "Press 'x' to go back to da language menu, yo."
        ]
    }
    print()
    for line in warnings[language]:
        print(line)
    print()

def get_number(language):
    prompts = {
        "de": "Wie viele Fibonacci-Zahlen möchtest du berechnen? (1-100): ",
        "en": "How many Fibonacci numbers would you like to calculate? (1-100): ",
        "fr": "Combien de nombres de Fibonacci voulez-vous calculer ? (1-100): ",
        "es": "¿Cuántos números de Fibonacci te gustaría calcular? (1-100): ",
        "gb": "How many da Fibonacci numbas ya wanna see? (1-100): "
    }
    errors = {
        "de": "Ungültige Eingabe. Bitte gib eine natürliche Zahl zwischen 1 und 100 ein.",
        "en": "Invalid input. Please enter a natural number between 1 and 100.",
        "fr": "Entrée invalide. Veuillez entrer un nombre naturel entre 1 et 100.",
        "es": "Entrada no válida. Introduce un número natural entre 1 y 100.",
        "gb": "That ain't right. Gimme a natural numba from 1 to 100, bro."
    }

    while True:
        val = input(prompts[language]).strip().lower()
        if val == "x":
            return "x"
        if val.isdigit():
            num = int(val)
            if 1 <= num <= 100:
                return num
        print(errors[language])

def round_fibonacci_number(num, language):
    suffixes = {
        "de": ["Millionen", "Milliarden", "Billionen", "Billiarden", "Trillionen"],
        "en": ["million", "milliard", "billion", "billiard", "trillion"],
        "fr": ["millions", "milliards", "billions", "billiards", "trillions"],
        "es": ["millones", "mil millones", "billones", "mil billones", "trillones"],
        "gb": ["millya", "billya", "trillya", "quadrya", "quinty"]
    }

    if num < 1_000_000:
        return f"{num:.2f}".replace('.', ',') if language == "de" else f"{num:.2f}"
    else:
        magnitude = 0
        while num >= 1000 and magnitude < len(suffixes[language]) - 1:
            num /= 1000
            magnitude += 1
        rounded = round(num, 2)
        value_str = f"{rounded:.2f}"
        if language == "de":
            value_str = value_str.replace('.', ',')
        return f"{value_str} {suffixes[language][magnitude]}"

def show_fibonacci(fibo_list, language):
    print("\nFibonacci Numbers:")
    for i, num in enumerate(fibo_list):
        rounded = round_fibonacci_number(num, language)
        print(f"{i+1}. Fibonacci Number: {num} (~{rounded})")

def answer_to_everything(language):
    messages = {
        "de": "Die Antwort auf das Leben, das Universum und den ganzen Rest.",
        "en": "The answer to life, the universe, and everything.",
        "fr": "La réponse à la vie, à l'univers et à tout le reste.",
        "es": "La respuesta a la vida, el universo y todo lo demás.",
        "gb": "Da answer to life, da universe and everythin', yo know?"
    }
    print("\n" + messages[language] + "\n")

def ask_repeat(language):
    prompts = {
        "de": "Möchtest du erneut berechnen? (Ja/Nein): ",
        "en": "Would you like to calculate again? (Yes/No): ",
        "fr": "Voulez-vous calculer à nouveau ? (Oui/Non): ",
        "es": "¿Quieres calcular de nuevo? (Sí/No): ",
        "gb": "Wanna go again? (Yes/No): "
    }
    errors = {
        "de": "Ungültige Eingabe. Bitte gib 'Ja' oder 'Nein' ein.",
        "en": "Invalid input. Please enter 'Yes' or 'No'.",
        "fr": "Entrée invalide. Veuillez entrer 'Oui' ou 'Non'.",
        "es": "Entrada no válida. Por favor introduce 'Sí' o 'No'.",
        "gb": "Huh? Say 'Yes' or 'No', my dude."
    }
    valid_yes = {
        "de": "ja", "en": "yes", "fr": "oui", "es": "sí", "gb": "yes"
    }
    valid_no = {
        "de": "nein", "en": "no", "fr": "non", "es": "no", "gb": "no"
    }

    while True:
        answer = input(prompts[language]).strip().lower()
        if answer == valid_yes[language]:
            return True
        elif answer == valid_no[language]:
            return False
        else:
            print(errors[language])

def main():
    while True:
        language = language_selection()
        print_language_hints(language)

        while True:
            number = get_number(language)
            if number == "x":
                break
            if number == 42:
                answer_to_everything(language)
            else:
                fibo = fibonacci(number)
                show_fibonacci(fibo, language)
            if not ask_repeat(language):
                farewells = {
                    "de": "Auf Wiedersehen!",
                    "en": "Goodbye!",
                    "fr": "Au revoir!",
                    "es": "¡Adiós!",
                    "gb": "See ya, space wizard!"
                }
                print(farewells[language])
                return

if __name__ == "__main__":
    main()

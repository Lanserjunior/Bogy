import sys

def show_header():
    print("-" * 50)
    print("© Felix, 2025")
    print("Version: 3.1.4")
    print("-" * 50 + "\n")

def get_language_choice():
    print("Sprache auswählen / Select language / Sélectionner la langue / Seleccionar idioma / Aporte:")
    print("1: Deutsch")
    print("2: English")
    print("3: Français")
    print("4: Español")
    print("5: Huttese")
    while True:
        choice = input("Auswahl / Choice / Choix / Selección / Aporte: ").strip()
        if choice in ("1", "2", "3", "4", "5"):
            return int(choice)
        else:
            print("Ungültige Auswahl / Invalid choice / Choix invalide / Selección inválida / Wermo choffo.")

LANGUAGES = {
    1: {
        "name": "Deutsch",
        "prompt": "Wie viele Fibonacci-Zahlen möchtest du berechnen? (1-100): ",
        "error": "Ungültige Eingabe. Bitte gib eine natürliche Zahl zwischen 1 und 100 ein.",
        "warning": "Hinweis: Hohe Zahlen können die Leistung beeinträchtigen.",
        "result": "Fibonacci-Zahlen:",
        "approx": "(~{approx} {unit})",
        "again": "Möchtest du erneut berechnen? (Ja/Nein): ",
        "yes": "ja",
        "no": "nein"
    },
    2: {
        "name": "English",
        "prompt": "How many Fibonacci numbers would you like to calculate? (1-100): ",
        "error": "Invalid input. Please enter a natural number between 1 and 100.",
        "warning": "Note: High values may slow down the program.",
        "result": "Fibonacci Numbers:",
        "approx": "(~{approx} {unit})",
        "again": "Would you like to calculate again? (Yes/No): ",
        "yes": "yes",
        "no": "no"
    },
    3: {
        "name": "Français",
        "prompt": "Combien de nombres de Fibonacci souhaitez-vous calculer ? (1-100) : ",
        "error": "Entrée invalide. Veuillez entrer un nombre naturel entre 1 et 100.",
        "warning": "Remarque : Des valeurs élevées peuvent ralentir le programme.",
        "result": "Nombres de Fibonacci :",
        "approx": "(~{approx} {unit})",
        "again": "Souhaitez-vous recommencer ? (Oui/Non) : ",
        "yes": "oui",
        "no": "non"
    },
    4: {
        "name": "Español",
        "prompt": "¿Cuántos números de Fibonacci deseas calcular? (1-100): ",
        "error": "Entrada no válida. Por favor, introduce un número natural entre 1 y 100.",
        "warning": "Nota: Valores altos pueden ralentizar el programa.",
        "result": "Números de Fibonacci:",
        "approx": "(~{approx} {unit})",
        "again": "¿Quieres calcular de nuevo? (Sí/No): ",
        "yes": "sí",
        "no": "no"
    },
    5: {
        "name": "Huttese",
        "prompt": "Peedunkee o wanna kee mombay m'bwa Fibonacci? (1-100): ",
        "error": "Moolee ra. Jee oto kee mombay m'bwa 1 fa 100.",
        "warning": "U wamma: Kee mombay spooko da naga mooie.",
        "result": "Fibonacci mombay:",
        "approx": "(~{approx} {unit})",
        "again": "Tee uba reecalculate? (Yes/No): ",
        "yes": "yes",
        "no": "no"
    }
}

UNITS_LONG_SCALE = [
    (10**18, "Trillionen", "trillion"),
    (10**15, "Billiarden", "quadrillion"),
    (10**12, "Billionen", "trillion"),
    (10**9, "Milliarden", "billion"),
    (10**6, "Millionen", "million")
]

def format_number_with_unit(n, lang_id):
    for threshold, de_unit, en_unit in UNITS_LONG_SCALE:
        if n >= threshold:
            short = round(n / threshold, 2)
            if lang_id == 1:
                return f"{short:.2f}".replace(".", ","), de_unit
            else:
                return f"{short:.2f}", en_unit
    return None, None

def get_number_input(lang):
    while True:
        try:
            number = int(input(lang["prompt"]).strip())
            if 1 <= number <= 100:
                return number
            else:
                print(lang["error"])
        except ValueError:
            print(lang["error"])

def fibonacci(n):
    fibs = [0, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:n]

def main():
    show_header()
    language_id = get_language_choice()
    lang = LANGUAGES[language_id]

    print("\n" + lang["warning"] + "\n")

    while True:
        number = get_number_input(lang)
        fibs = fibonacci(number)
        print("\n" + lang["result"])

        for i, val in enumerate(fibs, 1):
            approx, unit = format_number_with_unit(val, language_id)
            if approx and unit:
                print(f"{i}. Fibonacci Number: {val} {lang['approx'].format(approx=approx, unit=unit)}")
            else:
                print(f"{i}. Fibonacci Number: {val}")

        again = input("\n" + lang["again"]).strip().lower()
        if again != lang["yes"]:
            break

if __name__ == "__main__":
    main()

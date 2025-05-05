def show_header():
    print("-" * 50)
    print("© Max Mustermann, 2025")
    print("Version: 3.1.4")
    print("-" * 50 + "\n")

def get_language_choice():
    print("Sprache auswählen / Select language / Sélectionner la langue / Seleccionar idioma / Aporte:")
    print("1: Deutsch, 2: English, 3: Français, 4: Español, 5: Huttese")
    while (choice := input("Auswahl / Choice / Choix / Selección / Aporte: ").strip()) not in ("1", "2", "3", "4", "5"):
        print("Ungültige Auswahl / Invalid choice / Choix invalide / Selección inválida / Wermo choffo.")
    return int(choice)

LANGUAGES = {
    1: {"name": "Deutsch", "prompt": "Wie viele Fibonacci-Zahlen möchtest du berechnen? (1-100): ",
        "error": "Ungültige Eingabe.", "warning": "Hinweis: Hohe Zahlen können die Leistung beeinträchtigen.",
        "result": "Fibonacci-Zahlen:", "approx": "(~{approx} {unit})", "again": "Möchtest du erneut berechnen? (J/N): ", "yes": "j", "no": "n"},
    2: {"name": "English", "prompt": "How many Fibonacci numbers would you like to calculate? (1-100): ",
        "error": "Invalid input.", "warning": "Note: High values may slow down the program.", "result": "Fibonacci Numbers:",
        "approx": "(~{approx} {unit})", "again": "Would you like to calculate again? (Y/N): ", "yes": "y", "no": "n"},
    3: {"name": "Français", "prompt": "Combien de nombres de Fibonacci souhaitez-vous calculer ? (1-100) : ",
        "error": "Entrée invalide.", "warning": "Remarque : Des valeurs élevées peuvent ralentir le programme.",
        "result": "Nombres de Fibonacci :", "approx": "(~{approx} {unit})", "again": "Souhaitez-vous recommencer ? (O/N) : ",
        "yes": "o", "no": "n"},
    4: {"name": "Español", "prompt": "¿Cuántos números de Fibonacci deseas calcular? (1-100): ",
        "error": "Entrada no válida.", "warning": "Nota: Valores altos pueden ralentizar el programa.", "result": "Números de Fibonacci:",
        "approx": "(~{approx} {unit})", "again": "¿Quieres calcular de nuevo? (S/N): ", "yes": "s", "no": "n"},
    5: {"name": "Huttese", "prompt": "Peedunkee o wanna kee mombay m'bwa Fibonacci? (1-100): ",
        "error": "Moolee ra.", "warning": "U wamma: Kee mombay spooko da naga mooie.", "result": "Fibonacci mombay:",
        "approx": "(~{approx} {unit})", "again": "Tee uba reecalculate? (Y/N): ", "yes": "y", "no": "n"}
}

# Short Scale für alle Sprachen verwenden (Millionen, Milliarden, Billionen, Billiarden, Trillionen)
UNITS_SHORT_SCALE = [
    (10**18, "Trillionen", "trillion"),
    (10**15, "Billiarden", "quadrillion"),
    (10**12, "Billionen", "trillion"),
    (10**9, "Milliarden", "billion"),
    (10**6, "Millionen", "million")
]

def format_number_with_unit(n, lang_id):
    for threshold, de_unit, en_unit in UNITS_SHORT_SCALE:
        if n >= threshold:
            short = round(n / threshold, 2)
            unit = de_unit if lang_id == 1 else en_unit
            return f"{short:.3f}".replace(".", ","), unit
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
    lang_id = get_language_choice()
    lang = LANGUAGES[lang_id]

    print("\n" + lang["warning"] + "\n")

    while True:
        number = get_number_input(lang)
        
        # Easter Egg: Wenn der Benutzer 42 eingibt
        if number == 42:
            print(f"Die Antwort auf das Leben, das Universum und alles!\n")
            continue  # Überspringe die Fibonacci-Berechnung, da es das Easter Egg ist.

        fibs = fibonacci(number)
        print("\n" + lang["result"])

        for i, val in enumerate(fibs, 1):
            approx, unit = format_number_with_unit(val, lang_id)
            print(f"{i}. Fibonacci Number: {val} {lang['approx'].format(approx=approx, unit=unit)}" if approx else f"{i}. Fibonacci Number: {val}")

        again = input("\n" + lang["again"]).strip().lower()
        if again not in [lang["yes"], lang["no"]]:
            print(f"Ungültige Eingabe, bitte nur den ersten Buchstaben eingeben: {lang['yes']}/{lang['no']}")
        elif again != lang["yes"]:
            break

if __name__ == "__main__":
    main()

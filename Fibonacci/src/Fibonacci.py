import sys
import matplotlib.pyplot as plt  # Für die grafische Darstellung der Fibonacci-Verhältnisse

# Copyright- und Versionsinfo beim Start
print("=" * 50)
print("© Felix Lanser, 2025")
print("Version: 5.0.0")
print("=" * 50 + "\n")
print("1:Bitte wählen sie eine Sprache / 2:Please select a language / 3.Veuillez sélectionner une langue / 4.Por favor seleccione un idioma / 5.Braucha ein Sprachaa")

# Sprachdaten: Jede Sprache hat Texte (Prompts, Fehlermeldungen usw.) + Einheiten für große Zahlen
languages = {
    "1": ("Deutsch", {
        "prompt_number": "Wie viele Fibonacci-Zahlen möchtest du berechnen? (1-100): ",
        "prompt_again": "Möchtest du erneut berechnen? (J/N): ",
        "invalid_number": "Ungültige Eingabe. Bitte gib eine natürliche Zahl(ℕ) zwischen 1 und 100 ein.",
        "invalid_choice": "Ungültige Eingabe. Bitte gib J oder N ein.",
        "invalid_language": "Ungültige Auswahl. Bitte wähle eine Zahl zwischen 1 und 5.",
        "exit": "Programm beendet.",
        "back": "Zurück zur Sprachauswahl.",
        "heading": "Fibonacci-Zahlen:",
        "plot_title": "Fibonacci-Quotienten → Goldener Schnitt",
        "plot_xlabel": "n (Folgeposition)",
        "plot_ylabel": "f(n)/f(n-1)",
    }, ["Million", "Milliarde", "Billion", "Billiarde", "Trillion"]),

    "2": ("English", {
        "prompt_number": "How many Fibonacci numbers do you want to calculate? (1-100): ",
        "prompt_again": "Would you like to calculate again? (Y/N): ",
        "invalid_number": "Invalid input. Please enter a natural number(ℕ) between 1 and 100.",
        "invalid_choice": "Invalid input. Please enter Y or N.",
        "invalid_language": "Invalid selection. Please choose a number between 1 and 5.",
        "exit": "Program exited.",
        "back": "Returning to language selection.",
        "heading": "Fibonacci numbers:",
        "plot_title": "Fibonacci Ratios → Golden Ratio",
        "plot_xlabel": "n (sequence index)",
        "plot_ylabel": "f(n)/f(n-1)",
    }, ["million", "billion", "trillion", "quadrillion", "quintillion"]),

    "3": ("Français", {
        "prompt_number": "Combien de nombres de Fibonacci voulez-vous calculer ? (1-100) : ",
        "prompt_again": "Voulez-vous recommencer ? (O/N) : ",
        "invalid_number": "Entrée invalide. Veuillez entrer un nombre naturel(ℕ) entre 1 et 100.",
        "invalid_choice": "Entrée invalide. Veuillez entrer O ou N.",
        "invalid_language": "Sélection invalide. Choisissez un nombre entre 1 et 5.",
        "exit": "Programme terminé.",
        "back": "Retour à la sélection de langue.",
        "heading": "Nombres de Fibonacci :",
        "plot_title": "Rapports de Fibonacci → Nombre d'or",
        "plot_xlabel": "n (rang de la suite)",
        "plot_ylabel": "f(n)/f(n-1)",
    }, ["million", "milliard", "billion", "billiard", "trillion"]),

    "4": ("Español", {
        "prompt_number": "¿Cuántos números de Fibonacci quieres calcular? (1-100): ",
        "prompt_again": "¿Deseas calcular nuevamente? (S/N): ",
        "invalid_number": "Entrada inválida. Por favor, introduce un número natural(ℕ) entre 1 y 100.",
        "invalid_choice": "Entrada inválida. Por favor, introduce S o N.",
        "invalid_language": "Selección inválida. Elige un número entre 1 y 5.",
        "exit": "Programa terminado.",
        "back": "Volviendo a la selección de idioma.",
        "heading": "Números de Fibonacci:",
        "plot_title": "Cocientes de Fibonacci → Número áureo",
        "plot_xlabel": "n (posición en la secuencia)",
        "plot_ylabel": "f(n)/f(n-1)",
    }, ["millón", "mil millones", "billón", "mil billones", "trillón"]),

    "5": ("Galactic Basic", {
        "prompt_number": "How many Fibonacci digits do you seek, young padawan? (1-100): ",
        "prompt_again": "Try again you must? (Y/N): ",
        "invalid_number": "Wrong it is. Choose a natural number between 1 and 100.",
        "invalid_choice": "Wrong choice. Say Y or N, or face the dark side.",
        "invalid_language": "Invalid selection. Use the Force and choose 1-5.",
        "exit": "May the Force be with you. Exiting...",
        "back": "Back to galactic tongue selection.",
        "heading": "Fibonacci holonumbers:",
        "plot_title": "Fibonacci Ratios → Golden Holoratio",
        "plot_xlabel": "n (sequence index)",
        "plot_ylabel": "f(n)/f(n-1)",
    }, ["megacredit", "gigacredit", "teracredit", "petacredit", "exacredit"]),
}

# Wandelt große Zahlen in gerundete Einheiten (z. B. "1.23 Millionen") um
def round_number(n, units):
    if n < 1_000_000:
        return str(n)
    else:
        powers = [1_000_000, 1_000_000_000, 1_000_000_000_000,
                  1_000_000_000_000_000, 1_000_000_000_000_000_000]
        for i, p in reversed(list(enumerate(powers))):
            if n >= p:
                return f"{n/p:.2f} {units[i]}"
        return str(n)

# Berechnet die Fibonacci-Zahlen bis zur n-ten Position
def fibonacci(n):
    if n == 42:
        return "Die Antwort auf das Leben, das Universum und alles!"
    fibs = [0, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:n]

# Erstellt eine Plot-Grafik der Quotienten f(n)/f(n-1)
def plot_fibonacci_ratios(fibs, lang_data):
    if isinstance(fibs, str): return
    quotients = [fibs[i] / fibs[i-1] for i in range(2, len(fibs)) if fibs[i-1] != 0]
    plt.plot(range(2, len(fibs)), quotients, marker='o')
    plt.title(lang_data["plot_title"])
    plt.xlabel(lang_data["plot_xlabel"])
    plt.ylabel(lang_data["plot_ylabel"])
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Hauptfunktion des Programms
def main():
    while True:
        for key, (name, _, _) in languages.items():
            print(f"{key}: {name}")  # Sprachoption anzeigen
        lang_choice = input("->").strip()
        if lang_choice not in languages:
            print("Ungültige Auswahl. Bitte wähle eine gültige Sprache.")
            continue

        lang_name, lang_data, units = languages[lang_choice]

        while True:
            num_input = input(lang_data['prompt_number']).strip()
            if num_input.lower() == 'x':
                print(lang_data['back'])
                break
            if not num_input.isdigit() or not (1 <= int(num_input) <= 100):
                print(lang_data['invalid_number'])
                continue
            count = int(num_input)
            result = fibonacci(count)
            print("\n" + lang_data['heading'])

            if isinstance(result, str):
                print(result)
            else:
                for num in result:
                    print(f"{num} ({round_number(num, units)})")  # Zeilenweise Ausgabe
                # Die alte Komma-getrennte Ausgabe wurde entfernt

                plot_fibonacci_ratios(result, lang_data)

            while True:
                again = input(lang_data['prompt_again']).strip().lower()
                yes_char = lang_data['prompt_again'][lang_data['prompt_again'].find('(')+1].lower()
                no_char = lang_data['prompt_again'][lang_data['prompt_again'].find('/')+1].lower()
                if again == yes_char:
                    break
                elif again == no_char:
                    print(lang_data['exit'])
                    sys.exit()
                else:
                    print(lang_data['invalid_choice'])

# Start des Programms
if __name__ == "__main__":
    main()

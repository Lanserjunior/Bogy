print("-" * 45)

# Kopfzeile
print("| * ", end="")
for i in range(1, 11):
    print(f"|{i:>3}", end="")
print("|")

print("|---"*11 + "|")

# Tabelleninhalt
for i in range(1, 11):
    print(f"|{i:>3}", end="")  # Zeilenkopf
    for j in range(1, 11):
        print(f"|{i * j:>3}", end="")
    print("|")

print("-" * 45)

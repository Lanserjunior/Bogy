#lines = []
#header = "|   "

#for multiplikator in range(1,11):
#    line = "|" + f"{multiplikator}".rjust(3)
#    header += "|" + f"{multiplikator}".rjust(3)
#    for multiplikand in range(1,11):
#        line += "|" + f"{multiplikator * multiplikand}".rjust(3)
#    lines.append("|---" + "+---"*10 + "|")
#    lines.append(line+ "|")

#print ("/" + "-"*43 + "\\")
#print (header + "|")
#for line in lines:
#    print (line)
#print("\\" + "-"*43 + "/")

Void = "\n\n\n\n"

Horizontale_Linie = "=" * 50

Zwischen_Linie = " " + ("-" * 63)

Simon = "Depressiv"

Leerzeichen = " "

Erste_Zeile = " | *  | 1  | 2  | 3  | 4   | 5   | 6   | 7   | 8   | 9   | 10  |"

Zweite_Zeile = " | 1  | 1  | 2  | 3  | 4   | 5   | 6   | 7   | 8   | 9   | 10  |"

Dritte_Zeile = " | 2  | 2  | 4  | 6  | 8   | 10  | 12  | 14  | 16  | 18  | 20  |"

Vierte_Zeile = " | 3  | 3  | 6  | 9  | 12  | 15  | 18  | 21  | 24  | 27  | 30  |"

#-----------------------------------------------------------

print(Horizontale_Linie)

print(Void)

print(Zwischen_Linie)

print(Erste_Zeile)
  
print(Zwischen_Linie)

print(Zweite_Zeile)

print(Zwischen_Linie)

print(Dritte_Zeile)

print(Zwischen_Linie)

print(Vierte_Zeile)

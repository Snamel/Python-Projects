print("hur mycket skatt ska du betala kalkylator 2000")

lön = int(input("Ange din månadslön i hela kronor: "))
print("\n")

kskatt = lön * 0.2136
lskatt = lön * 0.1148

netto = lön - kskatt - lskatt

print("Månadslön", lön, "kr")
print("Kommunalskatt", kskatt, "kr")
print("Landstingskatt", lskatt, "kr")
print("Kvar efter skatt", netto, "kr")
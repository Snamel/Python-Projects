print("hur mycket skatt ska du betala kalkylator 2000")

lön = int(input("Ange din månadslön i hela kronor: "))
print("\n")

kskatt = lön * 0.2136
lskatt = lön * 0.1148
netto = lön - kskatt - lskatt
if lön * 12 < 19247:
    print("Månadslön", lön, "kr"," (Årslön: ", lön*12,"kr)")
    print("Kvar efter skatt", lön,"kr")
else:
    print("Du behöver betala skatt eftersom din årslön är högre än 19247kr", "\n")
    print("Månadslön", lön, "kr", " (Årslön: ", lön*12,"kr)")
    print("Kommunalskatt", kskatt, "kr")
    print("Landstingskatt", lskatt, "kr")
    print("Kvar efter skatt", netto, "kr")
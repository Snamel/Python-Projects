print("hur mycket skatt ska du betala kalkylator 2000")

lön = int(input("Ange din månadslön i hela kronor: "))
print("\n")

rubrik = "Du behöver  betala en statlig skatt eftersom din årslön är högre än 468700kr"
kskatt = 0
lskatt = 0
sskatt = 0
vskatt = 0

if lön * 12 < 19247:
    rubrik = "Du behöver inte betala en skatt eftersom din årslön är lägre än 19247kr"

elif lön * 12 < 468700:
    rubrik = "Du behöver betala en kommunal skatt och en landstingsskatt eftersom din årslön är högre än 19247kr"
    kskatt = 0.2136
    lskatt = 0.1148

elif lön * 12 < 675700:
    rubrik = "Du behöver betala en statlig skatt eftersom din årslön är högre än 468700kr"
    kskatt = 0.2136
    lskatt = 0.1148
    sskatt = 0.2

else:
    rubrik = "Du behöver betala en värnskatt eftersom din årslön är högre än 675700kr"
    kskatt = 0.2136
    lskatt = 0.1148
    sskatt = 0.2
    vskatt = 0.05

netto = lön - lön * (- kskatt - lskatt - sskatt - vskatt)

print(rubrik, "\n")
print("Månadslön", lön, "kr", " (Årslön: ", lön * 12, "kr)")
print("Kommunalskatt", lön * kskatt, "kr")
print("Landstingskatt", lön * lskatt, "kr")
print("Statlig skatt", lön * sskatt, "kr")
print("Värnskatt", lön * vskatt, "kr")
print("Kvar efter skatt", netto, "kr")

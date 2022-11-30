"""
    Jag har lärt mig använda "f-print" för att skriva ut variabler blandat med text snyggare.
    Jag har även lärt min inline if statements. Jag använde det för att skriva in if statements in i print statements. 

"""

print('\033[1m'"Skattkalkylator 3000"'\033[1m'"/""\n")

lön = int(input("Ange din månadslön i hela kronor: "))
print("\n")

rubrik = ""
kskatt = 0
lskatt = 0
sskatt = 0
vskatt = 0


if lön * 12 < 19247:
    rubrik="Du behöver inte betala en skatt eftersom din årslön är lägre än 19247kr"

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
tskatt = lön * (kskatt + lskatt + sskatt + vskatt)

print(
    f"Månadslön {lön} kr (Årslön: {lön * 12} kr)",
    f"\nKommunalskatt {int(lön * kskatt)}kr" if kskatt else "",
    f"\nLandstingskatt: {int(lön * lskatt)}kr" if lskatt else "",
    f"\nStatlig skatt: {int(lön * sskatt)}kr" if sskatt else "",
    f"\nVärnskatt {int(lön * vskatt)}kr" if vskatt else "",
    "\nKvar efter skatt",int(netto), "kr",
    "\nTotal skatt", int(tskatt), "kr" if tskatt else "",
    f"\nTotal skatt: {round( (tskatt / lön) * 100, 2)}%",
)
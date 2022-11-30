""" Jag har lärt mig använda Tuple och formatera listor i olika kollumner samt avstånd mellan dem"""

print('\033[1m'"Skattkalkylator 3000"'\033[1m'"\n")


def get_taxes(lön):
    kskatt = 0
    lskatt = 0
    sskatt = 0
    vskatt = 0


    if lön * 12 < 19247:
        pass

    elif lön * 12 < 468700:
        kskatt = 0.2136
        lskatt = 0.1148

    elif lön * 12 < 675700:
        kskatt = 0.2136
        lskatt = 0.1148
        sskatt = 0.2

    else:
        kskatt = 0.2136
        lskatt = 0.1148
        sskatt = 0.2
        vskatt = 0.05

    netto = lön - lön * (- kskatt - lskatt - sskatt - vskatt)
    tskatt = lön * (kskatt + lskatt + sskatt + vskatt)

    alön = lön * 12

    return {"alön": alön, "tskatt": tskatt, "netto": netto, "kskatt": kskatt, "lskatt": lskatt, "sskatt": sskatt, "vskatt": vskatt, "tskatt": tskatt}  #kskatt, lskatt, sskatt, vskatt}


tal = [1500, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000]

cols = "| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<12} | {:<10} | {:<10} | {:<15} |"
print(cols.format("Årslön", "Månadslön", "Totalskatt", "Netto/mån", "Kommunals.", "Landstingss.", "Statlig s.", "Värnskatt", "Total skatt i %"))

for t in tal:

    taxes = get_taxes(t)
    print(cols.format(int(taxes["alön"]), int(t), int(taxes["tskatt"]), int(taxes["netto"]), int(taxes["kskatt"] * t), int(taxes["lskatt"] * t), int(taxes["sskatt"] * t), int(taxes["vskatt"] * t), int(taxes["tskatt"])))

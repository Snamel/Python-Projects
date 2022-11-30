# var list
l = []
# for loop där du frågar efter tal, bryt ut loopen om man inte skriver in något
while True:
    try:
        a = int(input("Ange ett tal "))
        if a == 0:
            print("Inmatat tal: 0, programmet avbryts.")
            break
        l.append(a)
    except ValueError:
        print("Not a number")
    total = 0
    for i in l:
        total += i
    l.sort()
    print("Inmatat tal:", a, ", ", "min: ", l[0], ",", "max: ", l[-1], ", ", "Summan: ", total)

# print lägsta, högsta och summan av listan
print("Hela listan: ", l, ", ",   "min: ", l[0], ", ", "max: ", l[-1], ", ", "Summan: ", total)

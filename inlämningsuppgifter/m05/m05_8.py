resultat = [29, 86, 2, 79, 76, 55, 16, 50, 91, 76, 28, 41, 27, 31, 58, 61, 81, 94, 49, 13, 65, 48, 6, 46, 32]

resultat.sort()


def res():
    print(str(resultat).replace("[", "").replace("]", ""))
    print("\n""Medelvärdet av provresultatet är: ", sum(resultat) / len(resultat))
    m1 = resultat[int(len(resultat) / 2)]
    print("\n""Medianen av provresultatet är: ", m1)


res()

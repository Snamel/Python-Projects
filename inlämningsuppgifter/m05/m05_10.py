# skapar ett dokument som heter utskrift.txt
with open('utskrift.txt', 'w') as fw:
    # skriver i utskrift.txt "1 2 3 4 5 6 7 8 9" i ett 3x3 nät
    fw.write('''1 2 3
4 5 6
7 8 9
''')
# skriver i utskrift.txt på en ny rad "Här var det rutigt!"
    fw.write('\nHär var det rutigt!')
# öppnar och printar ut det som står i utskrift.txt till consolen.
with open('utskrift.txt', 'r') as fr:
    print(fr.read())

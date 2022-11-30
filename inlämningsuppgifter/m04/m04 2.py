print("Denna applikation gör ett antal beräkningar på en rektangel/rätblock.")

while True:
    a = int(input("Ange rektangelns ena sida "))
    b = int(input("Ange rektangelns andra sida "))
    area = a*b

    print(f"Rektangeln har sidorna {a} och {b} vilket gör att arean är {a*b}")
    if a==b:
        print("Eftersom bägge sidorna är lika långa så är denna rektangel en kvadrat.")

    cols = "| {:10} | {:10} |"
    print("\n" + cols.format("Area", "Volym"))
    print("|------------|------------|")
    for i in range(1, 11):
        print(cols.format(i, area*i))

    run = input("Vill du göra en ny beräkning (j/n)? ")
    if run == "j":
        pass
    elif run == "n":
        break

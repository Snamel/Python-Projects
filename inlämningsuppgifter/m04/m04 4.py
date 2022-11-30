print("Denna applikation gör ett antal beräkningar på en rektangel/rätblock.")

while True:
    a = int(input("Ange rätblockets ena sida: "))
    b = int(input("Ange rätblockets andra sida: "))
    c = int(input("Ange höjden för rätblocket: "))
    if c <= 0:
        c = 1
    area = a*b
    volym = a*b*c
    omkrets = a*2+b*2

    print(f"Rätblocket har sidorna {a} och {b} vilket gör att arean är {a*b}")
    if a == b == c:
        print("Eftersom alla sidor är lika långa så är rätblocket en kub.")

    cols = "| {:10} | {:10} | {:10} |"
    print("\n" + cols.format("Area", "Volym", "Omkrets"))
    print("|------------|------------|------------|")
    for i in range(1, 11):
        print(cols.format(i, volym*i, omkrets*i))

    run = input("Vill du göra en ny beräkning (j/n)? ")
    if run == "j":
        pass
    elif run == "n":
        break

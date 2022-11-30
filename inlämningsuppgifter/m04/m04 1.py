#
print("Denna applikation gör ett antal beräkningar på en rektangel/rätblock.")
a = int(input("Ange en sida på en rektangel "))
b = int(input("Ange den andra sidan på rektanglen "))
area = a*b

print(f"Rektangeln har sidorna {a} och {b} vilket gör att arean är {area}")
if a == b:
    print("Eftersom bägge sidorna är lika långa så är denna rektangel en kvadrat.")

cols = "| {:10} | {:10} |"
print("\n" + cols.format("Area", "Volym"))
print("|------------|------------|")
for i in range(1, 11):
    print(cols.format(i, area*i))

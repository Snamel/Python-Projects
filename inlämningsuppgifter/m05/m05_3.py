import math

r = float(input("Ange radien till en cirkel: "))
d = r*2


def radie():
    print("Radien till cirklen är", r*math.pi)


def omkrets():
    print("Omkretsen till cirken är", d*math.pi)


radie()
omkrets()

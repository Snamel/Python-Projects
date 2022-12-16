import math


def cirkel_area(radie):
    return math.pi * radie**2


def cirkel_omkrets(radie):
    return 2 * math.pi * radie


radie = float(input("Ange cirkelns radie: "))

area = cirkel_area(radie)
omkrets = cirkel_omkrets(radie)

print(f"Area: {area}")
print(f"Omkrets: {omkrets}")

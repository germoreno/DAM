v1 = float(input("Velocitat 1: "))
v2 = float(input("Velocitat 2: "))
d = float(input("Distancia: "))

kmh = v1 - v2
hores = d / kmh
minuts = hores * 60


print("tardara "+str(minuts)+" minuts en arribar")
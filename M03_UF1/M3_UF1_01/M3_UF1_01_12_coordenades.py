import math

x1 = float(input("Punt x1: "))
y1 = float(input("Punt y1: "))

x2 = float(input("Punt x2: "))
y2 = float(input("Punt y2: "))


distancia = math.sqrt((x2 - x1)**2 + (y2 - x1)**2)

print("La distancia total entre els dos punts es "+str(distancia))
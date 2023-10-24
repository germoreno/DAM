import math

num = float(input("Numero: "))

aQuadrada = num ** (1/2)
mathAQ = math.sqrt(num)

aCubica = num ** (1/3)
mathAC = math.cbrt(num)

print("Arrel quadrada normal es "+str(aQuadrada))
print("Arrel quadrada math es "+str(mathAQ))
print("Arrel cubica normal es "+str(aCubica))
print("Arrel cubica math es "+str(mathAC))
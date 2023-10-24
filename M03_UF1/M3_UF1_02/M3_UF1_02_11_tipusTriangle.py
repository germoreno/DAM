a = float(input("Costat A: "))
b = float(input("Costat B: "))
c = float(input("Costat C: "))

if a**2 + b**2 == c**2:
    print("El triangle es rectangle")
elif a == b == c:
    print("El triangle es equilàter")
elif a == b or a == c or b == c:
    print("El triangle es isòsceles")
else:
    print("El triangle es escalè")
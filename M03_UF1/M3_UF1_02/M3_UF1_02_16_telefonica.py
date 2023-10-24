minuts = float(input("Minuts de la trucada: "))
tipus = int(input("1. Diumenge 2. Matí 3. Tarda "))

if tipus == 1:
    if minuts <= 5:
        total = 1 + (1 * 0.03)
        print("El preu es",total,"euros")
    elif minuts <= 8:
        total = 1.8 + (1.8 * 0.03)
        print("El preu es",total,"euros")
    elif minuts <= 10:
        total = 2.5 + (2.5 * 0.03)
        print("El preu es",total,"euros")
    elif minuts > 10:
        total = 3 + (3 * 0.03)
        print("El preu es",total,"euros")
elif tipus == 2:
    if minuts <= 5:
        total = 1 + (1 * 0.15)
        print("El preu es",total,"euros")
    elif minuts <= 8:
        total = 1.8 + (1.8 * 0.15)
        print("El preu es",total,"euros")
    elif minuts <= 10:
        total = 2.5 + (2.5 * 0.15)
        print("El preu es",total,"euros")
    elif minuts > 10:
        total = 3 + (3 * 0.15)
        print("El preu es",total,"euros")
elif tipus == 3:
    if minuts <= 5:
        total = 1 + (1 * 0.1)
        print("El preu es",total,"euros")
    elif minuts <= 8:
        total = 1.8 + (1.8 * 0.1)
        print("El preu es",total,"euros")
    elif minuts <= 10:
        total = 2.5 + (2.5 * 0.1)
        print("El preu es",total,"euros")
    elif minuts > 10:
        total = 3 + (3 * 0.1)
        print("El preu es",total,"euros")
else:
    print("Resposta incorrecte")
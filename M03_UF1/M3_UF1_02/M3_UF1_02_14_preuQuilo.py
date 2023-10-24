pInicial = float(input("Preu inicial: "))
tipus = input("Tipus A o B: ")
grandaria = float(input("Grandaria 1 o 2: "))

if tipus == "A":
    if grandaria == 1:
        a1 = pInicial + 0.20
        print("El total es",a1,"euros el quilo")
    elif grandaria == 2:
        a2 = pInicial + 0.30
        print("El total es",a2,"euros el quilo")
elif tipus == "B":
    if grandaria == 1:
        b1 = pInicial - 0.30
        print("El total es",b1,"euros el quilo")
    elif grandaria == 2:
        b2 = pInicial - 0.50
        print("El total es",b2,"euros el quilo")
#primera manera
nom = input("Nom: ")
cognom1 = input("Cognom 1: ")
cognom2 = input("Cognom 2: ")

inicials = nom[0]
inicials = inicials + cognom1[0]
inicials = inicials + cognom2[0]

inicials = inicials.upper()

print("Les inicials són "+str(inicials))
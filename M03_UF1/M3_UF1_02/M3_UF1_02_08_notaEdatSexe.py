nota = int(input("Nota: "))
edat = int(input("Edat: "))
sexe = input("Sexe F o M:")

if nota >= 5 and edat >= 18 and sexe == "F":
    print("ACCEPTADA")
elif nota >= 5 and edat >= 18 and sexe == "M":
    print("POSSIBLE")
else:
    print("NO ACCEPTADA")
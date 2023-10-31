frase = input("Nom i cognoms: ")

espai = True

for i in frase:
    if i == " ":
        espai = True
    else:
        if espai == True:
            print(i.upper(), end=". ")
            espai = False
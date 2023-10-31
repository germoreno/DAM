frase = input("Frase: ")

cont = 1

for i in frase:
    if i == " ":
        cont += 1

print("El total de paraules es",cont)
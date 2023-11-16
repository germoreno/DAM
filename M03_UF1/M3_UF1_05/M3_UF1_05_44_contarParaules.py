frase = input("Frase: ")

paraules = frase.split()
paraulesNum = len(paraules)
print("La frase te",paraulesNum)

cont = 0

if frase != "" and frase != " ":
    cont = 1
    for i in frase:
        if i == " ":
            cont += 1

print("El total de paraules es",cont)


frase = input("Frase: ")
char = input("Caracter: ")

cont = 0

for i in frase:
    if i == char:
        cont += 1

print("El numero de vegades que s'ha imprimit",char,"es",cont)
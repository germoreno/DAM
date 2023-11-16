frase = input("Frase: ")
char = input("Caracter: ")

while not char.isalpha():
    char = input("No has introduït una lletra. Introdueix un caracter: ")

cont = 0

for i in frase:
    if i == char:
        cont += 1

print("El numero de vegades que s'ha imprimit",char,"es",cont)
print(f"El caracter {char} surt",frase.count(char),"vegades")
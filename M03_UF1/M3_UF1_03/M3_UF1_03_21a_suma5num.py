cont = 0
suma = 0

while cont != 5:
    num = int(input("Nombre: "))

    if num % 2 != 0:
        suma = suma + num
        cont += 1

print(suma)
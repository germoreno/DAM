cont = int(input("Quantitat: "))
suma = 0

while cont != 0:
    num = int(input("Nombre: "))

    if num % 2 != 0:
        suma = suma + num
        cont -= 1

print(suma)
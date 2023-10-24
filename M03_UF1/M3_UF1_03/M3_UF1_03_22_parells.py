cont = 0
suma = 0

while cont != 101:

    if cont % 2 == 0 and cont >= 2 and cont <= 100:
        suma = suma + cont

    cont += 1

print(suma)
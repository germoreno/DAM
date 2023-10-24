cont = int(input("Nombre de hores: "))
preuHora = float(input("Preu hora treballada: "))
suma = 0

while cont != 0:
    if cont > 40:    
        suma = suma + preuHora * 1.5
    else:
        suma = suma + preuHora

    cont -= 1

print(suma)
nombres = input("Digues una llista de nombres: ")

suma = 0
num = 0
maxim = 0
minim = 10

for i in nombres:
    a = int(i)
    if a == 0:
        break
    if a > maxim:
        maxim = a
    if a < minim:
        minim = a
    suma += a
    num += 1

mitjana = suma/num

print(maxim, minim,mitjana )
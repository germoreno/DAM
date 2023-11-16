num = int(input("Introdueix un numero: "))

suma = 0
cont = 0

array = []
array.append(num)

while num != 0:
    num = int(input("Introdueix un numero: "))
    
    if num == 0:
        break

    array.append(num)

for i in array:
    print(i, end=" ")
    suma = suma + i
    cont += 1


print()
print("Suma:",suma)
print("Quantitat:",cont)

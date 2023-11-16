cont = 0

array = []

for i in range(10):
    num = input("Introdueix numeros o lletres: ")

    array.append(num)

num2 = input("Numero o lletra a buscar: ")

for i in array:
    print(i, end=" ")
    if num2 == i:
        print()
        print("Posició:",cont)
        break
    elif cont == 9:
        print()
        print("No s'ha trobat")
        break
    cont += 1
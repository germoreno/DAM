frase = input("Digues una frase: ")
contador = False
total = 0

for i in frase:
    if i == "l" or contador == True:
        contador = True
        if i == 'a':
            total += 1
            contador = False


print(total)
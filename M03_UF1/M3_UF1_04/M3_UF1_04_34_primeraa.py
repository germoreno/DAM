frase = input("Digues una frase: ")

total = 0
trobar = False

for i in frase:
    if ((i == 'a' or i == 'A') or trobar == True):
        trobar = True
        total += 1


print("Total: ", total)
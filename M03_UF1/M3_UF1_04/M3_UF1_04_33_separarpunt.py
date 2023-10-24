frase = input("Digues una frase: ")

total = 0

for i in frase:
    if i == ".":
        break
    else:
        total += 1 


print("Total: ", total)
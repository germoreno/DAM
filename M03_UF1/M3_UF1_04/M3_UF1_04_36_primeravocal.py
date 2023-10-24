frase = input("Digues una frase: ")


vocals = ["a","e","i","o","u","A","E","I","O","U"]

for i in frase:
    if i in vocals:
        total = i
        break
    



print("Vocal: ", total)
frase = input("Digues una frase: ")

totalA = 0
totalB = 0

for i in frase:
    if i == "a" or i == "A":
        totalA += 1
    elif i == "b" or i == "B":
        totalB += 1


print("Total a : ", totalA, "Total b: ", totalB)
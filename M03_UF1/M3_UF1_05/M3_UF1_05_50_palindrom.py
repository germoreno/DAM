frase = input("Frase: ")

if frase == frase[::-1]:
    print("Es palíndrom")
else:
    print("No es palíndrom")

print(frase[::-1])
lletra = input("Lletra: ")

ascii = ord(lletra[0])

if ascii >= 65 and ascii <= 90: 
    print("Es majuscula")
else:
    print("No es majuscula")

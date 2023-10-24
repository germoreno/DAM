contador = 0
while contador < 3:
    clau = input("Digues la clau: ")
    if clau == "eureka":
        break
    else:
        contador += 1
        print("Has esgotat", contador, "de 3 tres intents")
        
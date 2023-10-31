f1 = input("Frase 1: ")
f2 = input("Frase 2: ")

if f1[0] == f2[0]:
    print("Comença igual")
else:
    print("Comença diferent")

if f1.startswith(f2) == True:
    print("Comença igual")
else:
    print("Comença diferent")
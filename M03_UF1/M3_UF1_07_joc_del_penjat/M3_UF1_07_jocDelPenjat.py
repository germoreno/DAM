vida = 10
penjat = False
pCompleta = False
acert = True
arrayPS = []
arrayP = []

paraulaS = input("Paraula secreta: ")

mida = len(paraulaS) 

print("Tria dificultat: \n1. facil \n2. mitja \n3. dificil")
dificultat = int(input())

if dificultat == 1:
    vida = 10
    print(" _     \n |     \n |     \n |      \n |      \n |_____")
elif dificultat == 2:
    vida = 6
    print(" ____  \n |  |  \n |     \n |      \n |      \n |_____")
elif dificultat == 3:
    vida = 3
    print(" ____  \n |  |  \n |  O  \n | /|   \n |      \n |_____")

for i in paraulaS:
    arrayPS.append(i)
    arrayP.append(i)

for i in range(mida):
    arrayP[i] = "-"
    print(arrayP[i], end="")

while penjat == False and pCompleta == False:
    acert = False
    print()
    lletra = input("Lletra: ")

    for i in range(mida):
        if lletra == arrayPS[i]:
            arrayP[i] = arrayPS[i]
            acert = True

    if acert == False:
        vida -= 1
        if vida == 10:
            print(" _     \n |     \n |     \n |      \n |      \n |_____")
        elif vida == 9:
            print(" __    \n |     \n |     \n |      \n |      \n |_____")
        elif vida == 8:
            print(" ___   \n |     \n |     \n |      \n |      \n |_____")
        elif vida == 7:
            print(" ____  \n |     \n |     \n |      \n |      \n |_____")
        elif vida == 6:
            print(" ____  \n |  |  \n |     \n |      \n |      \n |_____")
        elif vida == 5:
            print(" ____  \n |  |  \n |  O  \n |      \n |      \n |_____")
        elif vida == 4:
            print(" ____  \n |  |  \n |  O  \n |  |   \n |      \n |_____")
        elif vida == 3:
            print(" ____  \n |  |  \n |  O  \n | /|   \n |      \n |_____")
        elif vida == 2:
            print(" ____  \n |  |  \n |  O  \n | /|\\ \n |      \n |_____")
        elif vida == 1:
            print(" ____  \n |  |  \n |  O  \n | /|\\ \n | /    \n |_____")
        elif vida == 0:
            print(" ____  \n |  |  \n |  O  \n | /|\\ \n | / \\ \n |_____")

    for i in range(mida):
        print(arrayP[i], end="")

    if vida == 0:
        print()
        print("Has perdut! Tan penjat.")
        penjat = True

    if arrayP == arrayPS:
        print()
        print("Has guanyat! Paraula completa.")
        pCompleta = True
num = int(input("Nombre: "))
negatiu = bool(False)

while num != 0:
    num = int(input("Nombre: "))
    if num < 0:
        negatiu = True
    
if negatiu == False:
    print("Els numeros son positius")
elif negatiu == True:
    print("Hi ha numeros negatius")
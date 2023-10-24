num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))

abs(num1)
abs(num2)
if(num1 < num2):
    distancia = num2 - num1
elif(num1 >= num2):
    distancia = num1 - num2

print("La distancia total es "+str(distancia))
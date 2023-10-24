print("1. suma\n2. resta\n3. multiplicar\n4. dividir")
eleccio = int(input())

num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))

if(eleccio == 1):
    resposta = num1 + num2
elif(eleccio == 2):
    resposta = num1 - num2
elif(eleccio == 3):
    resposta = num1 * num2
elif(eleccio == 4):
    resposta = num1 / num2

print("la resposta es",resposta)
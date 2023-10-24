dia = int(input("Dia: "))
mes = int(input("Mes: "))
any = int(input("Any: "))

if dia > 0 and dia <= 31 and mes > 0 and mes <= 12 and any != 0:
    print("Es correcte")
else:
    print("No es correcte")
dia = int(input("Digues el dia: "))
mes = int(input("Digues el mes: "))
any2 = int(input("Digues el any: "))

a = False
mes30 = [4,6,9,11] 
mes31 = [1,3,5,7,8,10,12]

if(any2%4 == 0):
    if(any2%100 == 0):
        if(any2%400 == 0):
            m2 = 29
        else:
            m2 = 28
    else:
        m2 = 29
else:
    m2 = 28

if mes > 12:
    print('Error')
elif mes in mes31 and dia <=31:
    a = True
elif(mes in mes30 and dia <=30):
    a = True
elif mes == 2 and dia <=m2:
    a = True

if a == True:
    if mes == 1:
        print("Gener")
    elif mes == 2:
        print("Febrer")
    elif mes == 3:
        print("Març")
    elif mes == 4:
        print("Abril")
    elif mes == 5:
        print("Maig")
    elif mes == 6:
        print("Juny")
    elif mes == 7:
        print("Juliol")
    elif mes == 8:
        print("Agost")
    elif mes == 9:
        print("Septembre")
    elif mes == 10:
        print("Octubre")
    elif mes == 11:
        print("Nobembre")
    elif mes == 12:
        print("Decembre")
else:
    print("Error")
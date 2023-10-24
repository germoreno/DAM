any = int(input("Any: "))

if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
    print(any,"és any de trespas")
else:
    print(any,"no és any de trespas")

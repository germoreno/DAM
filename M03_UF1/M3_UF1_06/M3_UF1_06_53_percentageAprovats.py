num = int(input("Introdueix un numero: "))

aprovats = 0
suspes = 0

array = []

if num != -1:
    array.append(num)

    while num != -1:
        num = int(input("Introdueix un numero: "))
        
        if num == -1:
            break

        array.append(num)

    for i in array:
        if i >= 5:
            aprovats = aprovats + i
        else:
            suspes = suspes + i

    total = aprovats + suspes 

    paprovats = (aprovats * 100) / total
    psuspes = (suspes * 100) / total

    print("Aprovats: ",paprovats,"%")
    print("Suspesos:",psuspes,"%")
else:
    print("Error")
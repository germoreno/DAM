array = []

for i in range(4):
    array.append(input("Introdueix la data aaaa/mm/dd: "))

jove = ["3000","20","20"]
vell = ["0","0","0"]
for data in array:
    data_act = data.split("/")

if data_act[0]<jove[0]:
    jove = data_act
elif data_act[0] == jove[0]:
    if data_act[1] < jove[1]:
        jove = data_act
    elif data_act[1] == jove[1]:
        if data_act[2] < jove [2]:
            jove = data_act

if data_act[0] > vell[0]:
    vell = data_act
elif data_act[0] == vell[0]:
    if data_act[1] > vell[1]:
        vell = data_act
    elif data_act[1] == vell[1]:
        if data_act[2] > vell [2]:
            vell = data_act

print("El alumne mes jove es el nascut el",jove)
print("El alumne mes vell es el nascut el",vell)

if vell[0] == jove[0]:
    print("Tots dos son nascuts el mateix any")
else:
    print("No son nascuts el mateix any")

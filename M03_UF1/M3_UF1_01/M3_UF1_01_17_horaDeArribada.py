hores = int(input("Hores: "))
minuts = int(input("Minuts: "))
segons = int(input("Segons: "))
tSegons = int(input("Temps per arribar en segons: "))

#primera manera es peor tiene fallos
segons2 = int(tSegons % 60)
minuts2 = int((tSegons / 60) % 60)
hores2 = int((tSegons / 60) // 60)

totalHores = hores + hores2
totalMinuts = minuts + minuts2
totalSegons = segons + segons2

#segona manera
seginicial = hores * 3600 + minuts * 60 + segons
segfinal = seginicial + tSegons
horaarribada = segfinal // 3600
minarribada = (segfinal % 3600) // 60
segarribada = (segfinal % 3600) % 60

print("El temps per arribar es "+str(totalHores)+":"+str(totalMinuts)+":"+str(totalSegons))
print("El temps per arribar numero 2 es "+str(horaarribada)+":"+str(minarribada)+":"+str(segarribada))

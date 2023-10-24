minuts = int(input("Minuts: "))

thores = int(minuts / 60)
"thores = minuts // 60"
tminuts = minuts % 60

print("L'hora es "+str(thores)+":"+str(tminuts))
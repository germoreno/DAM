souBase = float(input("Sou base: "))
numComisio = float(input("Numero de comisions: "))

comisio = souBase * 0.1
tComisio = comisio * numComisio
tSou = souBase + tComisio

print("El total de les comisions es "+str(tComisio)+" i el sou total es "+str(tSou))
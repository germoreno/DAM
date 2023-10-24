eur2 = int(input("Quantes monedes de 2 euros: "))
eur1 = int(input("Quantes monedes de 1 euro: "))
cen50 = int(input("Quantes monedes de 50 centims: "))
cen20 = int(input("Quantes monedes de 20 centims: "))
cen10 = int(input("Quantes monedes de 10 centims: "))

euros = (eur2 * 2) + eur1
centims = (cen50 * 50) + (cen20 * 20) + (cen10 * 10)

teur = (centims // 100) + euros
tcen = centims % 100

print("El total de euros es "+str(teur)+"."+str(tcen))

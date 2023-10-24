qp1 = float(input("Qualificació parcial 1: "))
qp2 = float(input("Qualificació parcial 2: "))
qp3 = float(input("Qualificació parcial 3: "))

tParcial = (qp1 + qp2 + qp3) / 3

qe = float(input("Qualificació examen: "))
qt = float(input("Qualificació treball: "))

pParcial = tParcial * 0.55
pe = qe * 0.3
pt = qt * 0.15

total = pParcial + pe + pt

print("La qualificació total es "+str(total))
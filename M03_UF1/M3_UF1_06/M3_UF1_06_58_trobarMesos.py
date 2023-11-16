cont = 0

array = []

for i in range(12):
    array.append(input("Introdueix salari: "))

salari = input("Salari a buscar: ")

for i in array:
    if salari == i and cont == 0:
        print("El salari consideix en Gener: ",i)
    if salari == i and cont == 1:
        print("El salari consideix en Febrer: ",i)
    if salari == i and cont == 2:
        print("El salari consideix en Març: ",i)
    if salari == i and cont == 3:
        print("El salari consideix en Abril: ",i)        
    if salari == i and cont == 4:
        print("El salari consideix en Maig: ",i)
    if salari == i and cont == 5:
        print("El salari consideix en Juny: ",i)
    if salari == i and cont == 6:
        print("El salari consideix en Juliol: ",i)
    if salari == i and cont == 7:
        print("El salari consideix en Agost: ",i)
    if salari == i and cont == 8:
        print("El salari consideix en Setembre: ",i)
    if salari == i and cont == 9:
        print("El salari consideix en Octubre: ",i)
    if salari == i and cont == 10:
        print("El salari consideix en Novembre:",i)
    if salari == i and cont == 11:
        print("El salari consideix en Decembre:",i)

    cont += 1
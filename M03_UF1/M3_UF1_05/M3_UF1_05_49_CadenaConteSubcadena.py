frase = input("Frase: ")
subfrase = input("Subfrase: ")

res = frase.count(subfrase)

if res == 0:
    print("Quantitat:",res,"No hi ha subfrase")
else:
    print("Quantitat:",res,"Hi ha subfrase")

a = int(input("Nombre 1: "))
b = int(input("Nombre 2: "))
c = int(input("Nombre 3: "))

if a > b:
    a , b = b , a
if b > c:
    b , c = c , b
if a > c:
    a , c = c , a

print(a,b,c)

#segona manera
if a>b and a>c:
    if b>c:
        print(a,b,c)
    else:
        print(a,c,b)

if b>a and b>c:
    if a>c:
        print(b,a,c)
    else:
        print(b,c,a)

if c >= a and c >= b:
    if a>b:
        print(c,a,b)
    else:
        print(c,b,a)
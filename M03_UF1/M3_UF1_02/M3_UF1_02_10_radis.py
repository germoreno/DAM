import math

x1 = float(input("x1: "))
y1 = float(input("y2: "))
r1 = float(input("r1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
r2 = float(input("r2: "))

d = math.sqrt((x2 - x1)**2+(y2 - y1)**2)

if x1 == x2 and y1 == y2:
    print("Es concentriques") 

if d > (r1 + r2):
    print("Es exterior")

if d == (r1 + r2):
    print("Es tangent exterior")

if d < (r1 + r2) and d > abs(r1 - r2):
    print("Es secant")

if d > 0 and d < abs(r1 - r2):
    print("Es interior")

if d == abs(r1 - r2):
    print("Es tangent interior")

array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

a = array[-1]

for i in range(len(array)-1,0,-1):
        array[i] = array[i-1]

array[0] = a

print(array)
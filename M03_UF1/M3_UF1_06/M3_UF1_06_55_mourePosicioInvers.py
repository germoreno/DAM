array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

temp = array[0]

for i in range(0,len(array)-1,1):
        array[i] = array[i+1]

array[len(array)-1] = temp

for i in range(9):
        array[i] = array[i+1]

array[9] = temp

print(array)

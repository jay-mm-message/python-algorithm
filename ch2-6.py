from array import *

x = array('i', [1, 2, 3])
print('Data before pop(2)')
print(x)

elemt = x.pop(2)
print("Use 'pop' to extract the element at index 2 from an array: %d" % elemt)
print(x)
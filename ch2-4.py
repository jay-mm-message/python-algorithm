from array import *

x = array('i', [1, 2, 3, 4, 5])
print('Data before insertion')

for elemt1 in x:
  print(elemt1)

print('Insert the data 100 into the last position')
x.append(100)

for elemt2 in x:
  print(elemt2)
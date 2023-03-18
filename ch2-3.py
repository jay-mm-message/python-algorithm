from array import *

x = array('i', [1, 2, 3, 4, 5])

print('Date before insertion')
for elemt1 in x:
  print(elemt1)

x.insert(2, 100)
print('Insert the date 100 into the third position')

for elemt2 in x:
  print(elemt2)
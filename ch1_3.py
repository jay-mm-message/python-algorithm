# ch1_3.py
import itertools

arr_x = [1, 2, 3]
perm = itertools.permutations(arr_x)

for i in perm:
  print(i)
def create_btree(tree, data):
  for i in range(len(data)):
    level = 0
    if i == 0:
      tree[level] = data[i]
    else:
      while tree[level]:
        if data[i] > tree[level]:
          level = level * 2 + 2
        else:
          level = level * 2 + 1
      tree[level] = data[i]
    for j in range(len(data)):
      print("i = %d, level = %d, Binary tree[%d] = [%d]" % (i, level, j, tree[j]))

btree = [0] * 8
data = [10, 21, 5, 9, 13, 28]

create_btree(btree, data)
for i in range(len(btree)):
  print("Binary tree[%d] = %d" % (i, btree[i]))
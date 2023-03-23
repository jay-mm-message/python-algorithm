
def bubble_sort(nList):
  for i in range(len(nList)):
    for j in range(len(nList) - 1 - i):
      if nList[j] > nList[j+1]:
        nList[j], nList[j+1] = nList[j+1], nList[j]

list = [6, 1, 5, 7, 3]
print("The result before using the bubble sort algorithm for sort: {}"
        .format(list))
bubble_sort(list)
print("The result after using bubble sort algorithm for sort: {}"
      .format(list))

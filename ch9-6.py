
def selection_sort(nList):
    for i in range(len(nList) - 1):
        index = i
        for j in range(i+1, len(nList)):
            print("i = {}, j = {}".format(i, j))
            if nList[index] > nList[j]:
                index = j
        if index == i:
            pass
        else:
            max = nList[index]
            print("sort {} change: {}".format(list, max))
            nList[i], nList[index] = nList[index], nList[i]
    return nList

cars = ['honda', 'bmw', 'toyota', 'ford']
print("The result before using a selection sort algorithm for sort {}".format(cars))
print("The result after using a selection sort algorithm for sort {}".format(selection_sort(cars)))
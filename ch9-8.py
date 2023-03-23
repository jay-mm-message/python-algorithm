
def selection_sort(nList):
    n = len(nList)
    if n == 1:
        return nList
    else:
        for i in range(len(nList)):
            for j in range(i, 0, -1):
                if nList[j] < nList[j-1]:
                    min = nList[j]
                    print("mix: {}, list: {}".format(min, list))
                    nList[j], nList[j-1] = nList[j-1], nList[j]
                else:
                    break
    return nList

list = [6, 1, 5, 7, 3]
print("The result before using a selection sort algorithm for sort: {}".format(list))
sort_list = selection_sort(list)
print("The result after using a selection sort algorithm for sort: {}".format(sort_list))
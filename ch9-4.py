
def cocktail_sort(nList):
    is_sorted = True
    n = len(nList)
    start = 0
    end = n - 1

    while is_sorted:
        is_sorted = False
        for i in range(start, end, 1):
            if nList[i] > nList[i+1]:
                max = nList[i]
                nList[i], nList[i+1] = nList[i+1], nList[i]
                is_sorted = True
                print(">", nList, ", change: ", max)
        end = end - 1
        if not is_sorted:
            break
        for i in range(end - 1, start - 1, -1):
            if nList[i] > nList[i+1]:
                min = nList[i]
                nList[i], nList[i+1] = nList[i+1], nList[i]
                is_sorted = True
                print("<", nList, ", change: ", min)
        start = start + 1
    return nList
list = [6, 1, 5, 7, 3]
s1 = "The result before using the cocktail sort algorithm for sort "
print("{} {}".format(s1, list))
s2 = "The result after using the cocktail sort algorithm for sort "
print("{} {}".format(s1, cocktail_sort(list)))
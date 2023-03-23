
def selection_sort(nList):
    for i in range(len(nList) - 1):
        index = i
        for j in range(i+1, len(nList)):
            print("i = {}, j = {}".format(i, j))
            if nList[index][2] < nList[j][2]:
                index = j
        if index == i:
            pass
        else:
            max = nList[index]
            print("sort {} change: {}".format(list, max))
            nList[i], nList[index] = nList[index], nList[i]
    return nList

music = [('張敬軒', '斷點', 121234),
         ('藍心羽', '阿拉斯加海灣', 234352352),
         ('西柚', '愛過你這件事', 2352352)]

print('Youtube viewing charts.')
print("The result before using a selection sort algorithm for sort {}".format(music))
print("The result after using a selection sort algorithm for sort {}".format(selection_sort(music)))
print()
for i in range(len(music)):
    print("Top: {} : {}{} -- Number of views: {}".format(i+1, music[i][0], music[i][1], music[i][2]))
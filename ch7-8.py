import heapq

def heap_sort(tables):
    hs = []
    for t in tables:
        heapq.heappush(hs, t)
    return [ heapq.heappop(h) for i in range(len(tables))]

h = [10, 21, 5, 9, 13, 28, 3]
print(h)
heapq.heapify(h)
print(h)
print("heap sort: ", heap_sort(h))
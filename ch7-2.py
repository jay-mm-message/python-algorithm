import heapq

h = [10, 21, 5, 9, 13, 28, 3]
print("before heap creation", h)
heapq.heapify(h)
print("after heap creation", h)

heapq.heappush(h, 11)
print("first insertion", 11, h)
heapq.heappush(h, 2)
print("second insertion", 2, h)
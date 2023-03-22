import heapq

h = [10, 21, 5, 9, 13, 28, 3, 100]
print("before heap creation", h)
heapq.heapify(h)
print("after heap creation", h)

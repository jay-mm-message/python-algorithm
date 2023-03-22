import heapq

h = []

for i in range(10, 0, -1):
  heapq.heappush(h, i)

print(h)
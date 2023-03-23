from collections import deque

graph = {}
graph['Tom'] = ['Ivan', 'Ira', 'Kevin']
people = deque()
people += graph['Tom']

print("List the data type for people: ", type(people))
print("List search results: ", people)

while len(people) != 0:
  # Used to remove and return the leftmost (front) element from a deque (double-ended queue)."
  print(people.popleft())

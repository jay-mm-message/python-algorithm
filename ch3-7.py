class Node():
  def __init__(self, data = None):
    self.data = data
    self.next = None

n1 = Node(15)
n2 = Node(18)
n3 = Node(35)

n1.next = n2
n2.next = n3
n3.next = n1

pt = n1
count = 1

while count <= 6:
  print(pt.data)
  pt = pt.next
  count = count + 1
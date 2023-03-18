class Node():
  def __init__(self, data = None):
    self.data = data
    self.next = None

n1 = Node(15)
n2 = Node(18)
n3 = Node(20)

n1.next = n2
n2.next = n3

pt = n1

while pt:
  print(pt.data)
  pt = pt.next
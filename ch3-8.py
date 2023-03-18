class Node():
  def __init__(self, data = None):
    self.data = data
    self.previous = None
    self.next = None

class Double_linked_list():
  def __init__(self):
    self.head = None
    self.tail = None
  def add_double_linked_list(self, new_node):
    if isinstance(new_node, Node):
      if self.head == None:
        self.head = new_node
        new_node.previous = None
        new_node.next = None
        self.tail = new_node
      else:
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node
  def print_from_begining(self):
    pt = self.head
    while pt:
      print(pt.data)
      pt = pt.next
  def print_from_tail(self):
    pt = self.tail
    while pt:
      print(pt.data)
      pt = pt.previous

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

lists = Double_linked_list()
lists.add_double_linked_list(n1)
lists.add_double_linked_list(n2)
lists.add_double_linked_list(n3)

print("print from the begining")
lists.print_from_begining()

print("print from the tail")
lists.print_from_tail()
class Node():
  def __init__(self, data = None):
    self.data = data
    self.next = None

class Linked_list():
  def __init__(self):
    self.head = None
  def print_list(self):
    pt = self.head
    while pt:
      print(pt.data)
      pt = pt.next
  def insertBegin(self, NewData):
    newNode = Node(NewData)
    newNode.next = self.head
    self.head = newNode

n1 = Node(15)
n2 = Node(18)
n3 = Node(35)

n1.next = n2
n2.next = n3

lists = Linked_list()
lists.head = n1
print("Data before inserting into a linked list")
lists.print_list()

lists.insertBegin(100)
print("Data after inserting into a linked list")
lists.print_list()
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
  def insertEnd(self, NewData):
    newNode = Node(NewData)
    pt = self.head
    while pt.next:
      pt = pt.next
    pt.next = newNode
  def insertBetween(self, preNode, NewData):
    newNode = Node(NewData)
    newNode.next = preNode.next
    preNode.next = newNode
  def removeNode(self, data):
    pr = self.head

    while pr:
      if pr.data == data:
        break
      prev = pr
      pr = pr.next

    prev.next = pr.next

n1 = Node(15)
n2 = Node(18)
n3 = Node(35)

n1.next = n2
n2.next = n3

lists = Linked_list()
lists.head = n1
print("Before removing data from a linked list")
lists.print_list()

lists.removeNode(18)
print("After removing data from a linked list")
lists.print_list()
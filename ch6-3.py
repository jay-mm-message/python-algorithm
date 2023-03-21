class Node():
  def __init__(self, data = None):
    self.data = data
    self.left = None
    self.right = None
  def print_root(self):
    print(self.data)

n1 = Node(20)
n1.print_root()
class Node():
  def __init__(self, data = None):
    self.data = data
    self.left = None
    self.right = None
  def print_root(self):
    print(self.data)
  def insert(self, data = None):
    if self.data:
      if data < self.data:
        if self.left:
          self.left.insert(data)
        else:
          self.left = Node(data)
      else:
        if self.right:
          self.right.insert(data)
        else:
          self.right = Node(data)
    else:
      self.data = data
  def inorder(self):
    if self.left:
      self.left.inorder()
    print(self.data)
    if self.right:
      self.right.inorder()

tree = Node()
datas = [10, 21, 5, 9, 13, 28]

for d in datas:
  tree.insert(d)

tree.inorder()
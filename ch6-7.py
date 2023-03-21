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
  def preorder(self):
    print(self.data)
    if self.left:
      self.left.preorder()
    if self.right:
      self.right.preorder()
  def postorder(self):
    if self.left:
      self.left.postorder()
    if self.right:
      self.right.postorder()
    print(self.data)
  def search(self, val = None):
    if val < self.data:
      if not self.left:
        return str(val) + " not found"
      return self.left.search(val)
    elif val > self.data:
      if not self.right:
        return str(val) + " not found"
      return self.right.search(val)
    else:
      return str(val) + " have found"
class Delete_Node():
  def del_node(self, root, key):

    # find node 
    if root is None:
      return None
    if key < root.data:
      root.left = self.del_node(root.left, key)
      return root
    if key > root.data:
      root.right = self.del_node(root.right, key)
      return root
    if root.left is None:
      new_root = root.right
      return new_root
    if root.right is None:
      new_root = root.left
      return new_root

    # delete node
    succ = self.max_node(root.left)
    tmp = Node(succ.data)
    tmp.left = self.left_node(root.left)
    tmp.right = root.right
    return tmp
    
  def left_node(self, node):
    if node.right is None:
      new_root = node.left
      return new_root
    node.right = self.left_node(node.right)
    return node
  def max_node(self, node):
    while node.right:
      node = node.right
    return node

tree = Node()
datas = [10, 21, 5, 9, 13, 28]

for d in datas:
  tree.insert(d)

print("inorder")
tree.inorder()
print("preorder")
tree.preorder()
print("postorder")
tree.postorder()

print("search")
print(tree.search(13))
print(tree.search(100))

print("inorder")
tree.inorder()
del_data = 5
print("del data is %d" % (del_data))
delete_obj = Delete_Node()
result = delete_obj.del_node(tree, del_data)
result.inorder()

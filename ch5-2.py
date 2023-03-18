
class Stack():
  def __init__(self):
    self.my_stack = []
  def stack_push(self, data):
    self.my_stack.append(data)
  def stack_len(self):
    return len(self.my_stack)
  def stack_isEmpty(self):
    return self.my_stack == []
  def stack_pop(self):
    return self.my_stack.pop()

stack_1 = Stack()
print('Stack length: ', stack_1.stack_len())
for i in range(5):
  data = i + 1
  stack_1.stack_push(data)
  print('Stack push: ', data)
print('Stack length: ', stack_1.stack_len())
for i in range(10):
  if not stack_1.stack_isEmpty():
    print('Stack pop: ', stack_1.stack_pop(), ", count: ", i)
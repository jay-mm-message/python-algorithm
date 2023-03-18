
class Stack():
  def __init__(self):
    self.my_stack = []
  def stack_push(self, data):
    self.my_stack.append(data)
  def stack_len(self):
    return len(self.my_stack)

stack_1 = Stack()
print('Stack length: ', stack_1.stack_len())
for i in range(5):
  stack_1.stack_push(i)
print('Stack length: ', stack_1.stack_len())

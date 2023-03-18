class Queue():
  def __init__(self):
    self.queue = []
  def enqueue(self, data):
    self.queue.insert(0, data)
  def len_queue(self):
    return len(self.queue)
  def dequeue(self):
    if self.queue:
      return self.queue.pop()
    else:
      return "Queue is empty"

q1 = Queue()
q1.enqueue(10)
print(q1.queue, q1.queue[0])
q1.enqueue(20)
print(q1.queue, q1.queue[0])
q1.enqueue(30)
print(q1.queue, q1.queue[0])

print("queue len: ", q1.len_queue())

for x in range(5):
  print("dequeue: ", q1.dequeue(), ", count: ", x)
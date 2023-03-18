class Queue():
  def __init__(self):
    self.queue = []
  def enqueue(self, data):
    self.queue.insert(0, data)
  def len_queue(self):
    return len(self.queue)

q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)

print("queue len: ", q1.len_queue())
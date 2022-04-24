#배열을 이용한 원형큐 구현
#배열을 이용하여 선형큐를 구현할 경우 너무 비효율적이다. - 배열을 이용해서 큐를 구현할 경우에는 원형큐!


class CircularQueue:
  def __init__(self, size):
    self.elements = [None] * (size + 1)
    self.front = 0
    self.rear = 0
    self.max_size = size + 1

  def offer(self, data):
    if self.is_full():
      raise IndexError('Invalid')
    self.rear = (self.rear + 1) % self.max_size
    self.elements[self.rear] = data
    self.size += 1

  def poll(self):
    if self.is_empty():
      raise IndexError('Invalid')
    self.front = (self.front + 1) % self.max_size
    # self.elements[self.front] = None
    self.size -= 1

    return self.elements[self.front]

  def is_empty(self):
    return self.front == self.rear

  def is_full(self):
    return (self.rear + 1) % self.max_size == self.front

  def peek(self):
    if self.is_empty():
      raise ValueError('Invalid')

    
    return self.elements[(self.front + 1) % self.max_size]

  def size_(self):
    if self.front <= self.rear:
      return self.rear - self.front
    return self.max_size - self.front + self.rear

  def clear(self):
    self.front = 0
    self.rear = 0

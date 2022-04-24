class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

class LinkedQueue:
  def __init__(self):
    self.head = Node(None)
    self.tail = self.head
    self.size = 0

  def offer(self, data):
    new_node = Node(data)
    self.tail.next = new_node
    self.tail = self.tail.next
    self.size += 1

  def poll(self):
    if self.is_empty():
      raise ValueError('Invalid')
    curr = self.head.next
    self.head.next = curr.next
    curr.next = None
    self.size -= 1

    if self.head.next == None:
      self.tail = self.head

    return curr.data


  def is_empty(self):
    return self.head.next == None

  def peek(self):
    if self.is_empty():
      raise ValueError('Invalid')
    return self.head.next.data

  def size_(self):
    return self.size

  def clear(self):
    self.head.next = None
    self.tail = self.head
    self.size = 0

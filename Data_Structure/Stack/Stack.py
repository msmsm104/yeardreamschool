class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next


class Stack:
  def __init__(self):
    self.size = 0
    self.head = Node() #더미노드

  def push(self, data):
    new_node = Node(data, self.head.next)
    self.head.next = new_node

    self.size += 1
  
  def pop(self):
    if self.is_empty():
      raise ValueError('No value')
    curr = self.head.next
    self.head.next = curr.next
    curr.next = None

    self.size -= 1

    return curr.data

  def peek(self):
    if self.is_empty():
      raise ValueError('No value')
    return self.head.next.data

  def size_(self):
    return self.size

  def is_empty(self):
    return self.head.next == None
  
  

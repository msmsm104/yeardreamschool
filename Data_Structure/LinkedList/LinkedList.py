#더미 노드를 설정하여 LinkedList구현.

class Node:
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = Node() #더미 노드.
    self.size = 0

  def add(self, data):
    curr = self.head #더미 노드 head부터 탐색하는 pointer
    while curr.next != None:
      curr = curr.next
    new_node = Node(data)
    curr.next = new_node
    self.size += 1

  def insert(self, idx, data):
    if idx < 0 or idx > self.size:
      raise IndexError('Invalid Index')
    prev = self.head
    curr = prev.next

    i = 0
    while i < idx:
      prev = prev.next
      curr = curr.next
      i += 1

    new_node = Node(data, curr)
    prev.next = new_node
    self.size += 1

  def clear(self):
    self.size = 0
    self.head.next = None

  def delete(self, data):
    prev = self.head
    curr = prev.next

    while curr != None:
      if curr.data == data:
        prev.next = curr.next
        curr.next = None
        self.size -= 1
        return True
      prev = prev.next
      curr = curr.next
    return False

  def deleteByIndex(self, idx):
    self.outOfIndex(idx)
    prev = self.head
    curr = prev.next

    i = 0
    while i < idx:
      prev = prev.next
      curr = curr.next
      i += 1

    prev.next = curr.next
    curr.next = None
    self.size -= 1
    return True

  def outOfIndex(self, idx):
    if idx < 0 or idx > self.size - 1:
      raise IndexError('Invalid Index')

  def get(self, idx):
    self.outOfIndex(idx)
    curr = self.head.next

    i = 0
    while i < idx:
      curr = curr.next
      i += 1
    return curr.data

  def indexOf(self, data):
    curr = self.head.next

    idx = 0

    while curr != None:
      if curr.data == data:
        return idx
      curr = curr.next
      idx += 1
    return False

  def is_empty(self):
    return self.head.next == None #linkedlist 스럽게 구현.

  def contains(self, data):
    curr = self.head.next

    while curr != None:
      if curr.data == data:
        return True
      curr = curr.next
    return False

  def size_(self):
    return self.size

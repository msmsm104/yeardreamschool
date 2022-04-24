class Node:
  def __init__(self, data, next = None, prev = None):
    self.data = data
    self.next = next
    self.prev = prev

class DoubleLinkedList:
  def __init__(self):
    self.head = Node(None)
    self.tail = Node(None)
    self.size = 0
    self.head.next = self.tail
    self.tail.prev = self.head


  def size_(self):
    return self.size

  def clear(self):
    self.size = 0
    self.head.next = self.tail
    self.tail.prev = self.head

  def add(self, data): #tail 앞에 데이터 node를 삽입하는 method
    last = self.tail.prev
    new_node = Node(data, self.tail, last)
    last.next = new_node
    self.tail.prev = new_node
    self.size += 1

  def get(self, idx):
    if idx < 0 or idx >= self.size:
      raise IndexError('Invalid Index')

    curr = Node(None)

    i = 0

    if idx < self.size / 2:
      curr = self.head.next
      while i != idx:
        curr = curr.next
        i += 1

    else:
      curr = self.tail.prev
      while self.size - i - 1 != idx:
        curr = curr.prev
        i += 1

    return curr.data

  def insert(self, data, idx):
    if idx < 0 or idx >= self.size:
      raise IndexError('Invalid Index')

    prev = Node(None)
    curr = Node(None)
    
    i = 0

    if idx < self.size / 2:
      prev = self.head
      curr = prev.next

      while i < idx:
        prev = prev.next
        curr = curr.next
        i += 1
      
    else:
      prev = self.tail.prev
      curr = self.tail

      while i < self.size - idx:
        prev = prev.prev
        curr = curr.prev
        i += 1
      
    new_node = Node(data, curr, prev)
    prev.next = new_node
    curr.prev = new_node
    self.size += 1

  def deleteByIndex(self, idx):
    if idx < 0 or idx >= self.size:
      raise IndexError('Invalid Index!')

    prev = Node(None)
    curr = Node(None)

    i = 0

    if idx < self.size / 2:
      prev = self.head
      curr = self.head.next
      while i < idx:
        prev = prev.next
        curr = curr.next
        i += 1

    else:
      prev = self.tail.prev
      curr = self.tail
      while i < self.size - idx:
        prev = prev.prev
        curr = curr.prev
        i += 1

    prev.next = curr.next
    curr.next.prev = prev
    curr.next = None
    curr.prev = None
    self.size -= 1

  def contains(self, data):
    pointer_front = self.head.next
    pointer_back = self.tail.prev

    while pointer_front != pointer_back:
      if pointer_front.data == data or pointer_back.data == data:
        return True
      pointer_front = pointer_front.next
      pointer_back = pointer_back.prev
    return False


  def indexOf(self, data):
    pnt_front = self.head.next
    pnt_back = self.tail.prev

    idx_front = 0

    while pnt_front != pnt_back or pnt_front.data == data or pnt_back.data == data:
      if pnt_front.data == data:
        return idx_front
      if pnt_back.data == data:
        return self.size_() - idx_front - 1
      pnt_front = pnt_front.next
      pnt_back = pnt_back.prev
      idx_front += 1
      
    return False

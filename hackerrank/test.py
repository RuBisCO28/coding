class SinglyLinkedList:
  def __init__(self, data=0, next=None):
    self.data = data
    self.next = next

def has_cycle(head):
  current = head
  visited = set()
  while current:
    i = id(current)
    if i in visited:
      return 1
    visited.add(i)
    current = current.next
  return 0

if __name__ == '__main__':
  head = SinglyLinkedList(1,SinglyLinkedList(2,SinglyLinkedList(3)))
  print(has_cycle(head))

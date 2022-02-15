class SinglyLinkedListNode:
  def __init__(self, node_data):
    self.data = node_data
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def insert_node(self, node_data):
    node = SinglyLinkedListNode(node_data)

    if not self.head:
      self.head = node
    else:
      self.tail.next = node

    self.tail = node

def has_cycle(head):
  visited = set()
  f = head
  while f:
    i = id(f)
    if i in visited:
        return 1
    visited.add(i)
    f = f.next
  return 0

if __name__ == '__main__':
  index = int(input())
  llist_count = int(input())
  llist = SinglyLinkedList()

  for _ in range(llist_count):
    llist_item = int(input())
    llist.insert_node(llist_item)

  extra = SinglyLinkedListNode(-1)
  temp = llist.head

  for i in range(llist_count):
    if i == index:
      extra = temp

    if i != llist_count-1:
      temp = temp.next

  temp.next = extra

  result = has_cycle(llist.head)

  print(str(int(result)) + '\n')


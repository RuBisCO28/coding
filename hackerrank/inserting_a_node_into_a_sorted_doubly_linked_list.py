class DoublyLinkedListNode:
  def __init__(self, data=0, next=None, prev=None):
    self.data = data
    self.next = next
    self.prev = prev

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def insert_node(self, node_data):
    node = DoublyLinkedListNode(node_data)

    if not self.head:
      self.head = node
    else:
      self.tail.next = node
      node.prev = self.tail

    self.tail = node

def sortedInsert(llist, data):
  current = llist
  insert_node = DoublyLinkedListNode(data)
  if current.data >= data:
    insert_node.next = current
    current.prev = insert_node
    llist = insert_node
    return llist
  while(current.next is not None):
    if (current.data < data and current.next.data > data) or (current.data == data):
      insert_node.next = current.next
      current.next.prev = insert_node
      insert_node.prev = current
      current.next = insert_node
      return llist
    else:
      current = current.next
  if current.data <= data:
    insert_node.prev = current
    current.next = insert_node
    return llist

if __name__ == '__main__':
  arr = [1,3,4,10]
  llist = DoublyLinkedList()
  for i in range(len(arr)):
    llist.insert_node(arr[i])
  data = 5
  print(sortedInsert(llist.head, data))

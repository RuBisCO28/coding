class SinglyLinkedListNode: 
  def __init__(self, data=0, next=None): 
    self.data = data
    self.next = next

def insertNodeAtPosition(llist, data, position):
  current = llist
  l = 1
  insert_node = SinglyLinkedList()
  insert_node.data = data
  while(current is not None):
    if l == position:
      insert_node.next = current.next
      current.next = insert_node
    else:
      current = current.next
    l += 1
  return llist

if __name__ == '__main__':
  llist = SinglyLinkedListNode(16,SinglyLinkedListNode(13,SinglyLinkedListNode(7)))
  data = 1
  position = 2
  print(insertNodeAtPosition(llist, data, position))


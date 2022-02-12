class DoublyLinkedListNode: 
  def __init__(self, data=0, next=None, prev=None): 
    self.data = data
    self.next = next
    self.prev = prev

def reverse(llist):
  prev = None
  current = llist
  while(current is not None):
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
  llist = prev
  return llist
  

if __name__ == '__main__':
  llist = DoublyLinkedListNode(1,DoublyLinkedListNode(2,DoublyLinkedListNode(3,DoublyLinkedListNode(4,DoublyLinkedListNode(5)))))
  print(reverse(llist))


class SinglyLinkedListNode: 
  def __init__(self, data=0, next=None): 
    self.data = data
    self.next = next

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
  llist = SinglyLinkedListNode(1,SinglyLinkedListNode(2,SinglyLinkedListNode(3,SinglyLinkedListNode(4,SinglyLinkedListNode(5)))))
  print(reverse(llist))


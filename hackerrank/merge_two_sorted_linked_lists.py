class SinglyLinkedList:
  def __init__(self, data=0, next=None):
    self.data = data
    self.next = next

def mergeLists(head1, head2):
  dummyNode = SinglyLinkedList()
  tail = dummyNode
  while True:
    if head1 is None:
      tail.next = head2
      break
    if head2 is None:
      tail.next = head1
      break

    if head1.data <= head2.data:
      tail.next = head1
      head1 = head1.next
    else:
      tail.next = head2
      head2 = head2.next
    tail = tail.next
  return dummyNode.next

if __name__ == '__main__':
  head1 = SinglyLinkedList(1,SinglyLinkedList(3,SinglyLinkedList(7)))
  head2 = SinglyLinkedList(1,SinglyLinkedList(2))
  print(mergeLists(head1, head2))


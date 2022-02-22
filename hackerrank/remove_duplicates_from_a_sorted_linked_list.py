class SinglyLinkedList:
  def __init__(self, data=0, next=None):
    self.data = data
    self.next = next

def removeDuplicates(llist):
  current = llist
  while(current.next is not None):
    if current.data == current.next.data:
      current.next = current.next.next
    else:
      current = current.next
  # print(llist.data)
  # print(llist.next.data)
  # print(llist.next.next.data)
  return llist

if __name__ == '__main__':
  llist = SinglyLinkedList(1,SinglyLinkedList(2,SinglyLinkedList(2,SinglyLinkedList(3))))
  print(removeDuplicates(llist))


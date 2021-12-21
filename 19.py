from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def show(node):
  while True:
    if node and node.next:
      print(node.val + '-', end = '')
      node = node.next
    if node.next is None:
      print(node.val)
      break

class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    new_head = dummy_head = head
    l = 0
    while head:
      l += 1
      head = head.next
    stop = l - n
    if stop == 0: return new_head.next
    cnt = 1
    while dummy_head:
      if cnt == stop:
        dummy_head.next = dummy_head.next.next
        return new_head
      cnt += 1
      dummy_head = dummy_head.next

result = Solution()
head = ListNode(5,ListNode(4,ListNode(3, ListNode(2, ListNode(1)))))
n = 2
print(result.removeNthFromEnd(head, n))
# n1 = ListNode('A')
# show(n1)

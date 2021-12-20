from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if not head:
      return head
    if head.next is not None:
      head.next = self.removeNthFromEnd(head.next, n)
      return head
    else:
      return head

result = Solution()
head = ListNode(5,ListNode(4,ListNode(3, ListNode(2, ListNode(1)))))
n = 2
print(result.removeNthFromEnd(head, n))

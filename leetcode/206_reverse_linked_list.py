from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current_node = head
    while current_node is not None:
      next_node = current_node.next
      current_node.next = prev
      prev = current_node
      current_node = next_node
    head = prev
    return head

result = Solution()
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
print(result.reverseList(head))

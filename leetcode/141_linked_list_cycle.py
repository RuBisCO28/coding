from typing import Optional
from collections import deque

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

# Floyd's cycle-finding algorithm
# class Solution:
#   def hasCycle(self, head: Optional[ListNode]) -> bool:
#     if head is None:
#       return False
#     fast = head.next
#     slow = head

#     while fast != slow:
#       if fast is None or fast.next is None:
#         return False
#       print(fast.val,slow.val)
#       fast = fast.next.next
#       slow = slow.next
#       print(fast.val,slow.val)
#     return True

# hashmap
class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    hashmap = {}
    while head != None:
      if head in hashmap:
        return True
      hashmap[head] = head

result = Solution()
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
print(result.hasCycle(head))

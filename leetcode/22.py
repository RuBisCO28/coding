from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

# class Solution:
#   def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#     arr = []
#     if list1 is None and list2 is None:
#       return list1
#     if list1 is not None and list2 is None:
#       return list1
#     if list1 is None and list2 is not None:
#       return list2
#     while(list1.next is not None):
#       arr.append(list1.val)
#       if list1 is not None:
#         list1 = list1.next
#       if list1.next is None:
#         arr.append(list1.val)
#         break
#     while(list2.next is not None):
#       arr.append(list2.val)
#       if list2 is not None:
#         list2 = list2.next
#       if list2.next is None:
#         arr.append(list2.val)
#         break
#     ars = sorted(arr)
#     cnt = 0
#     print(ars)
#     dummyHead = ListNode(0)
#     current = dummyHead
#     while cnt < len(ars):
#       current.next = ListNode(ars[cnt])
#       current = current.next
#       cnt += 1
#     return dummyHead.next

# https://qiita.com/mhiro216/items/3232c7331dfaf899985a

class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 or not list2:
      return list1 or list2
    if list1.val < list2.val:
      list1.next = self.mergeTwoLists(list1.next, list2)
      return list1
    else:
      list2.next = self.mergeTwoLists(list1, list2.next)
      return list2

result = Solution()
# l1 = ListNode(4, ListNode(2, ListNode(1)))
# l2 = ListNode(4, ListNode(3, ListNode(1)))
l1 = ListNode(2)
l2 = ListNode(1)
print(result.mergeTwoLists(l1, l2))

from typing import Optional
from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# class Solution:
#   def isValidBST(self, root: Optional[TreeNode]) -> bool:
#     if root is None:
#       return []
#     queue = deque([root])
#     if root.left:
#       r_left = root.left.val
#     else:
#       r_left = 0
#     if root.right:
#       r_right = root.right.val
#     else:
#       r_right = 0
#     while queue:
#       for i in range(len(queue)):
#         node = queue.popleft()
#         if node.left:
#           print(node.left.val < r_left)
#           if node.val <= node.left.val or node.left.val < r_left:
#             return False
#           queue.append(node.left)
#         if node.right:
#           if node.right.val <= node.val or r_right < node.right.val:
#             return False
#           queue.append(node.right)
#     return True

class Solution:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    return self.isValid_helper(root,float('-inf'), float('inf'))

  def isValid_helper(self,node,low,high):
    if node is None:
      return True

    if node.val <= low or node.val >= high:
      return False

    return self.isValid_helper(node.left,low,node.val) and self.isValid_helper(node.right,node.val,high)

result = Solution()
# root = TreeNode(2,TreeNode(1),TreeNode(3))
# root = TreeNode(5,TreeNode(1),TreeNode(4,TreeNode(3),TreeNode(6)))
# root = TreeNode(5,TreeNode(4),TreeNode(6,TreeNode(3),TreeNode(7)))
root = TreeNode(3,TreeNode(1,TreeNode(0),TreeNode(2)),TreeNode(5,TreeNode(4),TreeNode(6)))
print(result.isValidBST(root))

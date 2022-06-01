from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    depth = 0

    l = [root] if root else []
    while l:
      depth += 1
      l_tmp = []
      for t in l:
        if t.left:
          # print(t.left.val)
          l_tmp.append(t.left)
        if t.right:
          # print(t.right.val)
          l_tmp.append(t.right)
      l = l_tmp
    return depth


result = Solution()
root = TreeNode(1,None,TreeNode(2))
print(result.maxDepth(root))


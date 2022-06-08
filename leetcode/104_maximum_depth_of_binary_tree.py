from typing import Optional

# https://www.youtube.com/watch?v=hTM3phVI6YQ

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Recursive DFS
# O(n)
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0

    return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

# BFS Solution
# O(n)
from collections import deque

class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0

    level = 1
    q = deque([root])
    while q:
      for i in range(len(q)):
        node = q.popleft()
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
      level += 1
    return level

# Iterrative DFS
# O(n)
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    depth = 0
    stack = [(root, 1)]

    while stack:
      node, l = stack.pop()
      if not node:
        return 0
      if l > depth:
        depth = l
      if root.left:
        stack.append((node.left,l+1))
      if root.right:
        stack.append((node.right,l+1))
    return depth

result = Solution()
root = TreeNode(1,None,TreeNode(2))
print(result.maxDepth(root))


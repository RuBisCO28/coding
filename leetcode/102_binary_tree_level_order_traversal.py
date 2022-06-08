import collections
from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    ans = []
    level = 0
    if root is None:
      return ans
    self.dfs(root,level,ans)
    return ans

  def dfs(self,root,level,ans):
    if not root:
      return
    if len(ans) < level + 1:
      ans.append([])
    ans[level].append(root.val)
    self.dfs(root.left,level+1,ans)
    self.dfs(root.right,level+1,ans)

# BFS
# O(n)
class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    res = []

    q = collections.deque()
    q.append(root)

    while q:
      qLen = len(q)
      level = []
      for i in range(qLen):
        node = q.popleft()
        if node:
          level.append(node.val)
          q.append(node.left)
          q.append(node.right)
      if level:
        res.append(level)
    return res

result = Solution()
root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
print(result.levelOrder(root))

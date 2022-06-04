from typing import Optional
from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
      return []
    queue = deque([root])
    answer = []
    direction = 1
    while queue:
      depth = []
      for i in range(len(queue)):
        node = queue.popleft()
        print(node.val)
        depth.append(node.val)
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
      answer.append(depth[::direction])
      direction *= (-1)
    return answer

result = Solution()
root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
root = TreeNode(5,TreeNode(4),TreeNode(6,TreeNode(3),TreeNode(7)))
print(result.zigzagLevelOrder(root))

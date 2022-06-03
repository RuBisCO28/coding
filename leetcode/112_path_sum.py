from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if root is None:
      return False

    if (targetSum == root.val) and root.left is None and root.right is None:
      return True
    else:
      return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)

result = Solution()
root = TreeNode(5,TreeNode(4,TreeNode(11,TreeNode(7),TreeNode(2)),None),TreeNode(8,TreeNode(13),TreeNode(4,None,1)))
# root = TreeNode(1,TreeNode(2),TreeNode(3))
print(result.hasPathSum(root,22))

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
  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
      return None

    preorderIndex = preorder[0]
    Tree = TreeNode(preorderIndex)
    inorderIndex = inorder.index(preorderIndex)

    print(inorderIndex,preorder[1:inorderIndex+1],inorder[:inorderIndex])
    Tree.left = self.buildTree(preorder[1:inorderIndex+1],inorder[:inorderIndex])
    Tree.right = self.buildTree(preorder[inorderIndex+1:],inorder[inorderIndex+1:])
    return Tree

result = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(result.buildTree(preorder,inorder))

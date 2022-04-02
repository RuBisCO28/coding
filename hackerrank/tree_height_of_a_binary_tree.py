def height(root):
  if root is None:
    return -1
  left_height = height(root.left) + 1
  right_height = height(root.right) + 1
  return max(left_height,right_height) 

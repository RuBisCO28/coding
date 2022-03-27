def decodeHuff(root, s):
  current = root
  result = ''
  for code in s:
    if int(code) == 0:
      current = current.left
    else:
      current = current.right
    if current.left is None and current.right is None:
        result += current.data
        current = root
  print(result)

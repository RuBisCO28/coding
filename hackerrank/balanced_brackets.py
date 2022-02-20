def isBalanced(s):
  flag = 0
  while True:
    flag = 0
    if '()' in s:
      s = s.replace('()','')
      flag += 1
    if '{}' in s:
      s = s.replace('{}','')
      flag += 1
    if '[]' in s:
      s = s.replace('[]','')
      flag += 1
    if flag == 0:
      answer = s
      break
  if answer == '':
    return 'YES'
  else:
    return 'NO'

if __name__ == '__main__':
  s = "{[()]}"
  s = "{{)[](}}"
  s = "{(([])[])[]}"
  print(isBalanced(s))


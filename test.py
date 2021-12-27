import math

def sequential(s,sub_string):
  if not s: return True
  if s.startswith(sub_string):
    l = len(sub_string)
    print(s[l:],str(int(sub_string)+1))
    return sequential(s[l:],str(int(sub_string)+1))
  return False

def separateNumbers(s):
  step = math.floor(len(s)/2)
  for i in range(1, step + 1):
    sub_string = s[:i]
    if sequential(s,sub_string):
      return "YES " + sub_string
  return 'NO'

if __name__ == '__main__':
  # s = "1234"
  # s = "123745"
  # s = "91011"
  # s = "891011"
  # s = "99100"
  s = "9899100"
  print(separateNumbers(s))

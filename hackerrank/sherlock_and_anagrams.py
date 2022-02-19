from collections import Counter

def all_substrs(s):
  return [[s[j:j+i] for j in range(len(s) - i + 1)] for i in range(1, len(s))]

def countem(ll):
  c = Counter()
  s = 0
  for lst in ll:
    for e in lst:
      q = ''.join(sorted(e))
      c[q] += 1
  print(c)
  # cdはcdが3つあるわけではなくcd,dc | cd, cd | dc,cdの３種類なので3???
  for e in c:
    # print(int(c[e]*(c[e]-1)/2))
    s += int(c[e]*(c[e]-1)/2)
  return s

def sherlockAndAnagrams(s):
  a = all_substrs(s)
  # for i in range(1, len(s)):
  #   print([[j,j+i] for j in range(len(s) - i + 1)])
  print(a)
  return countem(a)

if __name__ == '__main__':
  s = 'ifailuhkqq'
  s = 'cdcd'
  # s = 'abcd'
  # s = 'abba'
  print(sherlockAndAnagrams(s))




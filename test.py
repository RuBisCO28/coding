# def anagram(s):
#   l = len(s)
#   if l % 2 != 0:
#     return -1
#   else:
#     hf = int(l / 2)
#     first = s[:hf]
#     second = list(s[hf:])
#     cnt = 0
#     for i in range(hf):
#       if second.count(first[i]) > 0:
#         second.remove(first[i])
#       else:
#         cnt += 1
#     return cnt

from collections import Counter

def anagram(s):
  if len(s) % 2 != 0:
    return -1
  else:
    l = len(s)//2
    a = Counter(s[:l])
    b = Counter(s[l:])
    return l-sum((a & b).values())

if __name__ == '__main__':
  s = "aaab"
  s = "xyyx"
  s = "xaxbbbxx"
  print(anagram(s))

# time limit exceeded
# def weightedUniformStrings(s, queries):
#   alp = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,'m': 13,'n': 14,'o': 15,'p': 16,'q': 17,'r': 18,'s': 19,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26}
#   result = []
#   c = 0
#   for i in range(len(s)):
#     if i == 0:
#       prev = s[i]
#       c = 1
#     else:
#       if prev == s[i]:
#         c += 1
#       else:
#         prev = s[i]
#         c = 1
#     w = alp[s[i]] * c
#     result.append(w)
#     # print(i,s[i],w)
#   answer = ['Yes' if k in result else 'No' for k in queries]
#   return answer

def weightedUniformStrings(s, queries):
  weights = set()
  prev = -1
  length = 0
  for c in s:
      weight = ord(c) - ord('a') + 1
      weights.add(weight)
      if prev == c:
          length += 1
          weights.add(length*weight)
      else:
          prev = c
          length = 1

  rval = []
  for q in queries:
      if q in weights:
          rval.append("Yes")
      else:
          rval.append("No")
  return rval

def weightedUniformStrings(s, queries):
  result = set()
  c = 0
  for i in range(len(s)):
    if i == 0:
      prev = s[i]
      c = 1
    else:
      if prev == s[i]:
        c += 1
      else:
        prev = s[i]
        c = 1
    w = (ord(s[i])-ord('a')+1) * c
    result.add(w)
    # print(i,s[i],w)
  answer = ['Yes' if k in result else 'No' for k in queries]
  return answer

if __name__ == '__main__':
  s = 'abbcccdddd'
  queries = [1,7,5,4,15]
  print(weightedUniformStrings(s,queries))

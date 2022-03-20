# time limit exceeded
# def arrayManipulation(n, queries):
#   m = 4
#   d = {}
#   max_v = 0
#   for i in range(m):
#     for j in range((queries[i][0]-1),queries[i][1],1):
#       if j in d.keys():
#         d[j] += queries[i][2]
#       else:
#         d[j] = queries[i][2]
#       if max_v < d[j]:
#         max_v = d[j]
#     print(i,(queries[i][0]-1),queries[i][1]-1)
#   return max_v

from collections import Counter

def arrayManipulation(n, queries):
  c = Counter()
  for start,end,k in queries:
    c[start] += k
    c[end+1] -= k
  arrSum = 0
  maxSum = 0
  for i in sorted(c)[:-1]:
    arrSum += c[i]
    print(c,i,arrSum)
    maxSum = max(maxSum,arrSum)
  return maxSum

if __name__ == '__main__':
  n = 5
  queries = [[1,2,100],[2,5,100],[3,4,100]]
  # n = 10
  # queries = [[2,6,8],[3,5,7],[1,8,1],[5,9,15]]
  print(arrayManipulation(n, queries))

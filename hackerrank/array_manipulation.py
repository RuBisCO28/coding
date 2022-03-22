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

def arrayManipulation(n, queries):
  array = [0] * (n + 1)

  for query in queries:
    a = query[0] - 1
    b = query[1]
    k = query[2]
    array[a] += k
    array[b] -= k

  max_value = 0
  running_count = 0
  print(array)
  for i in array:
    running_count += i
    if running_count > max_value:
      max_value = running_count

  return max_value

if __name__ == '__main__':
  n = 5
  queries = [[1,2,100],[2,5,100],[3,4,100]]
  # n = 10
  # queries = [[2,6,8],[3,5,7],[1,8,1],[5,9,15]]
  print(arrayManipulation(n, queries))

# something wrong answer
# def prims(n, edges, start):
#   d = {}
#   v = {}
#   for i in range(len(edges)):
#     if edges[i][0] in d.keys():
#       if d[edges[i][0]] >= edges[i][2]:
#         d[edges[i][0]] = edges[i][2]
#         v[edges[i][0]] = edges[i][1]
#     else:
#       d[edges[i][0]] = edges[i][2]
#       v[edges[i][0]] = edges[i][1]
#     if edges[i][1] in d.keys():
#       if d[edges[i][1]] >= edges[i][2]:
#         d[edges[i][1]] = edges[i][2]
#         v[edges[i][1]] = edges[i][0]
#     else:
#       d[edges[i][1]] = edges[i][2]
#       v[edges[i][1]] = edges[i][0]
#   answer = 0
#   arr = [j+1 for j in range(n)]
#   for k in range(start,len(d)+1):
#     if len(arr) == 0:
#       break
#     if k in arr:
#       arr.remove(k)
#     if v[k] in arr:
#       arr.remove(v[k])
#     answer += d[k]
#   return answer

def prims(n, edges, start):
  vertices = {start}
  result = 0
  while len(vertices) < n:
    newEdges = [e for e in edges if ((e[0] in vertices and e[1] not in vertices) or (e[1] in vertices and e[0] not in vertices))]
    edge = min(newEdges, key = lambda e: e[2])
    vertices.update(edge[:2])
    result += edge[2]
  return result

if __name__ == '__main__':
  n = 5
  edges = [[1, 2, 3], [1, 3, 4], [4, 2, 6], [5, 2, 2], [2, 3, 5], [3, 5, 7]]
  start = 1
  n = 4
  edges = [[1,2,1],[3,2,150],[4,3,99],[1,4,100],[3,1,200]]
  start = 4
  print(prims(n, edges, start))

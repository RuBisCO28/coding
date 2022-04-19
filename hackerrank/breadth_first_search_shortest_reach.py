# something wrong
# def bfs(n, m, edges, s):
#   d = {}
#   for i in range(n):
#     d[i+1] = []
#   for j in range(len(edges)):
#     arr = []
#     if edges[j][0] in d.keys() and edges[j][1] in d.keys():
#       d[edges[j][0]].append(edges[j][1])
#       d[edges[j][1]].append(edges[j][0])
#       d[edges[j][0]] += d[edges[j][1]]
#       arr = list(set(d[edges[j][0]]))
#       for k in arr:
#         d[k] = arr
#     elif edges[j][0] in d.keys() and edges[j][1] not in d.keys():
#       d[edges[j][0]].append(edges[j][1])
#       for k in d[edges[j][0]]:
#         d[k] = d[edges[j][0]]
#     elif edges[j][0] not in d.keys() and edges[j][1] in d.keys():
#       d[edges[j][1]].append(edges[j][0])
#       for k in d[edges[j][1]]:
#         d[k] = d[edges[j][1]]
#   answer = []
#   print(d)
#   for l in d.keys():
#     if l != s:
#       if len(d[l]) > 0:
#         ln = len(d[l]) - 1
#         if s in d[l]:
#           ln -= 1
#         answer.append(ln*6)
#       else:
#         answer.append(-1)
#   return answer

from collections import deque

# something wrong
# おそらく最後の部分
# def bfs(n, m, edges, s):
#   graph = [[] for _ in range(n+1)]

#   for a,b in edges:
#     graph[a].append(b)
#     graph[b].append(a)

#   dist = [-1] * (n+1)
#   dist[0] = 0
#   dist[1] = 0

#   d = deque()
#   d.append(1)

#   while d:
#     v = d.popleft()
#     for i in graph[v]:
#       if dist[i] != -1:
#         continue
#       dist[i] = dist[v] + 1
#       d.append(i)
#   ans = []
#   for i in dist:
#     if i == -1:
#       ans.append(-1)
#     elif i > 0:
#       ans.append(i*6)
#   return ans

def bfs(n, m, edges, s):
  tree = {i:set() for i in range(1,n+1)}
  for l,m in edges: tree[l].add(m); tree[m].add(l)
  d,o,c = deque([(s,0)]),[s],{}
  while d:
    v,freq = d.popleft()
    for r in tree[v]:
      if r not in o:
        o.append(r)
        c[r] = freq + 6
        d.append((r,freq+6))
  return [c.get(ii,-1) for ii in range(1,n+1) if ii != s]

if __name__ == "__main__":
  n = 4
  m = 2
  edges = [[1,2],[1,3]]
  s = 1
  # n = 5
  # m = 3
  # edges = [[1,2],[1,3],[3,4]]
  # s = 1
  print(bfs(n, m, edges, s))


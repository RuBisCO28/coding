def bfs(n, m, edges, s):
  d = {}
  for i in range(n):
    d[i+1] = []
  for j in range(len(edges)):
    arr = []
    if edges[j][0] in d.keys() and edges[j][1] in d.keys():
      d[edges[j][0]].append(edges[j][1])
      d[edges[j][1]].append(edges[j][0])
      d[edges[j][0]] += d[edges[j][1]]
      arr = list(set(d[edges[j][0]]))
      for k in arr:
        d[k] = arr
    elif edges[j][0] in d.keys() and edges[j][1] not in d.keys():
      d[edges[j][0]].append(edges[j][1])
      for k in d[edges[j][0]]:
        d[k] = d[edges[j][0]]
    elif edges[j][0] not in d.keys() and edges[j][1] in d.keys():
      d[edges[j][1]].append(edges[j][0])
      for k in d[edges[j][1]]:
        d[k] = d[edges[j][1]]
  answer = []
  print(d)
  for l in d.keys():
    if l != s:
      if len(d[l]) > 0:
        ln = len(d[l]) - 1
        if s in d[l]:
          ln -= 1
        answer.append(ln*6)
      else:
        answer.append(-1)
  return answer

if __name__ == "__main__":
  # n = 4
  # m = 2
  # edges = [[1,2],[1,3]]
  # s = 1
  n = 5
  m = 3
  edges = [[1,2],[1,3],[3,4]]
  s = 1
  print(bfs(n, m, edges, s))


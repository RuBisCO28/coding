# time limit exceeded
# def componentsInGraph(gb):
#   d = {}
#   for i in range(len(gb)):
#     arr = []
#     if gb[i][0] in d.keys() and gb[i][1] in d.keys():
#       d[gb[i][0]].append(gb[i][1])
#       d[gb[i][1]].append(gb[i][0])
#       d[gb[i][0]] += d[gb[i][1]]
#       arr = list(set(d[gb[i][0]]))
#       for j in arr:
#         d[j] = arr
#     elif gb[i][0] in d.keys() and gb[i][1] not in d.keys():
#       d[gb[i][0]].append(gb[i][1])
#       for j in d[gb[i][0]]:
#         d[j] = d[gb[i][0]]
#     elif gb[i][0] not in d.keys() and gb[i][1] in d.keys():
#       d[gb[i][1]].append(gb[i][0])
#       for j in d[gb[i][1]]:
#         d[j] = d[gb[i][1]]
#     elif gb[i][0] not in d.keys() and gb[i][1] not in d.keys():
#       d.setdefault(gb[i][0], []).append(gb[i][0])
#       d.setdefault(gb[i][0], []).append(gb[i][1])
#       d.setdefault(gb[i][1], []).append(gb[i][0])
#       d.setdefault(gb[i][1], []).append(gb[i][1])
#   maxl = 0
#   minl = 999999999
#   for k in d.values():
#     if len(k) < minl:
#       minl = len(k)
#     if len(k) > maxl:
#       maxl = len(k)
#   return [minl,maxl]

# something wrong
# def componentsInGraph(gb):
#   d = {}
#   g = {}
#   i = 0
#   for a, b in gb:
#     if d.get(a, None) == None and d.get(b, None) == None:
#       g[i] = set({a, b})
#       d[a] = i
#       d[b] = i
#       i += 1
#     elif d.get(a, None) == None:
#       g[d[b]].update({a})
#       d[a] = d[b]
#     elif d.get(b, None) == None:
#       g[d[a]].update({b})
#       d[b] = d[a]
#     elif d[a] != d[b]:
#       if len(g[d[a]]) > len(g[d[b]]):
#         base = d[a]
#         add = d[b]
#       else:
#         base = d[b]
#         add = d[a]

#         g[base].update(g[add])
#         for item in g[add]:
#           d[item] = base
#         del(g[add])
#   lens = [len(g[item]) for item in g.keys()]
#   return [min(lens), max(lens)]

def generate_connected_groups(list_of_connected_nodes):
  node_connections = {}
  for connected_nodes in list_of_connected_nodes:
    node_A, node_B = connected_nodes
    if node_A not in node_connections:
        node_connections[node_A] = {node_A}
    if node_B not in node_connections:
        node_connections[node_B] = {node_B}
  for connected_nodes in list_of_connected_nodes:
    node_A, node_B = connected_nodes
    node_connections[node_A].add(node_B)
    node_connections[node_B].add(node_A)

  connected_groups_list = []
  visited = set()
  for node in node_connections:
    if node not in visited:
      visited.add(node)
      full_group = node_connections[node]
      queue = [node_connections[node]]
      while queue:
        current_set = queue.pop()
        for node in current_set:
          if node not in visited:
            visited.add(node)
            full_group.add(node)
            queue.append(node_connections[node])

      connected_groups_list.append(full_group)

  return connected_groups_list

def componentsInGraph(gb):
  connected_groups = generate_connected_groups(gb)
  connected_groups.sort(key=len)
  i = 0
  min = len(connected_groups[i])
  while min == 1:
    i += 1
    min = len(connected_groups[i])
  max = len(connected_groups[-1])

  return (min, max)

if __name__ == "__main__":
  gb = [[1, 6], [2, 7], [3, 8], [4, 9], [2, 6]]
  print(componentsInGraph(gb))


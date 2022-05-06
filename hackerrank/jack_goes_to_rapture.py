import heapq

def build_graph(g_nodes, g_from, g_to, g_weight):
  graph = [[] for _ in range(g_nodes+1)]

  for start, end, weight in zip(g_from, g_to, g_weight):
    graph[start].append((end, weight))
    graph[end].append((start, weight))

  return graph

def traverse_cost(current_cost, edge_weight):
  return max(current_cost, edge_weight)

def getCost(g_nodes, g_from, g_to, g_weight):
  graph = build_graph(g_nodes, g_from, g_to, g_weight)
  # print(graph)

  q = [(0, 1)] # start at node 1 with cost 0
  vis = [False] * (g_nodes+1)
  vis[1] = True # node 1 can be reached with no cost

  while q:
    cost, node = heapq.heappop(q)
    vis[node] = True

    if node == g_nodes: # The target node has been found, exit preliminary
      print(cost)
      return None

    for neighbor, weight in graph[node]:
      if vis[neighbor]: continue # ignore nodes that already have been explored
      heapq.heappush(q, (traverse_cost(cost, weight), neighbor))

  print("NO PATH EXISTS")
  return None

if __name__ == "__main__":
  g_nodes = 4
  g_from = [1,1,2,3]
  g_to = [2,3,4,4]
  g_weight = [20,5,30,40]
  print(getCost(g_nodes, g_from, g_to, g_weight))

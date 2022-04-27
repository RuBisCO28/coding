# something wrong
# from collections import defaultdict
# from math import factorial
# import math

# def journeyToMoon(n, astronaut):
#   d=defaultdict(int)
#   for i,j in astronaut:
#     d[i] += 1
#     d[j] += 1
#   total = math.floor(factorial(n) / factorial(2) / factorial(n - 2))
#   print(total)
#   print(d)
#   c = 0
#   o = 0
#   for k in d.values():
#     c += k
#     if k >= 2:
#       o += math.floor(factorial(k) / factorial(2) / factorial(k - 2))
#   return total - (c//2) - o

# something wrong
# from math import factorial
# import math

# def generate_connected_groups(list_of_connected_nodes):
#   node_connections = {}
#   for connected_nodes in list_of_connected_nodes:
#     node_A, node_B = connected_nodes
#     if node_A not in node_connections:
#         node_connections[node_A] = {node_A}
#     if node_B not in node_connections:
#         node_connections[node_B] = {node_B}
#   for connected_nodes in list_of_connected_nodes:
#     node_A, node_B = connected_nodes
#     node_connections[node_A].add(node_B)
#     node_connections[node_B].add(node_A)

#   connected_groups_list = []
#   visited = set()
#   for node in node_connections:
#     if node not in visited:
#       visited.add(node)
#       full_group = node_connections[node]
#       queue = [node_connections[node]]
#       while queue:
#         current_set = queue.pop()
#         for node in current_set:
#           if node not in visited:
#             visited.add(node)
#             full_group.add(node)
#             queue.append(node_connections[node])

#       connected_groups_list.append(full_group)

#   return connected_groups_list

# def journeyToMoon(n, astronaut):
#   connected_groups = generate_connected_groups(astronaut)
#   total = math.floor(factorial(n) / factorial(2) / factorial(n - 2))
#   for i in connected_groups:
#     k = len(i)
#     if k >= 2:
#       total -= math.floor(factorial(k) / factorial(2) / factorial(k - 2))
#   return total

# success but mysterious
# def journeyToMoon(n, astronaut):
#   dp = [[i] for i in range(n)]
#   for [x, y] in astronaut:
#     if dp[x] is dp[y]:
#       continue
#     [bigger, smaller] = [dp[x], dp[y]] if len(dp[x]) >= len(dp[y]) else [dp[y], dp[x]]
#     for k in smaller:
#       bigger.append(k)
#       dp[k] = bigger
#   dp = list({id(dp[i]): len(dp[i]) for i in range(n)}.values())
#   total = sum(dp)
#   result = 0
#   for i in dp:
#     total -= i
#     result += total * i
#   return result

def journeyToMoon(n, astronaut):
  cnn=[[] for i in range(n)]
  for [x,y] in astronaut:
    cnn[x].append(y)
    cnn[y].append(x)
  # print(cnn)

  # BFS to traverse, get the # of each group: group[]
  # where to change the vist? in case other branch expand the same points
  group=[]
  vist=[False for i in range(n)]
  for i in range(n):
    if not vist[i]: # not visited
      st=[i]
      # print(st)
      vist[i]=True
      s=1 # #of this group
      while len(st)>0:
        start=st.pop()
        # add all its neighbor
        for ngbr in cnn[start]:
          if not vist[ngbr]:
            vist[ngbr]=True
            st.append(ngbr)
            s += 1
        # print(st)
      group.append(s)
  # print(group)

  # choose from group A and other groups(by presum), and sum all possible group A
  # to avoid repeated, only jointed with the groups with index < index_A
  s = 0
  presum=[]
  for i in range(len(group)):
    s += group[i]
    presum.append(s)

  s = 0
  for i in reversed(range(1,len(group))):
    s += group[i]*presum[i-1]
  return s

# かぶらないようにしているなにかがわからん
if __name__ == "__main__":
  # n = 5
  # astronaut = [[0,1],[2,3],[0,4]]
  n = 10
  astronaut = [0,2],[1,8],[1,4],[2,8],[2,6],[3,5],[6,9]
  print(journeyToMoon(n, astronaut))

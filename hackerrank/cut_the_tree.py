# Time limit exceeded
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

# def cutTheTree(data, edges):
#   answer = 100000000000000000000000
#   arr = [i+1 for i in range(len(data))]
#   for i in range(len(edges)):
#     gb = edges[:i] + edges[i+1:]
#     connected_groups = generate_connected_groups(gb)
#     a = list(connected_groups[0])
#     b = list(set(arr) - set(a))
#     tmp = abs(sum([data[j-1] for j in a]) - sum([data[k-1] for k in b]))
#     if answer > tmp:
#       answer = tmp
#   return answer

# Something wrong
# def dfs(conn , node, sums, data, parent):
#   if sums[node]!=0:
#     return sums[node]
#   nb = conn[node]
#   if len(nb)==1 and node!=0:
#     sums[node] = data[node]
#     return data[node]
#   ans = 0
#   for n1 in nb:
#     if n1!=parent:
#       ans += dfs(conn, n1, sums, data, node)
#   ans += data[node]
#   sums[node] = ans
#   return ans

# def cutTheTree(data, edges):
#   n = len(data)
#   conn = [[] for i in range(n)]
#   for e in edges:
#     e1 = e[0]-1
#     e2 = e[1]-1
#     conn[e1].append(e2)
#     conn[e2].append(e1)
#   sums = [0 for i in range(n)]
#   dfs(conn , 0, sums, data, 0)
#   # print(sums)
#   mindiff = 999999999
#   for i in range(1, n):
#     ## separate node i
#     sum1 = sums[i]
#     sum2 = sums[0] - sums[i]
#     diff = abs(sum1 - sum2)
#     mindiff = min(mindiff, diff)
#   return mindiff

def cutTheTree(data, edges): # CORRECTION TO SETUP: data 0-indexed
  T, L, d, D = {a:set() for a in range(1,1+n)}, {1}, 0, [0]*(1+n)
  for a,b in edges : T[a].add(b) ; T[b].add(a) # start symmetric
  while L : # decycle graph T into a tree and calculate depths D
    L1 = set() # becomes all visited nodes at depth level d
    for a in L :
      D[a] = d ; L1 |= T[a]
      for b in T[a] : T[b].remove(a)
    d += 1 ; L = L1
  for a in sorted( range(1,1+n), key=lambda x:-D[x] ):#bottom up
    data[a-1] += sum( data[b-1] for b in T[a] ) #find subtotal
  return min( abs(data[0]-2*data[x]) for x in range(1,n) )

if __name__ == "__main__":
  data = [1,2,3,4,5,6]
  edges = [[1,2],[1,3],[2,6],[3,4],[3,5]]
  data = [100,200,100,500,100,600]
  edges = [[1,2],[2,3],[2,5],[4,5],[5,6]]
  print(cutTheTree(data, edges))

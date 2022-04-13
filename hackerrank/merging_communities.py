# something wrong
# if __name__ == '__main__':
#   nq = str(input()).split()
#   n = int(nq[0])
#   q = int(nq[1])
#   d = {}
#   for _ in range(q):
#     l = str(input()).split()
#     if l[0] == "M":
#       if l[1] in d.keys() and l[2] in d.keys():
#         d[l[1]].append(l[2])
#         for i in d[l[1]]:
#           d[str(i)] = d[l[1]]
#       elif l[1] in d.keys() and l[2] not in d.keys():
#         d[l[1]].append(l[2])
#         for i in d[l[1]]:
#           d[str(i)] = d[l[1]]
#       elif l[1] not in d.keys() and l[2] in d.keys():
#         d[l[2]].append(l[1])
#         for i in d[l[2]]:
#           d[str(i)] = d[l[2]]
#       elif l[1] not in d.keys() and l[2] not in d.keys():
#         d.setdefault(l[1], []).append(l[2])
#         d.setdefault(l[2], []).append(l[1])
#         d.setdefault(l[1], []).append(l[1])
#         d.setdefault(l[2], []).append(l[2])
#       #print(l[0], l[1], l[2], d)
#     else:
#       if l[1] not in d.keys():
#         d.setdefault(l[1], []).append(l[1])
#       print(len(d[l[1]]))
#       #print(l[0], l[1], d)

import sys

class disjoint_set:
    class Node:
        def __init__(self, data = 0):
            self.data = data
            self.parent = self
            self.rank = 0
            self.size = 1

    def __init__(self):
        self.items = dict()

    def make_set(self, data):
        if not data in self.items:
            self.items[data] = self.Node(data)
        return self.items

    def find_set(self, data):
        if data in self.items:
            node = self.items[data]
        else:
            return False

        if node.parent == node:
            return node
        node.parent = self.find_set(node.parent.data)

        return node.parent

    def union(self, rep1, rep2):
        node1 = self.find_set(rep1)
        node2 = self.find_set(rep2)

        #print("union: node1 = {} node2 = {}".format(node1.data, node2.data))

        if node1 and node2 and node1 != node2:
            if node1.rank >= node2.rank:
                if node1.rank == node2.rank:
                    node1.rank += 1
                node2.parent = node1
                node1.size += node2.size
            else:
                node1.parent = node2
                node2.size += node1.size

        return True
    
    def get_size(self, rep):
        return self.find_set(rep).size


if __name__ == "__main__":
    n, q = [int(x) for x in input().strip().split()]
    dset = disjoint_set()
    
    for ind in range(1, n+1):
        dset.make_set(ind)
    
    for _ in range(q):
        query = input().strip().split()
        
        if query[0] == 'M':
            rep1 = int(query[1])
            rep2 = int(query[2])
            dset.union(rep1, rep2)
        elif query[0] == 'Q':
            rep = int(query[1])
            print(dset.get_size(rep))
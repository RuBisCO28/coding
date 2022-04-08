# something wrong
# def find_min_path(st,ed,road_edges,road_from,road_to,road_weight,w):
#   for i in range(road_edges):
#     if st == road_from[i] and ed == road_to[i]:
#       w += road_weight[i]
#       return w
#     elif st == road_from[i]:
#       w += road_weight[i]
#       return find_min_path(road_to[i],ed,road_edges,road_from,road_to,road_weight,w)
#     else:
#       return -1

#!/bin/python3

# PyPy3

import math
import os
import random
import re
import sys

class Graph:
    def __init__(self, node_n):
        self.node_n = node_n
        self.matrix = [[float('inf')
                        for _ in range(node_n)]
                       for _ in range(node_n)
                       ]
        for k in range(node_n):
            for v in range(node_n):
                if k == v: self.matrix[k][v] = 0
    def add_edge(self, p, c, w):
        p=p-1;c=c-1
        self.matrix[p][c] = w
    def fw(self):
        for k in range(self.node_n):
            for i in range(self.node_n):
                for j in range(self.node_n):
                    if self.matrix[i][k] + self.matrix[k][j] < self.matrix[i][j]:
                        self.matrix[i][j] = self.matrix[i][k] + self.matrix[k][j]
    def get_graph(self):
        return self.matrix


if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().rstrip().split())

    # road_from = [0] * road_edges
    # road_to = [0] * road_edges
    # road_weight = [0] * road_edges

    # for i in range(road_edges):
    #     road_from[i], road_to[i], road_weight[i] = map(int, input().rstrip().split())

    graph=Graph(road_nodes)
    for i in range(road_edges):
        p,c,w=list(map(int, input().split()))
        graph.add_edge(p=p,c=c,w=w)
    graph.fw()
    get_map = graph.get_graph()
    cost=[]

    q = int(input().strip())

    cost = []
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        x = int(first_multiple_input[0])

        y = int(first_multiple_input[1])

        cost.append(-1  if get_map[x-1][y-1]==float('inf') else get_map[x-1][y-1])
    [print(y) for y in cost]

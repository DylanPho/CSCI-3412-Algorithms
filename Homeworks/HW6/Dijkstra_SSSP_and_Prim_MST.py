'''
Name: Dylan Phoutthavong
Date: May 4th, 2025
Course: CSCI 3412
Task(s): 2. (7 points) Run Dijsktra's SSSP algorithm from Q1 to find the shortest distance from the starting city (e.g. Denver) to all other cities in the output format specified below.
         3. (8 points) Run either Prim's or Kruskal's (not both) MST algorithm to find the Minimum Spanning Tree from the starting city (e.g. Denver) to all other cities in the format specified below
'''

import sys
from collections import defaultdict

# #########################
#  Graph class
# #########################
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)  # undirected edge for MST
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

    def initializeDistances(self):
        for i in self.nodes:
            for j in self.nodes:
                self.distances[(i, j)] = sys.maxsize
        for i in self.nodes:
            self.distances[(i, "")] = 0


# #########################
#  Dijkstra's SSSP
# #########################
def dijkstra_city_distance(graph, s):
    visited = {s: 0}
    path = dict.fromkeys(graph.nodes, "")
    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None or visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for v in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, v)]
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                path[v] = min_node

    for city in sorted(graph.nodes):
        if city in visited:
            pathStr = city
            currentCity = city
            while path[currentCity] != "":
                pathStr = path[currentCity] + " to " + pathStr
                currentCity = path[currentCity]
            print(f"Distance from {s} to '{city}': {visited[city]} with path({pathStr})")


# #########################
#  MST using Prim's Algorithm
# #########################
def minKey(g, key, mstSet):
    min_val = sys.maxsize
    min_index = None
    for node in g.nodes:
        if node not in mstSet and key[node] < min_val:
            min_val = key[node]
            min_index = node
    if min_index is not None:
        print(min_index, "is selected. Distance:", min_val)
    return min_index

def printMST(parent, g):
    print("\n\t\tEdge \t\t\t\tWeight\n")
    total = 0
    for i in parent.keys():
        if parent[i] != "":
            total += g.distances[(i, parent[i])]
            print(f"{parent[i]:>15} {i:>15} {g.distances[(i, parent[i])]:.>20d}")
    print("\nTotal MST: ", "\t", total)

def primMST(graph, start):
    key = {node: sys.maxsize for node in graph.nodes}
    parent = {node: "" for node in graph.nodes}
    mstSet = set()

    key[start] = 0

    for _ in range(len(graph.nodes)):
        u = minKey(graph, key, mstSet)
        if u is None:
            break
        mstSet.add(u)

        for v in graph.edges[u]:
            if v not in mstSet and graph.distances[(u, v)] < key[v]:
                key[v] = graph.distances[(u, v)]
                parent[v] = u

    printMST(parent, graph)


# #########################
#  Main Function
# #########################
if __name__ == "__main__":
    g = Graph()
    cities = ['Atlanta', 'Boston', 'Chicago', 'Dallas', 'Denver', 'Houston', 'LA', 'Memphis',
              'Miami', 'NY', 'Philadelphia', 'Phoenix', 'SF', 'Seattle', 'Washington']

    for city in cities:
        g.add_node(city)

    g.add_edge('Seattle', 'SF', 1092)
    g.add_edge('Seattle', 'LA', 1544)
    g.add_edge('LA', 'SF', 559)
    g.add_edge('LA', 'Houston', 2205)
    g.add_edge('LA', 'Denver', 1335)
    g.add_edge('LA', 'NY', 3933)
    g.add_edge('LA', 'Miami', 3755)
    g.add_edge('Denver', 'Dallas', 1064)
    g.add_edge('Denver', 'Boston', 2839)
    g.add_edge('Denver', 'Memphis', 1411)
    g.add_edge('Denver', 'Chicago', 1474)
    g.add_edge('Chicago', 'Boston', 1367)
    g.add_edge('Chicago', 'NY', 1145)
    g.add_edge('Boston', 'NY', 306)
    g.add_edge('Boston', 'Atlanta', 1505)
    g.add_edge('Atlanta', 'Dallas', 1157)
    g.add_edge('Dallas', 'Houston', 362)
    g.add_edge('Atlanta', 'Miami', 973)
    g.add_edge('Atlanta', 'SF', 3434)
    g.add_edge('Dallas', 'Memphis', 675)
    g.add_edge('Memphis', 'Philadelphia', 1413)
    g.add_edge('Miami', 'Phoenix', 3182)
    g.add_edge('Miami', 'Washington', 1487)
    g.add_edge('Phoenix', 'NY', 3441)
    g.add_edge('Phoenix', 'Chicago', 2332)
    g.add_edge('Phoenix', 'Dallas', 1422)
    g.add_edge('Philadelphia', 'Washington', 199)
    g.add_edge('Philadelphia', 'Phoenix', 3342)
    g.add_edge('Washington', 'Dallas', 1900)
    g.add_edge('Washington', 'Denver', 2395)

    print("\nDijkstra Output:\n")
    dijkstra_city_distance(g, 'Denver')

    print("\nPrim's MST Output:\n")
    primMST(g, 'Denver')
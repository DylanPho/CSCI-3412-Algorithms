'''
Name: Dylan Phoutthavong
Date: May 4th, 2025
Course: CSCI 3412
Task(s): - Read and learn how Dijkstra's SSSP algorithm works 
         - Implement the algorithm in Python including your test driver to prove your implementation
                - You can use any 8 - 10 vertexes graph for testing or
                - You may start from the sample graph in slide 16-ish of Module 17
'''

import sys
from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)       # adjacency list: from_node -> [to_node, ...]
        self.distances = {}                  # edge weights: keys are (from_node, to_node)

    def add_node(self, value):
        """Add a single node to the graph."""
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        """Add a directed edge with a weight to the graph."""
        self.nodes.add(from_node)
        self.nodes.add(to_node)
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

    def dijkstra(self, start):
        """Perform Dijkstra's algorithm from the start node and print the relaxation process."""
        dist = {node: float('inf') for node in self.nodes}
        dist[start] = 0
        prev = {node: None for node in self.nodes}
        visited = set()
        nodes_to_visit = set(self.nodes)

        if start not in nodes_to_visit:
            print("Start node not in graph")
            return

        while nodes_to_visit:
            # Select the unvisited node with the smallest distance
            current_node = None
            current_min_dist = float('inf')
            for node in nodes_to_visit:
                if dist[node] < current_min_dist:
                    current_min_dist = dist[node]
                    current_node = node
            if current_node is None:
                break

            # Show the node being added to visited set before relaxing
            visited_str = "{" + ", ".join(f"'{v}'" for v in sorted(visited | {current_node})) + "}"
            print(f"Node({current_node} with Weight {dist[current_node]}) is added to the 'Visited' {visited_str} # selected")
            nodes_to_visit.remove(current_node)
            visited.add(current_node)

            neighbors = self.edges.get(current_node, [])
            if not neighbors:
                print(f"No unvisited outgoing edges from the node, {current_node}")
            else:
                any_relaxed = False
                for neighbor in neighbors:
                    if neighbor in visited:
                        continue
                    old_distance = dist[neighbor]
                    new_distance = dist[current_node] + self.distances[(current_node, neighbor)]
                    if new_distance < old_distance:
                        dist[neighbor] = new_distance
                        prev[neighbor] = current_node
                        any_relaxed = True
                        old_dist_str = "Infinity" if old_distance == float('inf') else str(old_distance)
                        print(f"Relaxed: vertex {neighbor}: OLD: {old_dist_str}, NEW: {new_distance}, Paths: {{'{neighbor}': '{current_node}'}}")
                if not any_relaxed:
                    print(f"No edge relaxation is needed for node, {current_node}")

        # Final output
        print("\nFinal shortest distances from source node:")
        for node in sorted(self.nodes):
            dist_val = dist[node]
            if dist_val == float('inf'):
                print(f"{node}: Infinity")
            else:
                print(f"{node}: {dist_val}")


# Sample usage: build a graph and run Dijkstra's algorithm
g = Graph()
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('C', 'B', 10)
g.add_edge('B', 'D', 5)
g.add_edge('B', 'E', 3)
g.add_edge('C', 'F', 4)
g.add_edge('E', 'G', 2)
g.add_edge('F', 'H', 1)
g.add_edge('A', 'E', 7)
g.add_edge('G', 'H', 5)

# Run the algorithm from node 'A'
g.dijkstra('A')
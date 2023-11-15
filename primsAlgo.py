import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        self.graph.setdefault(u, []).append((v, weight))
        self.graph.setdefault(v, []).append((u, weight))

def prim(graph, start):
    visited = set()
    mst = []
    priority_queue = [(0, start)]

    while priority_queue:
        current_weight, current_vertex = heapq.heappop(priority_queue)

        if current_vertex not in visited:
            visited.add(current_vertex)
            mst.append((current_vertex, current_weight))

            for neighbor, weight in graph.graph[current_vertex]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (weight, neighbor))

    return mst

# Example usage for Prim's Algorithm:
my_graph_prim = Graph()
my_graph_prim.add_edge('A', 'B', 2)
my_graph_prim.add_edge('A', 'C', 1)
my_graph_prim.add_edge('B', 'C', 3)
my_graph_prim.add_edge('B', 'D', 4)
my_graph_prim.add_edge('C', 'D', 5)

minimum_spanning_tree_prim = prim(my_graph_prim, 'A')
print("Minimum Spanning Tree (Prim's Algorithm):", minimum_spanning_tree_prim)

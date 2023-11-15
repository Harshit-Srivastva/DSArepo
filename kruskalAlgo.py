class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

def kruskal(graph):
    # Step 1: Sort edges by weight
    graph.edges = sorted(graph.edges, key=lambda edge: edge[2])

    parent = {vertex: vertex for vertex in graph.vertices}
    mst = []

    def find_set(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find_set(parent[vertex])
        return parent[vertex]

    def union(u, v):
        parent_u = find_set(u)
        parent_v = find_set(v)
        parent[parent_u] = parent_v

    for edge in graph.edges:
        u, v, weight = edge
        if find_set(u) != find_set(v):
            mst.append((u, v, weight))
            union(u, v)

    return mst

# Example usage:
vertices = ['A', 'B', 'C', 'D']
my_graph = Graph(vertices)
my_graph.add_edge('A', 'B', 2)
my_graph.add_edge('A', 'C', 1)
my_graph.add_edge('B', 'C', 3)
my_graph.add_edge('B', 'D', 4)
my_graph.add_edge('C', 'D', 5)

minimum_spanning_tree = kruskal(my_graph)

print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} -- {edge[1]} : {edge[2]}")

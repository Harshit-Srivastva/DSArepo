class Graph:
    def __init__(self):
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append((u, v, weight))

def bellman_ford(graph, start):
    # Step 1: Initialize distances
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Step 2: Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for u, v, weight in graph:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Step 3: Check for negative cycles
    for u, v, weight in graph:
        if distances[u] + weight < distances[v]:
            print("Graph contains a negative cycle. Bellman-Ford not applicable.")
            return

    return distances

# Example usage:
my_graph = Graph()
my_graph.add_edge('A', 'B', 1)
my_graph.add_edge('A', 'C', -2)
my_graph.add_edge('B', 'D', 4)
my_graph.add_edge('C', 'D', 5)
my_graph.add_edge('D', 'A', -1)

start_node = 'A'
shortest_distances = bellman_ford(my_graph.graph, start_node)

print(f"Shortest distances from {start_node}: {shortest_distances}")

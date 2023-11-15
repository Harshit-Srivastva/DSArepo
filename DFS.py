class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def dfs(graph, start, visited):
    if start not in visited:
        print(start, end=" ")  # Process the current node
        visited.add(start)

        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

# Example usage:
my_graph = Graph()
my_graph.add_edge('A', ['B', 'C'])
my_graph.add_edge('B', ['A', 'D'])
my_graph.add_edge('C', ['A', 'D'])
my_graph.add_edge('D', ['B', 'C'])

print("DFS starting from node 'A':")
dfs(my_graph.graph, 'A', set())

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            print(current_node, end=" ")  # Process the current node
            visited.add(current_node)
            queue.extend(graph[current_node])

# Example usage:
my_graph = Graph()
my_graph.add_edge('A', ['B', 'C'])
my_graph.add_edge('B', ['A', 'D'])
my_graph.add_edge('C', ['A', 'D'])
my_graph.add_edge('D', ['B', 'C'])

print("BFS starting from node 'A':")
bfs(my_graph.graph, 'A')

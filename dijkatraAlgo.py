import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage:
my_graph = Graph()
my_graph.add_edge('A', {'B': 1, 'C': 3})
my_graph.add_edge('B', {'A': 1, 'D': 2})
my_graph.add_edge('C', {'A': 3, 'D': 5})
my_graph.add_edge('D', {'B': 2, 'C': 5})

start_node = 'A'
shortest_distances = dijkstra(my_graph.graph, start_node)

print(f"Shortest distances from {start_node}: {shortest_distances}")

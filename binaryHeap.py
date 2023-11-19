import heapq

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def extract_min(self):
        return heapq.heappop(self.heap)

# Example usage:
binary_heap = BinaryHeap()
elements = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
for element in elements:
    binary_heap.insert(element)

print("Binary Heap:")
while binary_heap.heap:
    print(binary_heap.extract_min(), end=" ")
print()

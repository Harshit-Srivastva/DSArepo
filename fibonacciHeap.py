class FibonacciHeapNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.marked = False
        self.child = None
        self.parent = None
        self.left = self
        self.right = self

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.nodes = []

    def insert(self, key):
        new_node = FibonacciHeapNode(key)
        if self.min_node is None:
            self.min_node = new_node
        else:
            self._link(self.min_node, new_node)
            if key < self.min_node.key:
                self.min_node = new_node
        self.nodes.append(new_node)

    def extract_min(self):
        min_node = self.min_node
        if min_node:
            if min_node.child:
                child = min_node.child
                while True:
                    next_child = child.right
                    child.parent = None
                    if next_child == min_node.child:
                        break
                    child = next_child

            self._remove_from_list(min_node)
            if min_node == min_node.right:
                self.min_node = None
            else:
                self.min_node = min_node.right
                self._consolidate()

        return min_node.key if min_node else None

    def _link(self, node1, node2):
        node2.left.right = node2.right
        node2.right.left = node2.left
        node2.left = node2
        node2.right = node2
        node1.child = self._merge_lists(node1.child, node2)
        node2.parent = node1
        node1.degree += 1
        node2.marked = False

    def _consolidate(self):
        max_degree = int(self._log_base_phi(len(self.nodes))) + 1
        degree_array = [None] * max_degree

        current = self.min_node
        remaining_nodes = set(self.nodes)
        while current in remaining_nodes:
            next_node = current.right
            current_degree = current.degree

            while degree_array[current_degree]:
                other = degree_array[current_degree]
                if current.key > other.key:
                    current, other = other, current
                self._link(current, other)
                degree_array[current_degree] = None
                current_degree += 1

            degree_array[current_degree] = current
            current = next_node

        self.min_node = None
        for node in degree_array:
            if node:
                if not self.min_node or node.key < self.min_node.key:
                    self.min_node = node

    def _remove_from_list(self, node):
        node.left.right = node.right
        node.right.left = node.left
        node.left = node
        node.right = node

    def _merge_lists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        list1_right = list1.right
        list2_left = list2.left

        list1.right = list2
        list2.left = list1

        list1_right.left = list2_left
        list2_left.right = list1_right

        return list1

    def _log_base_phi(self, n):
        # Logarithm to the base phi (golden ratio)
        phi = (1 + 5**0.5) / 2
        return int(round((n - 1) / phi))

# Example usage:
fibonacci_heap = FibonacciHeap()
for element in elements:
    fibonacci_heap.insert(element)

print("\nFibonacci Heap:")
while True:
    min_key = fibonacci_heap.extract_min()
    if min_key is None:
        break
    print(min_key, end=" ")
print()

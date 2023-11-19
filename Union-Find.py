class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, element):
        if self.parent[element] != element:
            # Path compression
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)

        # Union by rank
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1

# Example usage:
size = 5
uf = UnionFind(size)

# Initially, each element is its own set
print("Initial sets:", [uf.find(i) for i in range(size)])

# Union operations
uf.union(0, 1)
uf.union(2, 3)
uf.union(0, 2)

# Find operations
print("\nRepresentative after union operations:")
for i in range(size):
    print(f"Element {i} belongs to set: {uf.find(i)}")

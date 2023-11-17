class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        # A simple hash function to convert the key into an index
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            # Handle collisions using chaining (each index in the table is a list of key-value pairs)
            for i, (existing_key, existing_value) in enumerate(self.table[index]):
                if key == existing_key:
                    # If the key already exists, update its value
                    self.table[index][i] = (key, value)
                    break
            else:
                # If the key is not found in the list, add a new key-value pair
                self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for existing_key, existing_value in self.table[index]:
                if key == existing_key:
                    return existing_value
        return None

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i, (existing_key, existing_value) in enumerate(self.table[index]):
                if key == existing_key:
                    # If the key is found, delete the key-value pair
                    del self.table[index][i]
                    break

    def display(self):
        for i in range(self.size):
            print(f'Index {i}: {self.table[i]}')

# Example usage:
hash_table = HashTable(size=10)
hash_table.insert("apple", 5)
hash_table.insert("banana", 8)
hash_table.insert("orange", 3)

print("Hash Table:")
hash_table.display()

print("\nSearch for 'banana':", hash_table.search("banana"))
print("Search for 'grape':", hash_table.search("grape"))

hash_table.delete("apple")

print("\nAfter deleting 'apple':")
hash_table.display()

class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            # Handle collisions using chaining
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


class HashTableOpenAddressing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.table[index] is not None:
            # Handle collisions using linear probing (open addressing)
            index = (index + 1) % self.size

        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        initial_index = index

        while self.table[index] is not None:
            existing_key, existing_value = self.table[index]
            if key == existing_key:
                return existing_value
            index = (index + 1) % self.size

            # If we have checked all slots and haven't found the key, stop searching
            if index == initial_index:
                break

        return None

    def delete(self, key):
        index = self.hash_function(key)
        initial_index = index

        while self.table[index] is not None:
            existing_key, existing_value = self.table[index]
            if key == existing_key:
                # If the key is found, delete the key-value pair
                self.table[index] = None
                break
            index = (index + 1) % self.size

            # If we have checked all slots and haven't found the key, stop searching
            if index == initial_index:
                break

    def display(self):
        for i in range(self.size):
            print(f'Index {i}: {self.table[i]}')


# Example usage with chaining
print("Chaining Example:")
hash_table_chaining = HashTableChaining(size=10)
hash_table_chaining.insert("apple", 5)
hash_table_chaining.insert("banana", 8)
hash_table_chaining.insert("orange", 3)

hash_table_chaining.display()

print("\nSearch for 'banana':", hash_table_chaining.search("banana"))
print("Search for 'grape':", hash_table_chaining.search("grape"))

hash_table_chaining.delete("apple")

print("\nAfter deleting 'apple':")
hash_table_chaining.display()


# Example usage with open addressing (linear probing)
print("\nOpen Addressing Example:")
hash_table_open_addressing = HashTableOpenAddressing(size=10)
hash_table_open_addressing.insert("apple", 5)
hash_table_open_addressing.insert("banana", 8)
hash_table_open_addressing.insert("orange", 3)

hash_table_open_addressing.display()

print("\nSearch for 'banana':", hash_table_open_addressing.search("banana"))
print("Search for 'grape':", hash_table_open_addressing.search("grape"))

hash_table_open_addressing.delete("apple")

print("\nAfter deleting 'apple':")
hash_table_open_addressing.display()

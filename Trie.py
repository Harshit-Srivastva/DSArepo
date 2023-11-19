class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage:
trie = Trie()
words = ["apple", "app", "apricot", "banana", "bat", "batman"]

# Insert words into the trie
for word in words:
    trie.insert(word)

# Search for words in the trie
print("Search results:")
print("Search for 'apple':", trie.search("apple"))  # True
print("Search for 'app':", trie.search("app"))      # True
print("Search for 'apricot':", trie.search("apricot"))  # True
print("Search for 'ap':", trie.search("ap"))        # False
print("Search for 'banana':", trie.search("banana"))  # True
print("Search for 'bat':", trie.search("bat"))      # True
print("Search for 'batman':", trie.search("batman"))  # False

# Check if a prefix exists in the trie
print("\nPrefix check:")
print("Starts with prefix 'app':", trie.starts_with_prefix("app"))  # True
print("Starts with prefix 'ban':", trie.starts_with_prefix("ban"))  # True
print("Starts with prefix 'cat':", trie.starts_with_prefix("cat"))  # False

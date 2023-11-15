import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def build_frequency_table(data):
    freq_table = defaultdict(int)
    for char in data:
        freq_table[char] += 1
    return freq_table

def build_huffman_tree(freq_table):
    priority_queue = [HuffmanNode(char, freq) for char, freq in freq_table.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged_node = HuffmanNode(None, left.freq + right.freq)
        merged_node.left = left
        merged_node.right = right
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def build_huffman_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}

    if root is not None:
        if root.char is not None:
            codes[root.char] = current_code
        build_huffman_codes(root.left, current_code + "0", codes)
        build_huffman_codes(root.right, current_code + "1", codes)

    return codes

def huffman_compress(data):
    freq_table = build_frequency_table(data)
    huffman_tree = build_huffman_tree(freq_table)
    huffman_codes = build_huffman_codes(huffman_tree)
    
    compressed_data = ''.join(huffman_codes[char] for char in data)
    
    return compressed_data, huffman_tree

# Example usage:
data = "abracadabra"
compressed_data, huffman_tree = huffman_compress(data)
print("Original Data:", data)
print("Compressed Data:", compressed_data)

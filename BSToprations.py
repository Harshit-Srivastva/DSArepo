class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)

        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor (smallest
            # in the right subtree)
            root.key = self._min_value_node(root.right).key

            # Delete the inorder successor
            root.right = self._delete(root.right, root.key)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.key)
            self._inorder_traversal(root.right, result)

# Example usage:
bst = BinarySearchTree()

# Insert values into the BST
values_to_insert = [50, 30, 20, 40, 70, 60, 80]
for value in values_to_insert:
    bst.insert(value)

# Inorder traversal
print("Inorder Traversal:", bst.inorder_traversal())

# Search for a value
search_value = 40
search_result = bst.search(search_value)
if search_result:
    print(f"Node with key {search_value} found in the BST.")
else:
    print(f"Node with key {search_value} not found in the BST.")

# Delete a value
delete_value = 30
bst.delete(delete_value)
print(f"Deleted node with key {delete_value}.")

# Inorder traversal after deletion
print("Inorder Traversal after deletion:", bst.inorder_traversal())

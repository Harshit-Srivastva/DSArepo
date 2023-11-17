class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node:
        # Traverse the left subtree
        inorder_traversal(node.left)
        # Process the current node
        print(node.value, end=" ")
        # Traverse the right subtree
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node:
        # Process the current node
        print(node.value, end=" ")
        # Traverse the left subtree
        preorder_traversal(node.left)
        # Traverse the right subtree
        preorder_traversal(node.right)

def postorder_traversal(node):
    if node:
        # Traverse the left subtree
        postorder_traversal(node.left)
        # Traverse the right subtree
        postorder_traversal(node.right)
        # Process the current node
        print(node.value, end=" ")

# Example usage:
# Constructing a simple binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder Traversal:")
inorder_traversal(root)

print("\nPreorder Traversal:")
preorder_traversal(root)

print("\nPostorder Traversal:")
postorder_traversal(root)

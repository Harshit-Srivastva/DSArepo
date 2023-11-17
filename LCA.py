class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_lowest_common_ancestor(root, node1, node2):
    if root is None:
        return None

    # If either node1 or node2 is the root, then root is the LCA
    if root.value == node1 or root.value == node2:
        return root

    # Recursively find the LCA in the left and right subtrees
    left_lca = find_lowest_common_ancestor(root.left, node1, node2)
    right_lca = find_lowest_common_ancestor(root.right, node1, node2)

    # If both left_lca and right_lca are not None, then root is the LCA
    if left_lca and right_lca:
        return root

    # If either left_lca or right_lca is not None, return the non-None value
    return left_lca if left_lca else right_lca

# Example usage:
# Constructing a simple binary tree
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

node1_value = 5
node2_value = 1

# Find the Lowest Common Ancestor
lca_node = find_lowest_common_ancestor(root, node1_value, node2_value)

# Display the result
if lca_node:
    print(f"The Lowest Common Ancestor of nodes {node1_value} and {node2_value} is: {lca_node.value}")
else:
    print(f"One or both of the nodes {node1_value} and {node2_value} not found in the tree.")

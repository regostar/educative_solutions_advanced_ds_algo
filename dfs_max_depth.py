class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    # Base case: if the tree is empty, the depth is 0
    if not root:
        return 0

    # Recursively find the depth of the left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # The maximum depth is the greater of the two depths, plus 1 for the current node
    return max(left_depth, right_depth) + 1

# Example usage:
# Constructing a binary tree:
#        3
#       / \
#      9   20
#         /  \
#        15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print(max_depth(root))  # Output: 3
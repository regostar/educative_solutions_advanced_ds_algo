"""
Find the sum of all elements in a binary tree that fall within the range [low, high], where 'low' and 'high' are integers.

""" 
from typing import List

class TreeNode:
    def __init__(self, val=None, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def dfs(root: TreeNode, low: int, high: int)->int:
    """
    find sum of nodes in ranghe
    """
    total = 0
    
    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        if node.val >= low and node.val <= high:
            total += node.val
        if node.right is not None:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return total

def recursive_dfs(root: TreeNode, low: int, high: int)->int:
    """
    """
    if not root:
        return 0
    if root.val >= low and root.val <= high:
        # in range, compute sum and return
        return root.val + recursive_dfs(root.left, low, high) + recursive_dfs(root.right, low, high)

    else:
        return recursive_dfs(root.left, low, high) + recursive_dfs(root.right, low, high)


# Constructing a binary tree:
#        10
#       /  \
#      5    15
#     / \     \
#    3   7     18
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

# Find the sum of nodes in the range [7, 15]
print("Iterative")
print(dfs(root, 7, 15))  # Output: 32 (7 + 10 + 15)

print("recursive ")
print(recursive_dfs(root, 7, 15))

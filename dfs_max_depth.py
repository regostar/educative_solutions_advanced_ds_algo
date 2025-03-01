"""
The Max Depth of Binary Tree

"""


from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_max_depth(root)-> int:
    """
    """
    # use recursion
    # can change to stack later if needed


    def dfs(node)->int:
        if not node:
            return 0
        print("came to ", node.val)

        left = dfs(node.left)
        right = dfs(node.right)

        return max(left, right) + 1

    return dfs(root)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print(find_max_depth(root))  # Output: 3
             
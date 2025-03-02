"""
Vierify BST 

"""

from typing import List
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def verify_bst(root)-> int:
    """
    tO CHECK IF bINARY TRee is BST
    we keep , min_limit,  max_limit
    root ->  , -Inf , +Inf
    dfs(root.left,  -Inf, root.val)
    dfs(root.right, root.val, Inf )


    right 
    dfs(r.left,  max(-Inf, prent.val, r.val)
    dfs(r.right, root.val, Inf )

    
    """
    # use recursion
    # can change to stack later if needed


    def dfs(node, min_limit, max_limit)->bool:
        if not node:
            return True
        
        if node.val < min_limit or node.val > max_limit:
            return False
        
        # print("came to ", node.val, " max =", max_seen, " count = ", count_visible)

        return dfs(node.left, min_limit=min_limit, max_limit = min(node.val, max_limit)) and  dfs(node.right, min_limit=max(node.val, min_limit), max_limit=max_limit)

    return dfs(root, -math.inf, math.inf)


# False
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20, TreeNode(15), TreeNode(7))

# False
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20, TreeNode(15), TreeNode(7))


root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(20, TreeNode(15), TreeNode(70))

# root = TreeNode(5)
# root.left = TreeNode(4, TreeNode(3), TreeNode(8))
# root.right = TreeNode(6)

print(verify_bst(root))  # Output: 3
             
        #      3
        #     / \
        #    9  20
        #      /  \
        #     15   7


#      5
#     / \
#    4   6
#   / \  /\
#  3   8



"""
LCA

"""

from typing import List
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def find_lca(root, p, q):
    """
    given 2 nodes
    root will always be an ancestor

    if none, return none
    
    if n1 == node or n2 == node -> we found the lca 

    do dfs left 
    dfs right 

    if left and right 
    -> root 

    else return left or right 
    # found in one subtree

    """
    # use recursion
    # can change to stack later if needed


    def dfs(node, p, q):
        if not node:
            return None
        
        if node == p or node == q:
            return node
        
        left = dfs(node.left, p, q)

        right = dfs(node.right, p, q)

        if left and right:
            # curr node is 
            return node
        
        return left or right
        

    return dfs(root, p, q)
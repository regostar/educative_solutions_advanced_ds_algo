"""
In a binary tree, a node is considered “visible” if no node on the root-to-itself path
 has a greater value. The root is always “visible” since there are no other nodes between 
 the root and itself. Given a binary tree, count the number of “visible” nodes.
"""

from typing import List
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def find_visible_nodes(root)-> int:
    """
    Given binary tree
    Count no of visible nodes
    Visible - no nodes bigger than itself from root to itself
    We keep state
    Count increases if we encounter
    DFS - from root to node, we keep track of max seen so far
    if cur val > max seen so far 
    then count ++
    max seen so far updated

    """
    # use recursion
    # can change to stack later if needed
    count_visible = 0

    def dfs(node, max_seen):
        nonlocal count_visible
        if not node:
            return
        print("came to ", node.val)

        if node.val > max_seen:
            count_visible += 1
            max_seen = node.val

        dfs(node.left, max_seen)
        dfs(node.right, max_seen)

    dfs(root, -math.inf)

    return count_visible


def find_visible_nodes_v2(root)-> int:
    """
    Given binary tree
    Count no of visible nodes
    Visible - no nodes bigger than itself from root to itself
    We keep state
    Count increases if we encounter
    DFS - from root to node, we keep track of max seen so far
    if cur val > max seen so far 
    then count ++
    max seen so far updated

    """
    # use recursion
    # can change to stack later if needed


    def dfs(node, max_seen)->int:
        if not node:
            return 0
        
        count_visible = 0

        if node.val >= max_seen:
            count_visible += 1
        
        # print("came to ", node.val, " max =", max_seen, " count = ", count_visible)

        count_visible += dfs(node.left, max(max_seen, node.val))
        count_visible += dfs(node.right, max(max_seen, node.val))

        return count_visible

    return dfs(root, -math.inf)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print(find_visible_nodes(root))  # Output: 3
             
        #      3
        #     / \
        #    9  20
        #      /  \
        #     15   7


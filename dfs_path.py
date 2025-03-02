"""
Ternary tree paths #
Given a ternary tree (each node of the tree has at most three children), find all root-to-leaf paths.

"""

from typing import List
import math

class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children



def ternery_tree_paths(root):
    """
    Perform DFS 
    record path and pass it as state to children
    when we reach end, print or add to result

    """
    result = []
    def dfs(node, path):
        # idf all children is none 
        if all(c is None for c in node.children):
            result.append('->'.join(path) + '->' + node.val)
            return

        # print(path)
        for child in node.children:
            if child is not None:
                dfs(child, path + [node.val])
    
    dfs(root, [])
    return result

class Node: 
    def __init__(self, val, children=[]): 
        self.val = val 
        self.children = children 

def build_tree(nodes): 
    val = next(nodes) 
    if not val or val == 'x': return 
    cur = Node(val, []) 
    for _ in range(3): cur.children.append(build_tree(nodes)) 
    return cur 

inputs = ["1 2 5 x x x x x 3 x x x 4 x x x", "1 2 3 x x x 4 x x x 7 x x x 5 x x x 6 x x x"]

for i in range(len(inputs)): 
    root = build_tree(iter(inputs[i].split())) 
    # print(root.children[0].val)
    print("Ternary tree path", ternery_tree_paths(root))
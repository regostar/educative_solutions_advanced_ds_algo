"""
BFS OF Graph

""" 
from typing import List


from collections import deque

# def bfs_queue(root):
#     queue = deque([root])
#     while len(queue):
#         node = queue.pop()
#         for child in node.children:
#             if OK(child):
#                 return FOUND(child)
#             queue.append(child)
#     return notfoun


"""
Binary tree level order traversal
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root: TreeNode):
    if not root:
        return []
    q = deque([root])
    res = []

    while len(q):
        # all here currently belong to same level
        # but we will insert in queue 
        # so we find the lenth now 
        n = len(q)
        # only these are in same level 
        # traverse these now
        level = []
        for i in range(n):
            node = q.popleft()
            level.append(node.val)
            # binary tree so add left and right if they exist 
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level[-1])
    return res

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)
#        10
#       /  \
#      5    15
#     / \     \
#    3   7     18

print(level_order_traversal(root))



root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4, right=TreeNode(7))
root2.left.right = TreeNode(5)
root2.right.right = TreeNode(6)
#        1
#       /  \
#      2    3
#     / \     \
#    4   5     6
#    \
#     7

print(level_order_traversal(root2))
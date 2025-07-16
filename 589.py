"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # time: O(n), space: O(n)
        if not root:
            return []
        res = []
        def helper(node):
            res.append(node.val)
            for c in node.children:
                helper(c)
        helper(root)
        return res
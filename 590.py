"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # time: O(n), space: O(n)
        res = []
        if not root:
            return res
        def helper(node):
            for c in node.children:
                helper(c)
            res.append(node.val)
        helper(root)
        return res
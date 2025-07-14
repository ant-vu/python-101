"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # time: O(n), space: O(n)
        if not root:
            return 0
        q = deque()
        q.append((root, 1))
        while q:
            node, lvl = q.popleft()
            for c in node.children:
                if c:
                    q.append((c, lvl + 1))
        return lvl
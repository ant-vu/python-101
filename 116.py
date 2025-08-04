"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # time: O(n), space: O(1)
        if not root:
            return None
        leftMost = root
        while leftMost.left:
            cur = leftMost
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            leftMost = leftMost.left
        return root

        # time: O(n), space: O(w)
        # if not root:
        #     return None
        # q = deque([root])
        # while q:
        #     prev = None
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         if prev:
        #             prev.next = node
        #         prev = node
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # time: O(n), space: O(n)
        q = deque()
        q.append(root)
        cnt = 0
        while q:
            node = q.popleft()
            if node:
                cnt += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return cnt
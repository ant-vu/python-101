# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # time: O(n), space: O(n)
        def dfs(node):
            if node:
                q.append(node)
                dfs(node.left)
                dfs(node.right)
        
        q = deque()
        dfs(root)
        if q:
            q.popleft()
        while q:
            root.right = q.popleft()
            root.left = None
            root = root.right
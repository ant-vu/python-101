# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # time: O(n), space: O(n)
        if not root:
            return 0
        min_depth = float("inf")
        def dfs(node, cur_depth):
            nonlocal min_depth
            if not node:
                return
            if not node.left and not node.right:
                min_depth = min(min_depth, cur_depth)
            dfs(node.left, cur_depth + 1)
            dfs(node.right, cur_depth + 1)
        dfs(root, 1)
        return min_depth
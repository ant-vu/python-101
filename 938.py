# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # time: O(n), space: O(n)
        def dfs(root):
            nonlocal res
            if root:
                res += root.val if low <= root.val <= high else 0
                dfs(root.left)
                dfs(root.right)
        
        res = 0
        dfs(root)
        return res
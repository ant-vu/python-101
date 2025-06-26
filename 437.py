# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def helper(root, targetSum):
            nonlocal res
            if not root:
                return None
            if targetSum - root.val == 0:
                res += 1
            targetSum -= root.val
            helper(root.left, targetSum)
            helper(root.right, targetSum)
        
        def dfs(root):
            if not root:
                return None
            helper(root, targetSum)
            dfs(root.left)
            dfs(root.right)

        res = 0
        if not root:
            return 0
        dfs(root)
        return res
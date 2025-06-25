# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # time: O(n), space: O(n)
        flg = False
        def dfs(node, total=0):
            nonlocal flg
            if node:
                if not node.left and not node.right and total + node.val == targetSum:
                    flg = True
                    return
                else:
                    dfs(node.left, total + node.val)
                    dfs(node.right, total + node.val)
        dfs(root)
        return True if flg else False
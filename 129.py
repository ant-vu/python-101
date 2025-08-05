# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # time: O(n), space: O(h)
        def dfs(node, path):
            nonlocal res
            if node:
                path += str(node.val)
                if not node.left and not node.right:
                    res += int(path)
                dfs(node.left, path)
                dfs(node.right, path)
        
        res = 0
        dfs(root, "")
        return res
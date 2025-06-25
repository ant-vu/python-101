# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # time: O(n), space: O(h)
        res = 0
        def dfs(node, maxi):
            nonlocal res
            if node:
                if node.val >= maxi:
                    res += 1
                if node.left:
                    dfs(node.left, max(maxi, node.left.val))
                if node.right:
                    dfs(node.right, max(maxi, node.right.val))
        dfs(root, root.val)
        return res
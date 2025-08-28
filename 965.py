# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # time: O(n), space: O(n)
        left = not root.left or (root.val == root.left.val and self.isUnivalTree(root.left))
        right = not root.right or (root.val == root.right.val and self.isUnivalTree(root.right))
        return left and right

        # time: O(n), space: O(n)
        # def dfs(node):
        #     if node:
        #         res.append(node.val)
        #         dfs(node.left)
        #         dfs(node.right)
        
        # res = []
        # dfs(root)
        # return len(set(res)) == 1

        # time: O(n), space: O(n)
        # def dfs(node):
        #     nonlocal res
        #     if node:
        #         if node.val != root.val:
        #             res = False
        #             return
        #         dfs(node.left)
        #         dfs(node.right)
        
        # res = True
        # dfs(root)
        # return res
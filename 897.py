# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # time: O(n), space: O(n)
        def helper(root, nxt):
            if not root:
                return nxt
            res = helper(root.left, root)
            root.left = None
            root.right = helper(root.right, nxt)
            return res
        
        return helper(root, None)

        # time: O(n), space: O(n)
        # def dfs(root):
        #     if root:
        #         dfs(root.left)
        #         inorder.append(root.val)
        #         dfs(root.right)
        
        # inorder = []
        # dfs(root)
        # for i in range(len(inorder)):
        #     inorder[i] = TreeNode(val=inorder[i])
        # for i in range(len(inorder) - 1):
        #     inorder[i].right = inorder[i + 1]
        # return inorder[0]
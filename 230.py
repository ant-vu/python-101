# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # time: O(n), space: O(n)
        cnt = 0
        res = None
        def inorder(node):
            nonlocal cnt, res
            if node:
                inorder(node.left)
                cnt += 1
                if cnt == k:
                    res = node.val
                    return
                inorder(node.right)
        inorder(root)
        return res

        # time: O(n), space: O(n)
        # inorder = []
        # def helper(node):
        #     if node:
        #         helper(node.left)
        #         inorder.append(node.val)
        #         helper(node.right)
        # helper(root)
        # return inorder[k - 1]
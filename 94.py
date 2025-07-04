# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # time: O(n), space: O(n)
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

        # time: O(n), space: O(n)
        # res = []
        # def helper(node):
        #     if not node:
        #         return
        #     helper(node.left)
        #     res.append(node.val)
        #     helper(node.right)
        # helper(root)
        # return res
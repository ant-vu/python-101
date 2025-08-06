# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # time: O(n), space: O(n)
        def inorder(node):
            if node:
                inorder(node.left)
                nodes.append(node.val)
                inorder(node.right)

        nodes = []
        inorder(root)
        res = float("inf")
        for i in range(len(nodes) - 1):
            res = min(res, nodes[i + 1] - nodes[i])
        return res
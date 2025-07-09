# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # time: O(n), space: O(n)
        res = []
        def dfs(node, path):
            if node:
                path += "->" + str(node.val)
                if not node.left and not node.right:
                    res.append(path[2:])
                dfs(node.left, path)
                dfs(node.right, path)
        dfs(root, "")
        return res
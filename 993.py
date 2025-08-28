# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # time: O(n), space: O(n)
        def dfs(node, depth, parent):
            nonlocal depth_x, depth_y, parent_x, parent_y
            if node:
                if node.val == x:
                    depth_x = depth
                    parent_x = parent
                elif node.val == y:
                    depth_y = depth
                    parent_y = parent
                dfs(node.left, depth + 1, node)
                dfs(node.right, depth + 1, node)

        depth_x, depth_y = None, None
        parent_x, parent_y = None, None
        dfs(root, 0, None)
        return depth_x == depth_y and parent_x != parent_y
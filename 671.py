# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # time: O(n), space: O(n)
        def dfs(root):
            nonlocal res
            if root:
                if min1 < root.val < res:
                    res = root.val
                elif min1 == root.val:
                    dfs(root.left)
                    dfs(root.right)

        min1 = root.val
        res = float('inf')
        dfs(root)
        return res if res != float('inf') else -1

        # time: O(n), space: O(n)
        # def dfs(root):
        #     if root:
        #         nodes.add(root.val)
        #         dfs(root.left)
        #         dfs(root.right)
        
        # nodes = set()
        # dfs(root)
        # nodes.remove(root.val)
        # return min(nodes) if nodes else -1
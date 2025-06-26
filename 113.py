# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # time: O(n), space: O(n)
        def dfs(node, total=0, li=[]):
            nonlocal res
            if node:
                if not node.left and not node.right and total + node.val == targetSum:
                    res.append(li + [node.val])
                else:
                    dfs(node.left, total + node.val, li + [node.val])
                    dfs(node.right, total + node.val, li + [node.val])
        res = []
        dfs(root)
        return res
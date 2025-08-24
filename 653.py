# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # time: O(n), space: O(n)
        def helper(root, k):
            if not root:
                return False
            elif k - root.val in vis:
                return True
            vis.add(root.val)
            return helper(root.left, k) or helper(root.right, k)
        
        vis = set()
        return helper(root, k)
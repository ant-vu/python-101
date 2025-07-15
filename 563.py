# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        # time: O(n), space: O(n)
        if not root:
            return 0
        totalTilt = 0
        def helper(root):
            nonlocal totalTilt
            lSum = rSum = 0
            def leftSum(root, isLeft):
                if not root:
                    return
                elif isLeft:
                    nonlocal lSum
                    lSum += root.val
                else:
                    nonlocal rSum
                    rSum += root.val
                leftSum(root.left, isLeft)
                leftSum(root.right, isLeft)
            leftSum(root.left, True)
            leftSum(root.right, False)
            root.val = abs(lSum - rSum)
            totalTilt += abs(lSum - rSum)
        
        q = deque([root])
        while q:
            node = q.popleft()
            helper(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return totalTilt
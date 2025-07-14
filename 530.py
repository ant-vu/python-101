# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # time: O
        nodes = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            nodes.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res = inf
        nodes.sort()
        for i in range(len(nodes) - 1):
            res = min(res, abs(nodes[i] - nodes[i + 1]))
        return res
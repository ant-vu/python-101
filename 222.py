# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # time: O(log^2(n)), space: O(log(n))
        def getDepth(node):
            depth = 0
            while node:
                node = node.left
                depth += 1
            return depth
        
        if not root:
            return 0
        leftDepth = getDepth(root.left)
        rightDepth = getDepth(root.right)
        if leftDepth == rightDepth:
            return (2 ** leftDepth) + self.countNodes(root.right)
        return (2 ** rightDepth) + self.countNodes(root.left)

        # time: O(n), space: O(w)
        # if not root:
        #     return 0
        # q = deque([root])
        # cnt = 0
        # while q:
        #     for _ in range(len(q)):
        #         cnt += 1
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return cnt
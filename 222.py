# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # time: O(logn * logn), space: O(logn)
        def getDepth(node, left):
            depth = 0
            while node:
                node = node.left if left else node.right
                depth += 1
            return depth
        
        if not root:
            return 0
        left = getDepth(root.left, True) + 1
        right = getDepth(root.right, False) + 1
        if left == right:
            return (2 ** left) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

        # time: O(n), space: O(n)
        # q = deque()
        # q.append(root)
        # cnt = 0
        # while q:
        #     node = q.popleft()
        #     if node:
        #         cnt += 1
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return cnt
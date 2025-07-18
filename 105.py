# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # time: O(n), space: O(n)
        mapping = {}
        for i in range(len(inorder)):
            mapping[inorder[i]] = i
        preorder = deque(preorder)
        def build(start, end):
            if start > end:
                return None
            root = TreeNode(preorder.popleft())
            mid = mapping[root.val]
            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)
            return root
        return build(0, len(preorder) - 1)

        # time: O(n^2), space: O(n^2)
        # preorder = deque(preorder)
        # def build(preorder, inorder):
        #     if inorder:
        #         idx = inorder.index(preorder.popleft())
        #         root = TreeNode(inorder[idx])
        #         root.left = build(preorder, inorder[:idx])
        #         root.right = build(preorder, inorder[idx+1:])
        #         return root
        # return build(preorder, inorder)
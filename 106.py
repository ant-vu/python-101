# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # time: O(n), space: O(n)
        if not inorder:
            return None
        rootVal = postorder.pop()
        root = TreeNode(rootVal)
        inorderIdx = inorder.index(rootVal)
        root.right = self.buildTree(inorder[inorderIdx+1:], postorder)
        root.left = self.buildTree(inorder[:inorderIdx], postorder)
        return root
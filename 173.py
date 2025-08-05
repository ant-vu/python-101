# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def dfs(node):
            if node:
                dfs(node.left)
                self.q.append(node.val)
                dfs(node.right)
        
        self.q = deque()
        dfs(root)

    def next(self) -> int:
        # time: O(1), space: O(h)
        return self.q.popleft()

    def hasNext(self) -> bool:
        # time: O(1), space: O(h)
        return bool(self.q)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
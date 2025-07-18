# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # time: O(n), space: O(n)
        q = deque([root])
        res = []
        while q:
            n = len(q)
            s = 0
            for _ in range(n):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(s / n)
        return res

        # time: O(n), space: O(n)
        # lvls = []
        # q = deque()
        # q.append((root, 0))
        # while q:
        #     node = q.popleft()
        #     lvls.append((node[0].val, node[1]))
        #     if node[0].left:
        #         q.append((node[0].left, node[1] + 1))
        #     if node[0].right:
        #         q.append((node[0].right, node[1] + 1))
        # mapping = {}
        # for l in lvls:
        #     if l[1] not in mapping:
        #         mapping[l[1]] = [l[0]]
        #     else:
        #         mapping[l[1]].append(l[0])
        # res = []
        # for k, v in mapping.items():
        #     res.append(sum(v) / len(v))
        # return res
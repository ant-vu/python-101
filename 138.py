"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # time: O(n), space: O(n)
        mapping = {None: None}
        cur = head
        while cur:
            mapping[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            copy = mapping[cur]
            copy.next = mapping[cur.next]
            copy.random = mapping[cur.random]
            cur = cur.next
        return mapping[head]

        # time: O(n), space: O(n)
        # if not head:
        #     return head
        # nodes = []
        # randoms = []
        # randomsIdx = []
        # cur = head
        # while cur:
        #     nodes.append(Node(cur.val))
        #     randoms.append(cur.random)
        #     cur = cur.next
        # for i in range(len(nodes) - 1):
        #     nodes[i].next = nodes[i + 1]
        # for r in randoms:
        #     idx = len(nodes)
        #     while r:
        #         idx -= 1
        #         r = r.next
        #     randomsIdx.append(idx)
        # for i in range(len(nodes)):
        #     if randomsIdx[i] == len(nodes):
        #         nodes[i].random = None
        #     else:
        #         nodes[i].random = nodes[randomsIdx[i]]
        # return nodes[0]
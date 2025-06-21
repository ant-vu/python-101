# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # time: O(n), space: O(n)
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        size = [0] * k
        idx = 0
        while length > 0:
            length -= 1
            size[idx] += 1
            idx = (idx + 1) % k
        res = []
        for s in size:
            tmp2 = head
            for _ in range(s - 1):
                if tmp2:
                    tmp2 = tmp2.next
            if tmp2:
                tmp3 = tmp2.next
            else:
                tmp3 = None
            if tmp2:
                tmp2.next = None
            res.append(head)
            head = tmp3
        return res
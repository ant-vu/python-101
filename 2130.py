# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # time: O(n), space: O(n)
        li = []
        while head:
            li.append(head.val)
            head = head.next
        res = float("-inf")
        for i in range(len(li) // 2):
            res = max(res, li[i] + li[len(li) - 1 - i])
        return res
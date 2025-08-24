# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # time: O(n), space: O(1)
        res = 0
        while head:
            res = 2 * res + head.val
            head = head.next
        return res

        # time: O(n), space: O(n)
        # binary = ''
        # while head:
        #     binary += str(head.val)
        #     head = head.next
        # factor = 1
        # res = 0
        # for n in binary[::-1]:
        #     if n == '1':
        #         res += factor
        #     factor *= 2
        # return res
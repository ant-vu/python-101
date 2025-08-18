# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # time: O(m + n), space: O(m + n)
        num1 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        num2 = ''
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        tot = str(int(num1) + int(num2))
        res = ListNode(val=int(tot[0]))
        cur = res
        for t in tot[1:]:
            nxt = ListNode(val=int(t))
            cur.next = nxt
            cur = cur.next
        return res
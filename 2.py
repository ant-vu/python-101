# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # time: O(max(m, n)), space: O(1)
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            total = l1Val + l2Val + carry
            carry = total // 10
            node = ListNode(total % 10)
            cur.next = node
            cur = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

        # time: O(m + n), space: O(1)
        # head1, len1 = l1, 0
        # while head1:
        #     len1 += 1
        #     head1 = head1.next
        # head2, len2 = l2, 0
        # while head2:
        #     len2 += 1
        #     head2 = head2.next
        # carry = 0
        # if len1 >= len2:
        #     dummy = ListNode(val=None, next=l1)
        #     while l1 and l2:
        #         total = l1.val + l2.val + carry
        #         l1.val = total % 10
        #         carry = total // 10
        #         if l1.next == None and carry:
        #             l1.next = ListNode(val=1, next=None)
        #             return dummy.next
        #         l1 = l1.next
        #         l2 = l2.next
        #     while l1:
        #         total = l1.val + carry
        #         l1.val = total % 10
        #         carry = total // 10
        #         if l1.next == None and carry:
        #             l1.next = ListNode(val=1, next=None)
        #             break
        #         l1 = l1.next
        # else:
        #     dummy = ListNode(val=None, next=l2)
        #     while l1 and l2:
        #         total = l1.val + l2.val + carry
        #         l2.val = total % 10
        #         carry = total // 10
        #         if l2.next == None and carry:
        #             l2.next = ListNode(val=1, next=None)
        #             return dummy.next
        #         l1 = l1.next
        #         l2 = l2.next
        #     while l2:
        #         total = l2.val + carry
        #         l2.val = total % 10
        #         carry = total // 10
        #         if l2.next == None and carry:
        #             l2.next = ListNode(val=1, next=None)
        #             break
        #         l2 = l2.next
        # return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # time: O(n), space: O(1)
        x = ListNode(next=head)
        y = x
        for _ in range(n):
            head = head.next
        while head:
            y = y.next
            head = head.next
        y.next = y.next.next
        return x.next

        # time: O(n), space: O(1)
        # x = None
        # y = head
        # z = head
        # for _ in range(n):
        #     z = z.next
        # while z:
        #     x = y
        #     y = y.next
        #     z = z.next
        # if x is None:
        #     return head.next
        # x.next = y.next
        # return head
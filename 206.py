# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # time: O(n), space: O(n)
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

        # time: O(n), space: O(1)
        # cur = None
        # while head:
        #     tmp = head.next
        #     head.next = cur
        #     cur = head
        #     head = tmp
        # return cur

        # time: O(n), space: O(1)
        # if not head or not head.next:
        #     return head
        # pre, cur = head, head.next
        # pre.next = None
        # while cur:
        #     tmp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = tmp
        # return pre
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # time: O(n), space: O(1)
        res = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return res

        # time: O(n), space: O(1)
        # if not head:
        #     return head
        # dummy = ListNode(next=head)
        # prev = head
        # while head:
        #     if prev.val == head.val:
        #         head = head.next
        #     else:
        #         prev.next = head
        #         prev = prev.next
        #         head = head.next
        # prev.next = head
        # return dummy.next
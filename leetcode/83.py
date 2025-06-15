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
        # dummy = ListNode(next=head)
        # if not head:
        #     return None
        # slow = head
        # fast = head.next
        # while fast:
        #     if slow.val == fast.val:
        #         if fast.next == None:
        #             slow.next = None
        #         fast = fast.next
        #         continue
        #     slow.next = fast
        #     slow = fast
        #     fast = fast.next
        # return dummy.next
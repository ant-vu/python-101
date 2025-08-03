# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # time: O(n), space: O(1)
        if not head:
            return head
        length = 1
        dummy = head
        while dummy.next:
            dummy = dummy.next
            length += 1
        position = k % length
        if position == 0:
            return head
        current = head
        for _ in range(length - position - 1):
            current = current.next
        new_head = current.next
        current.next = None
        dummy.next = head
        return new_head

        # time: O(n), space: O(1)
        # if not head or not head.next:
        #     return head
        # length = 0
        # cur = head
        # while cur:
        #     length += 1
        #     cur = cur.next
        # k %= length
        # if k == 0:
        #     return head
        # prev = head
        # cur = head
        # for _ in range(k + 1):
        #     cur = cur.next
        # while cur:
        #     prev = prev.next
        #     cur = cur.next
        # start = prev.next
        # prev.next = None
        # end = start
        # while end and end.next:
        #     end = end.next
        # end.next = head
        # return start
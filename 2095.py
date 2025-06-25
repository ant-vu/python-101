# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # time: O(n), space: O(1)
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        if length == 1:
            return None
        cur2 = head
        for _ in range((length // 2) - 1):
            cur2 = cur2.next
        cur2.next = cur2.next.next
        return head
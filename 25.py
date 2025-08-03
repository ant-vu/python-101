# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # time: O(n), space: O(1)
        dummy = ListNode(next=head)
        groupPrev = dummy

        def getKthNode(start, k):
            while start and k > 0:
                start = start.next
                k -= 1
            return start
        
        while True:
            kthNode = getKthNode(groupPrev, k)
            if not kthNode:
                break
            groupNext = kthNode.next
            
            prev = kthNode.next
            cur = groupPrev.next
            while cur != groupNext:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            tmp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = tmp
        return dummy.next

        # time: O(n), space: O(n / k)
        # if not head:
        #     return head
        # tail = head
        # for _ in range(k):
        #     if not tail:
        #         return head
        #     tail = tail.next
        
        # def reverse(cur, end):
        #     prev = None
        #     while cur != end:
        #         nxt = cur.next
        #         cur.next = prev
        #         prev = cur
        #         cur = nxt
        #     return prev
        
        # newHead = reverse(head, tail)
        # head.next = self.reverseKGroup(tail, k)
        # return newHead
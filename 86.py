# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # time: O(n), space: O(1)
        slist = ListNode()
        blist = ListNode()
        small = slist
        big = blist
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        small.next = blist.next
        big.next = None
        return slist.next

        # time: O(n), space: O(1)
        # if not head or not head.next:
        #     return head
        # lDummy = ListNode()
        # rDummy = ListNode()
        # left = lDummy
        # right = rDummy
        # pivot = None
        # end = None
        # cur = head
        # while cur:
        #     if cur.val < x:
        #         left.next = cur
        #         left = left.next
        #         pivot = left
        #     else:
        #         right.next = cur
        #         right = right.next
        #         end = right
        #     cur = cur.next
        # if pivot:
        #     pivot.next = rDummy.next
        # if end:
        #     end.next = None
        # if lDummy.next:
        #     return lDummy.next
        # return rDummy.next
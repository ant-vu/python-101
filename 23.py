# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # time: O(nlog(k)), space: O(n)
        def mergeTwoLists(list1, list2):
            dummy = ListNode()
            cur = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            if list1:
                cur.next = list1
            elif list2:
                cur.next = list2
            return dummy.next

        if len(lists) == 0:
            return None
        while len(lists) > 1:
            tmp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                tmp.append(mergeTwoLists(l1, l2))
            lists = tmp
        return lists[0]
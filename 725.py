# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # time: O(n), space: O(1)
        ans = [None] * k
        size = 0
        current = head
        while current is not None:
            size += 1
            current = current.next
        split_size = size // k
        num_remaining_parts = size % k
        current = prev = head
        for i in range(k):
            new_part = current
            current_size = split_size
            if num_remaining_parts > 0:
                num_remaining_parts -= 1
                current_size += 1
            j = 0
            while j < current_size:
                prev = current
                if current:
                    current = current.next
                j += 1
            if prev:
                prev.next = None
            ans[i] = new_part
        return ans

        # time: O(n), space: O(n)
        # ans = [None] * k
        # size = 0
        # current = head
        # while current is not None:
        #     size += 1
        #     current = current.next
        # split_size = size // k
        # num_remaining_parts = size % k
        # current = head
        # for i in range(k):
        #     new_part = ListNode(0)
        #     tail = new_part
        #     current_size = split_size
        #     if num_remaining_parts > 0:
        #         num_remaining_parts -= 1
        #         current_size += 1
        #     for j in range(current_size):
        #         tail.next = ListNode(current.val)
        #         tail = tail.next
        #         current = current.next
        #     ans[i] = new_part.next
        # return ans

        # time: O(n), space: O(n)
        # length = 0
        # tmp = head
        # while tmp:
        #     length += 1
        #     tmp = tmp.next
        # size = [0] * k
        # idx = 0
        # while length > 0:
        #     length -= 1
        #     size[idx] += 1
        #     idx = (idx + 1) % k
        # res = []
        # for s in size:
        #     tmp2 = head
        #     for _ in range(s - 1):
        #         if tmp2:
        #             tmp2 = tmp2.next
        #     if tmp2:
        #         tmp3 = tmp2.next
        #     else:
        #         tmp3 = None
        #     if tmp2:
        #         tmp2.next = None
        #     res.append(head)
        #     head = tmp3
        # return res
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # time: O(n), space: O(1)
        time = 0
        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], tickets[k])
            else:
                time += min(tickets[i], tickets[k] - 1)
        return time

        # time: O(n*m), space: O(n)
        # res = 0
        # q = deque(tickets)
        # while q:
        #     res += 1
        #     front = q.popleft()
        #     if front > 1:
        #         q.append(front - 1)
        #     if k > 0:
        #         k -= 1
        #     else:
        #         if front == 1:
        #             break
        #         k = len(q) - 1
        # return res
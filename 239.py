class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # time: O(n), space: O(n)
        res = []
        q = deque()
        for i, n in enumerate(nums):
            while q and q[-1] < n:
                q.pop()
            q.append(n)
            if i >= k and nums[i - k] == q[0]:
                q.popleft()
            if i >= k - 1:
                res.append(q[0])
        return res
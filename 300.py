class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # time: O(nlogn), space: O(n)
        def binary_search(res, n):
            l, r = 0, len(res) - 1
            while l <= r:
                m = l + (r - l) // 2
                if res[m] == n:
                    return m
                elif res[m] < n:
                    l = m + 1
                else:
                    r = m - 1
            return l

        res = []
        for n in nums:
            if not res or res[-1] < n:
                res.append(n)
            else:
                idx = binary_search(res, n)
                res[idx] = n
        return len(res)

        # time: O(n^2), space: O(n)
        # dp = [0] * len(nums)
        # dp[-1] = 1
        # for i in range(len(nums) - 2, -1, -1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] < nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        #         else:
        #             dp[i] = max(dp[i], 1)
        # return max(dp)
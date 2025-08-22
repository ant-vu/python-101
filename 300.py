class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # time: O(nlogn), space: O(n)
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x)
                sub[idx] = x
        return len(sub)

        # time: O(n^2), space: O(n)
        # n = len(nums)
        # dp = [1] * n
        # for i in range(n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        #     print(dp)
        # return max(dp)
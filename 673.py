class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # time: O(n^2), space: O(n)
        n = len(nums)
        if n <= 1:
            return n
        lengths = [1] * n
        counts = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
        maxLen = max(lengths)
        return sum(count for length, count in zip(lengths, counts) if length == maxLen)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # time: O(n+k), space: O(k)
        maxVal = max(nums)
        cnts = [0] * (maxVal + 1)
        for val in nums:
            cnts[val] += 1
        curSum = 0
        for i in range(maxVal + 1):
            cnts[i], curSum = curSum, curSum + cnts[i]
        return [cnts[val] for val in nums]
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # time: O(n), space: O(n)
        houses = [0] * (max(nums) + 1)
        for i in nums:
            houses[i] += i
        if len(houses) < 2:
            return houses[0]
        l = houses[0]
        r = max(houses[0], houses[1])
        for i in range(2, len(houses)):
            cur = max(l + houses[i], r)
            l, r = r, cur
        return r
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # time: O(n^2), space: O(1)
        n = len(nums)
        nums.sort()
        closestSum = inf
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if abs(curSum - target) < abs(closestSum - target):
                    closestSum = curSum
                if curSum < target:
                    l += 1
                elif curSum > target:
                    r -= 1
                else:
                    return curSum
        return closestSum
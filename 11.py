class Solution:
    def maxArea(self, height: List[int]) -> int:
        # time: O(n), space: O(1)
        maxWater = 0
        l = 0
        r = len(height) - 1
        while l < r:
            curWater = min(height[l], height[r]) * (r - l)
            maxWater = max(maxWater, curWater)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxWater
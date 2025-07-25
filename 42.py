class Solution:
    def trap(self, height: List[int]) -> int:
        # time: O(n), space: O(1)
        n = len(height)
        water = 0
        l = 0
        r = n - 1
        maxL = height[l]
        maxR = height[r]
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                water += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                water += maxR - height[r]
        return water

        # time: O(n^2), space: O(1), TLE
        # n = len(height)
        # water = 0
        # l = 0
        # r = n - 1
        # while l + 1 < r:
        #     for i in range(l + 1, r):
        #         wall = min(height[l], height[r])
        #         if wall - height[i] > 0:
        #             water += wall - height[i]
        #             height[i] = wall
        #     if height[l] < height[r]:
        #         l += 1
        #     else:
        #         r -= 1
        # return water
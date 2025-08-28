class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # time: O(logn), space: O(1)
        def my_bisect_left(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return l
        
        def my_bisect_right(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return l

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return [my_bisect_left(nums, target), my_bisect_right(nums, target) - 1]
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return [-1, -1]

        # time: O(logn), space: O(1)
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     m = l + (r - l) // 2
        #     if nums[m] == target:
        #         return [bisect_left(nums, target), bisect_right(nums, target) - 1]
        #     elif nums[m] < target:
        #         l = m + 1
        #     else:
        #         r = m - 1
        # return [-1, -1]
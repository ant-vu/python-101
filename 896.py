class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # time: O(n), space: O(1)
        if len(nums) == 1:
            return True
        isInc = True
        isDec = True
        for i in range(len(nums) - 1):
            if not isInc and not isDec:
                return False
            if nums[i] < nums[i + 1]:
                isDec = False
            if nums[i] > nums[i + 1]:
                isInc = False
        return isInc or isDec

        # time: O(n), space: O(1)
        # if len(nums) == 1:
        #     return True
        # inc = False
        # dec = False
        # seen = False
        # for i in range(len(nums) - 1):
        #     if not seen and nums[i] < nums[i + 1]:
        #         inc = True
        #         seen = True
        #     elif not seen and nums[i] > nums[i + 1]:
        #         dec = True
        #         seen = True
        #     elif (inc and nums[i] > nums[i + 1]) or (dec and nums[i] < nums[i + 1]):
        #         return False
        # return True
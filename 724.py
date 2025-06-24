class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        l, r = 0, sum(nums)
        for i, n in enumerate(nums):
            r -= n
            if l == r:
                return i
            l += n
        return -1

        # time: O(n), space: O(n)
        # if len(nums) == 1:
        #     return 0
        # forward, backward = nums[:], nums[:]
        # for i in range(len(nums) - 1):
        #     forward[i + 1] += forward[i]
        # for i in range(len(nums) - 1, 0, -1):
        #     backward[i - 1] += backward[i]
        # for i in range(len(nums)):
        #     if i == 0 and backward[1] == 0:
        #         return 0
        #     elif i == len(nums) - 1 and forward[-2] == 0:
        #         return len(nums) - 1
        #     elif 0 < i < len(nums) - 1 and forward[i - 1] == backward[i + 1]:
        #         return i
        # return -1
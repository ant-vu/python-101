class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # time: O(n), space: O(n)
        n = len(nums)
        res = [1] * n
        l = 1
        for i in range(n):
            res[i] *= l
            l *= nums[i]
        r = 1
        for i in range(n - 1, -1, -1):
            res[i] *= r
            r *= nums[i]
        return res

        # time: O(n^2), space: O(n), TLE
        # n = len(nums)
        # res = [1] * n
        # for i in range(n):
        #     for j in range(n):
        #         if i != j:
        #             res[i] *= nums[j]
        # return res

        # time: O(n), space: O(n)
        # prefixProducts = [nums[0]]
        # curPrefix = nums[0]
        # for n in nums[1:]:
        #     curPrefix *= n
        #     prefixProducts.append(curPrefix)

        # suffixProducts = [nums[-1]]
        # curSuffix = nums[-1]
        # for n in nums[:-1][::-1]:
        #     curSuffix *= n
        #     suffixProducts.append(curSuffix)
        # suffixProducts.reverse()

        # res = []
        # for i in range(len(nums)):
        #     if i == 0:
        #         res.append(suffixProducts[1])
        #     elif i == len(nums) - 1:
        #         res.append(prefixProducts[-2])
        #     else:
        #         res.append(prefixProducts[i - 1] * suffixProducts[i + 1])
        # return res
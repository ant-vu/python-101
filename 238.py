class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # time: O(n), space: O(1)
        n = len(nums)
        res = [1] * n
        cur = 1
        for i in range(len(nums)):
            res[i] *= cur
            cur *= nums[i]
        cur = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= cur
            cur *= nums[i]
        return res

        # time: O(n), space: O(n)
        # products = []
        # cur = 1
        # for n in nums:
        #     cur *= n
        #     products.append(cur)
        # products_rev = []
        # cur = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     cur *= nums[i]
        #     products_rev.insert(0, cur)
        # res = []
        # for i in range(len(nums)):
        #     if i == 0:
        #         res.append(products_rev[1])
        #     elif i == len(nums) - 1:
        #         res.append(products[-2])
        #     else:
        #         res.append(products[i - 1] * products_rev[i + 1])
        # return res
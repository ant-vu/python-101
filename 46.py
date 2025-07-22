class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # time: O(n * n!), space: O(n)
        res = []

        def backtrack(idx):
            if idx == len(nums):
                res.append(nums[:])
                return
            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                backtrack(idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]
        
        backtrack(0)
        return res

        # time: O(n * n!), space: O(n)
        # res = []
        # comb = []

        # def backtrack(idx):
        #     if len(comb) == len(nums):
        #         res.append(comb[:])
        #         return
        #     for n in nums:
        #         if n not in comb:
        #             comb.append(n)
        #             backtrack(idx + 1)
        #             comb.pop()
        
        # backtrack(0)
        # return res
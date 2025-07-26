class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # time: O(n * n!), space: O(n)
        n = len(nums)
        if n == 1:
            return [nums[:]]
        res = []
        for _ in range(n):
            num = nums.pop(0)
            perms = self.permute(nums)
            for p in perms:
                p.append(num)
            res.extend(perms)
            nums.append(num)
        return res

        # time: O(n * n!), space: O(n)
        # n = len(nums)
        # perms = []

        # def backtrack(start):
        #     if start == n:
        #         perms.append(nums[:])
        #         return
        #     for i in range(start, n):
        #         nums[start], nums[i] = nums[i], nums[start]
        #         backtrack(start + 1)
        #         nums[start], nums[i] = nums[i], nums[start]

        # backtrack(0)
        # return perms
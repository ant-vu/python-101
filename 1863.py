class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # time: O(n*2^n), space: O(n*2^n)
        def backtrack(start, comb):
            res.append(comb[:])
            for i in range(start, len(nums)):
                comb.append(nums[i])
                backtrack(i + 1, comb)
                comb.pop()

        res = []
        backtrack(0, [])
        ans = 0
        for i in res:
            if len(i) == 0:
                continue
            if len(i) == 1:
                ans += i[0]
            else:
                tmp = i[0]
                for j in i[1:]:
                    tmp ^= j
                ans += tmp
        return ans
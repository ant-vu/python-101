class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # time: O(2^n), space: O(n)
        res = []
        def backtrack(total, comb, idx):
            if total == target:
                res.append(comb[:])
                return
            if total > target:
                return
            for i in range(idx, len(candidates)):
                backtrack(total + candidates[i], comb + [candidates[i]], i)
        backtrack(0, [], 0)
        return res
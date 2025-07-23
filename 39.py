class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # time: O(2^n), space: O(t/d), t=target, d=smallest candidate
        res = []

        def backtrack(idx, comb, total):
            if total == target:
                res.append(comb[:])
                return
            if total > target or idx >= len(candidates):
                return
            comb.append(candidates[idx])
            backtrack(idx, comb, total + candidates[idx])
            comb.pop()
            backtrack(idx + 1, comb, total)

        backtrack(0, [], 0)
        return res
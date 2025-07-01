class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # time: O(2^n), space: O(n)
        res = []
        seen = []
        def backtrack(total, comb):
            if total == n and len(comb) == k and sorted(comb[:]) not in seen:
                res.append(sorted(comb[:]))
                seen.append(sorted(comb[:]))
                return
            if total > n or len(comb) > k:
                return
            for i in range(1, 10):
                if i not in comb:
                    backtrack(total + i, comb + [i])
        backtrack(0, [])
        return res
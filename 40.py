class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # time: O(2^n), space: O(n)
        candidates.sort()
        res = []
        def backtrack(ans, tmp_list, candidates, total_left, idx):
            if total_left < 0:
                return
            elif total_left == 0:
                ans.append(tmp_list[:])
            else:
                for i in range(idx, len(candidates)):
                    if i > idx and candidates[i] == candidates[i - 1]:
                        continue
                    if total_left < candidates[i]:
                        break
                    tmp_list.append(candidates[i])
                    backtrack(ans, tmp_list, candidates, total_left - candidates[i], i + 1)
                    tmp_list.pop()
        backtrack(res, [], candidates, target, 0)
        return res
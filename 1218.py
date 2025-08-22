class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # time: O(n), space: O(n)
        res = {}
        for num in arr:
            res[num] = 1 + res.get(num - difference, 0)
        return max(res.values())
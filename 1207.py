class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # time: O(n), space: O(n)
        cnt = {}
        for i in arr:
            cnt[i] = cnt.get(i, 0) + 1
        return len(cnt.values()) == len(set(cnt.values()))
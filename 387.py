class Solution:
    def firstUniqChar(self, s: str) -> int:
        # time: O(n), space: O(n)
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1
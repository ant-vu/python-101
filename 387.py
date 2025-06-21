class Solution:
    def firstUniqChar(self, s: str) -> int:
        # time: O(n), space: O(1)
        counter = Counter(s)
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1

        # time: O(n), space: O(1)
        # counter = defaultdict(int)
        # for c in s:
        #     counter[c] += 1
        # for i, c in enumerate(s):
        #     if counter[c] == 1:
        #         return i
        # return -1
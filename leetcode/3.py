class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # time: O(n), space: O(1)
        count = {}
        res = 0
        l = 0
        for r, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            while count[c] > 1:
                count[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        return res

        # time: O(n), space: O(1)
        # unique = set()
        # res = 0
        # l = 0
        # for r in range(len(s)):
        #     while s[r] in unique:
        #         unique.remove(s[l])
        #         l += 1
        #     unique.add(s[r])
        #     res = max(r - l + 1, res)
        # return res
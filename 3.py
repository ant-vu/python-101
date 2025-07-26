class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # time: O(n), space: O(1)
        lastSeen = {}
        maxCount = 0
        l = 0
        for r, c in enumerate(s):
            if c in lastSeen and lastSeen[c] >= l:
                l = lastSeen[c] + 1
            lastSeen[c] = r
            maxCount = max(maxCount, r - l + 1)
        return maxCount

        # time: O(n), space: O(1)
        # count = {}
        # maxCount = 0
        # l = 0
        # for r, c in enumerate(s):
        #     count[c] = count.get(c, 0) + 1
        #     while count[c] > 1:
        #         count[s[l]] -= 1
        #         l += 1
        #     maxCount = max(maxCount, r - l + 1)
        # return maxCount

        # time: O(n), space: O(1)
        # seen = set()
        # maxCount = 0
        # l = 0
        # for r in range(len(s)):
        #     while s[r] in seen:
        #         seen.remove(s[l])
        #         l += 1
        #     seen.add(s[r])
        #     maxCount = max(maxCount, r - l + 1)
        # return maxCount
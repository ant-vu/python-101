class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # time: O(m * n), space: O(m)
        prefix = strs[0]
        prefixLen = len(prefix)
        for s in strs[1:]:
            while prefix != s[:prefixLen]:
                prefixLen -= 1
                if prefixLen == 0:
                    return ""
                prefix = prefix[:prefixLen]
        return prefix

        # time: O(m * n), space: O(m)
        # if len(set(strs)) == 1:
        #     return strs[0]
        # minLen = inf
        # minWord = None
        # for s in strs:
        #     if len(s) < minLen:
        #         minLen = len(s)
        #         minWord = s
        # prefix = ""
        # for i in range(len(minWord)):
        #     prefix += minWord[i]
        #     for s in strs:
        #         if minWord[:i+1] != s[:i+1]:
        #             return prefix[:-1]
        # return prefix
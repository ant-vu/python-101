class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # time: O(n^2), space: O(1)
        if len(strs) == 1:
            return strs[0]

        shortest = min(strs, key=len)
        res = 0
        for length in range(len(shortest) + 1):
            flag = True
            for s in strs:
                if s[:length] != shortest[:length]:
                    flag = False
                    break
            if flag:
                res = max(res, length)
        return shortest[:res]
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # time: O(n^2), space: O(1)
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0]

        # time: O(n^2), space: O(1)
        # prefix = strs[0]
        # for i in range(1, len(strs)):
        #     while strs[i].find(prefix) != 0:
        #         prefix = prefix[:len(prefix) - 1]
        #         if prefix == "":
        #             return ""
        # return prefix

        # time: O(n^2), space: O(1)
        # if len(strs) == 1:
        #     return strs[0]

        # shortest = min(strs, key=len)
        # res = 0
        # for length in range(len(shortest) + 1):
        #     flag = True
        #     for s in strs:
        #         if s[:length] != shortest[:length]:
        #             flag = False
        #             break
        #     if flag:
        #         res = max(res, length)
        # return shortest[:res]
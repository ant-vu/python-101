class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # time: O(m*n^2), space: O(1)
        n = len(words)
        res = []
        for i in range(n):
            for j in range(n):
                if i != j and words[i] in words[j]:
                    res.append(words[i])
                    break
        return res

        # time: O(m*n^2), space: O(m*n)
        # n = len(words)
        # res = set()
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         if words[i] in words[j]:
        #             res.add(words[i])
        #         if words[j] in words[i]:
        #             res.add(words[j])
        # return list(res)
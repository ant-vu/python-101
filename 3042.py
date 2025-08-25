class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # time: O(m*n^2), space: O(1)
        def isPrefixAndSuffix(a, b):
            if len(a) > len(b):
                return 0
            for i in range(len(a)):
                if (a[i] != b[i]) or (a[i] != b[i + len(b) - len(a)]):
                    return 0
            return 1
        
        res = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                res += isPrefixAndSuffix(words[i], words[j])
        return res
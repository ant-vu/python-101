class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # time: O(l * m * n), space: O(m * n), l = len(s), m = len(words), n = len(words[0])
        l = len(s)
        m = len(words)
        n = len(words[0])
        total = m * n

        def freqMap(wordList):
            freq = {}
            for w in wordList:
                freq[w] = freq.get(w, 0) + 1
            return freq
        
        wordsFreqMap = freqMap(words)
        res = []
        for start in range(l - total + 1):
            sParts = [s[i:i+n] for i in range(start, start + total, n)]
            if freqMap(sParts) == wordsFreqMap:
                res.append(start)
        return res

        # time: O(n * n!), space: O(n), MLE
        # def permute(nums):
        #     # time: O(n * n!), space: O(n)
        #     res = []
        #     def backtrack(idx):
        #         if idx == len(nums):
        #             res.append(nums[:])
        #             return
        #         for i in range(idx, len(nums)):
        #             nums[i], nums[idx] = nums[idx], nums[i]
        #             backtrack(idx + 1)
        #             nums[i], nums[idx] = nums[idx], nums[i]
        #     backtrack(0)
        #     return res

        # indices = []
        # permutations = ["".join(x) for x in permute(words)]
        # windowLen = sum(len(w) for w in words)
        # for i in range(len(s) - windowLen + 1):
        #     if s[i:i+windowLen] in permutations:
        #         indices.append(i)
        # return indices
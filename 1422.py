class Solution:
    def maxScore(self, s: str) -> int:
        # time: O(n), space: O(1)
        ones, zeros, best = 0, 0, -inf
        for i in range(len(s) - 1):
            if s[i] == '1':
                ones += 1
            else:
                zeros += 1
            best = max(best, zeros - ones)
        if s[-1] == '1':
            ones += 1
        return best + ones

        # time: O(n), space: O(n)
        # forward = []
        # zeroes = 0
        # for num in s:
        #     if num == '0':
        #         zeroes += 1
        #     forward.append(zeroes)
        # backward = []
        # ones = 0
        # for i in range(len(s)-1, -1, -1):
        #     if s[i] == '1':
        #         ones += 1
        #     backward.append(ones)
        # res = 0
        # for i, j in zip(forward[0:-1], backward[0:-1][::-1]):
        #     res = max(res, i + j)
        # return res
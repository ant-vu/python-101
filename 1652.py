class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # time: O(n), space: O(n)
        n = len(code)
        res = [0] * n
        if k == 0:
            return res
        start, end, windowSum = 1, k, 0
        if k < 0:
            start = n - abs(k)
            end = n - 1
        for i in range(start, end + 1):
            windowSum += code[i]
        for i in range(n):
            res[i] = windowSum
            windowSum -= code[start % n]
            windowSum += code[(end + 1) % n]
            start += 1
            end += 1
        return res

        # time: O(n*k), space: O(n)
        # n = len(code)
        # if k == 0:
        #     return [0] * n
        # elif k > 0:
        #     res = []
        #     code *= 2
        #     for i in range(n):
        #         res.append(sum(code[i+1:i+k+1]))
        #     return res
        # else:
        #     res = []
        #     code *= 2
        #     for i in range(n, n * 2):
        #         res.append(sum(code[i+k:i]))
        #     return res
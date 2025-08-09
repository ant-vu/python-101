class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # time: O(n), space: O(1)
        cnt = 0
        for i in range(1, (n // 2) + 1):
            if n % i == 0:
                cnt += 1
                if cnt == k:
                    return i
        if cnt == k - 1:
            return n
        return -1

        # time: O(n), space: O(n)
        # factors = []
        # for i in range(1, n + 1):
        #     if n % i == 0:
        #         factors.append(i)
        #         if len(factors) == k:
        #             return factors[k - 1]
        # if len(factors) < k:
        #     return -1
        # return factors[k - 1]
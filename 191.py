class Solution:
    def hammingWeight(self, n: int) -> int:
        # time: O(1), space: O(1)
        cnt = 0
        for i in range(32):
            cnt += 1 if (n >> i) & 1 else 0
        return cnt

        # time: O(1), space: O(1)
        # cnt = 0
        # while n:
        #     cnt += 1 if n & 1 else 0
        #     n >>= 1
        # return cnt
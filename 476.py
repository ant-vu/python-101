class Solution:
    def findComplement(self, num: int) -> int:
        # time: O(n), space: O(n)
        binary = bin(num)[2:][::-1]
        factor = 1
        res = 0
        for i in binary:
            if int(i) == 0:
                res += factor
            factor *= 2
        return res
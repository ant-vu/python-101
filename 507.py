class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # time: O(logn), space: O(1)
        if num <= 1:
            return False
        res = 0
        for i in range(1, int(sqrt(num)) + 1):
            if num % i == 0:
                res += i + (num // i)
        return num == res - num
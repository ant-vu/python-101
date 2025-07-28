class Solution:
    def isHappy(self, n: int) -> bool:
        # time: O(logn), space: O(1)
        if n == 1:
            return True
        seen = set()
        while True:
            newN = 0
            while n > 0:
                newN += (n % 10) ** 2
                n //= 10
            if newN == 1:
                return True
            elif newN in seen:
                return False
            seen.add(newN)
            n = newN
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # time: O(n), space: O(1)
        def calcPower(x, n):
            if x == 0:
                return 0
            elif n == 0:
                return 1
            res = calcPower(x, n // 2)
            res *= res
            if n % 2 == 1:
                return res * x
            return res
        
        ans = calcPower(x, abs(n))
        if n >= 0:
            return ans
        return 1 / ans

        # time: O(n), space: O(1)
        # return x ** n
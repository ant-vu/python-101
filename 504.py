class Solution:
    def convertToBase7(self, num: int) -> str:
        # time: O(n), space: O(n)
        isNeg = False
        res = ""
        if num == 0:
            return "0"
        elif num < 0:
            isNeg = True
            num = abs(num)
        while num:
            res = str(num % 7) + res
            num //= 7
        return "-" + res if isNeg else res
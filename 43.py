class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # time: O(m * n), space: O(m + n)
        if num1 == '0' or num2 == '0':
            return '0'
        res = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for place2, digit2 in enumerate(num2):
            for place1, digit1 in enumerate(num1):
                zeros = place1 + place2
                multi = int(digit1) * int(digit2) + res[zeros]
                res[zeros] = multi % 10
                res[zeros + 1] += multi // 10
        if res[-1] == 0:
            res.pop()
        return ''.join(str(digit) for digit in res[::-1])
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # time: O(max(m, n)), space: O(max(m, n))
        num1 = "0" * (len(num2) - len(num1)) + num1
        num2 = "0" * (len(num1) - len(num2)) + num2
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = ""
        carry = 0
        for i in range(len(num1)):
            tmp = int(num1[i]) + int(num2[i]) + carry
            carry = 0
            if tmp > 9:
                tmp %= 10
                carry = 1
            res = res + str(tmp)
        return "1" + res[::-1] if carry else res[::-1]
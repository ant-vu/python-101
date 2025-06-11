class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # time: O(m * n), space: O(m + n)
        while len(a) < len(b):
            a = "0" + a
        while len(a) > len(b):
            b = "0" + b
        res = ""
        carry = 0
        for i in range(len(a) - 1, -1, -1):
            if a[i] == "1" and b[i] == "1" and carry:
                res = "1" + res
                carry = 1
            elif (a[i] == "1" and b[i] == "1" and not carry) or (a[i] == "1" and b[i] == "0" and carry) or (a[i] == "0" and b[i] == "1" and carry):
                res = "0" + res
                carry = 1
            elif (a[i] == "1" and b[i] == "0" and not carry) or (a[i] == "0" and b[i] == "1" and not carry) or (a[i] == "0" and b[i] == "0" and carry):
                res = "1" + res
                carry = 0
            else:
                res = "0" + res
                carry = 0
        return "1" + res if carry else res
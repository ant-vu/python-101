class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # time: O(max(m, n)), space: O(max(m, n))
        res = ""
        carry = 0
        idxA, idxB = len(a) - 1, len(b) - 1
        while idxA >= 0 or idxB >= 0 or carry == 1:
            if idxA >= 0:
                carry += int(a[idxA])
                idxA -= 1
            if idxB >= 0:
                carry += int(b[idxB])
                idxB -= 1
            res = str(carry % 2) + res
            carry //= 2
        return res

        # time: O(max(m, n)), space: O(max(m, n))
        # return bin(int(a, 2) + int(b, 2))[2:]

        # time: O(max(m, n)^2), space: O(max(m, n))
        # while len(a) < len(b):
        #     a = "0" + a
        # while len(a) > len(b):
        #     b = "0" + b
        # res = ""
        # carry = 0
        # for i in range(len(a) - 1, -1, -1):
        #     if a[i] == "1" and b[i] == "1" and carry:
        #         res = "1" + res
        #         carry = 1
        #     elif (a[i] == "1" and b[i] == "1" and not carry) or (a[i] == "1" and b[i] == "0" and carry) or (a[i] == "0" and b[i] == "1" and carry):
        #         res = "0" + res
        #         carry = 1
        #     elif (a[i] == "1" and b[i] == "0" and not carry) or (a[i] == "0" and b[i] == "1" and not carry) or (a[i] == "0" and b[i] == "0" and carry):
        #         res = "1" + res
        #         carry = 0
        #     else:
        #         res = "0" + res
        #         carry = 0
        # return "1" + res if carry else res
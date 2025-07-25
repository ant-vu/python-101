class Solution:
    def romanToInt(self, s: str) -> int:
        # time: O(n), space: O(1)
        romanToInt = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for a, b in zip(s, s[1:]):
            if romanToInt[a] < romanToInt[b]:
                total -= romanToInt[a]
            else:
                total += romanToInt[a]
        return total + romanToInt[s[-1]]

        # time: O(n), space: O(1)
        # n = len(s)
        # romanToInt = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL":40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
        # total = 0
        # for i in range(n - 1):
        #     if s[i:i+2] in romanToInt:
        #         total += romanToInt[s[i:i+2]]
        #         s = s.replace(s[i:i+2], "**")
        # for i in range(n):
        #     if s[i] in romanToInt:
        #         total += romanToInt[s[i]]
        # return total
class Solution:
    def intToRoman(self, num: int) -> str:
        # time: O(1), space: O(1)
        M = ['', 'M', 'MM', 'MMM']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        return M[num // 1000] + C[num % 1000 // 100] + X[num % 100 // 10] + I[num % 10]

        # time: O(1), space: O(1)
        # intToRoman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        # res = ""
        # for integer, roman in intToRoman:
        #     if num == 0:
        #         break
        #     count = num // integer
        #     res += roman * count
        #     num -= integer * count
        # return res

        # time: O(n), space: O(1)
        # roman = ""
        # while num > 0:
        #     if num >= 1000:
        #         num -= 1000
        #         roman += "M"
        #     elif num >= 900:
        #         num -= 900
        #         roman += "CM"
        #     elif num >= 500:
        #         num -= 500
        #         roman += "D"
        #     elif num >= 400:
        #         num -= 400
        #         roman += "CD"
        #     elif num >= 100:
        #         num -= 100
        #         roman += "C"
        #     elif num >= 90:
        #         num -= 90
        #         roman += "XC"
        #     elif num >= 50:
        #         num -= 50
        #         roman += "L"
        #     elif num >= 40:
        #         num -= 40
        #         roman += "XL"
        #     elif num >= 10:
        #         num -= 10
        #         roman += "X"
        #     elif num >= 9:
        #         num -= 9
        #         roman += "IX"
        #     elif num >= 5:
        #         num -= 5
        #         roman += "V"
        #     elif num >= 4:
        #         num -= 4
        #         roman += "IV"
        #     elif num >= 1:
        #         num -= 1
        #         roman += "I"
        # return roman
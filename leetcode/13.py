class Solution:
    def romanToInt(self, s: str) -> int:
        # time: O(n), space: O(n)
        nums = []
        idx = 0
        while idx < len(s) - 1:
            if s[idx : idx + 2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                nums.append(s[idx : idx + 2])
                idx += 2
            else:
                nums.append(s[idx])
                idx += 1
        if s[-2 :] not in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
            nums.append(s[-1])

        res = 0
        for num in nums:
            match num:
                case 'I':
                    res += 1
                case 'IV':
                    res += 4
                case 'V':
                    res += 5
                case 'IX':
                    res += 9
                case 'X':
                    res += 10
                case 'XL':
                    res += 40
                case 'L':
                    res += 50
                case 'XC':
                    res += 90
                case 'C':
                    res += 100
                case 'CD':
                    res += 400
                case 'D':
                    res += 500
                case 'CM':
                    res += 900
                case 'M':
                    res += 1000
        return res
class Solution:
    def romanToInt(self, s: str) -> int:
        # time: O(n), space: O(1)
        mapping = {'I': 1,
                   'V': 5,
                   'X': 10,
                   'L': 50,
                   'C': 100,
                   'D': 500,
                   'M': 1000}
        res = 0
        for a, b in zip(s, s[1:]):
            if mapping[a] < mapping[b]:
                res -= mapping[a]
            else:
                res += mapping[a]
        return res + mapping[s[-1]]

        # time: O(n), space: O(1)
        # mapping = {'I': 1,
        #            'IV': 4,
        #            'V': 5,
        #            'IX': 9,
        #            'X': 10,
        #            'XL': 40,
        #            'L': 50,
        #            'XC': 90,
        #            'C': 100,
        #            'CD': 400,
        #            'D': 500,
        #            'CM': 900,
        #            'M': 1000}
        # idx = 0
        # res = 0
        # while idx < len(s) - 1:
        #     if s[idx : idx + 2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
        #         res += mapping[s[idx : idx + 2]]
        #         idx += 2
        #     else:
        #         res += mapping[s[idx]]
        #         idx += 1
        # if s[-2 :] not in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
        #     res += mapping[s[-1]]
        # return res

        # time: O(n), space: O(n)
        # nums = []
        # idx = 0
        # while idx < len(s) - 1:
        #     if s[idx : idx + 2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
        #         nums.append(s[idx : idx + 2])
        #         idx += 2
        #     else:
        #         nums.append(s[idx])
        #         idx += 1
        # if s[-2 :] not in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
        #     nums.append(s[-1])

        # res = 0
        # for num in nums:
        #     match num:
        #         case 'I':
        #             res += 1
        #         case 'IV':
        #             res += 4
        #         case 'V':
        #             res += 5
        #         case 'IX':
        #             res += 9
        #         case 'X':
        #             res += 10
        #         case 'XL':
        #             res += 40
        #         case 'L':
        #             res += 50
        #         case 'XC':
        #             res += 90
        #         case 'C':
        #             res += 100
        #         case 'CD':
        #             res += 400
        #         case 'D':
        #             res += 500
        #         case 'CM':
        #             res += 900
        #         case 'M':
        #             res += 1000
        # return res
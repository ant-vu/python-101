class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # time: O(m + n), space: O(m + n)
        if str1 + str2 != str2 + str1:
            return ""
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]

        # time: O(min(m, n) * (m + n)), space: O(min(m, n))
        # res = ""
        # gcd = ""
        # for i in range(min(len(str1), len(str2))):
        #     gcd += str1[i]
        #     if (len(str1) % len(gcd) == 0 and gcd * (len(str1) // len(gcd)) == str1) and (len(str2) % len(gcd) == 0 and gcd * (len(str2) // len(gcd)) == str2):
        #         res = gcd
        # return res
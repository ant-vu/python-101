class Solution:
    def reverseVowels(self, s: str) -> str:
        # time: O(n), space: O(n)
        s = list(s)
        l, r = 0, len(s) - 1
        vowels = set("aeiouAEIOU")
        while l < r:
            while l < r and s[l] not in vowels:
                l += 1
            while l < r and s[r] not in vowels:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)

        # time: O(n), space: O(n)
        # s = list(s)
        # l, r = 0, len(s) - 1
        # vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        # while l < r:
        #     while s[l] not in vowels:
        #         l += 1
        #         if l > len(s) - 1:
        #             break
        #     while s[r] not in vowels:
        #         r -= 1
        #         if r < 0:
        #             break
        #     if l < r:
        #         s[l], s[r] = s[r], s[l]
        #         l += 1
        #         r -= 1
        # return "".join(s)
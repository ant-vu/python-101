class Solution:
    def isPalindrome(self, s: str) -> bool:
        # time: O(n), space: O(n)
        clean = ""
        for c in s:
            if c.isalnum():
                clean += c
        clean = clean.lower()
        print(clean)
        l, r = 0, len(clean) - 1
        while l < r:
            if clean[l] != clean[r]:
                return False
            l += 1
            r -= 1
        return True
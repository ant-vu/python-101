class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # time: O(2^n), space: O(n)
        res = []
        path = []

        def isPalindrome(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def partPalindrome(idx):
            if idx == len(s):
                res.append(path[:])
            for i in range(idx, len(s)):
                if isPalindrome(s, idx, i):
                    path.append(s[idx:i+1])
                    partPalindrome(i + 1)
                    path.pop()
        
        partPalindrome(0)
        return res
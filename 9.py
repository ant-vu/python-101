class Solution:
    def isPalindrome(self, x: int) -> bool:
        # time: O(n), space: O(1)
        return str(x) == str(x)[::-1]
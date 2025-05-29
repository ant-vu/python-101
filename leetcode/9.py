class Solution:
    def isPalindrome(self, x: int) -> bool:
        # time: O(n), space: O(1)
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        half = 0
        while x > half:
            half = (half * 10) + (x % 10)
            x //= 10
        return x == half or x == half // 10

        # time: O(n), space: O(1)
        # str_x = str(x)
        # left = 0
        # right = len(str_x) - 1
        # while left < right:
        #     if str_x[left] != str_x[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True
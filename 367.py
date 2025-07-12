class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # time: O(n), space: O(n)
        squares = []
        x = 0
        while (x ** 2) < (2 ** 31 - 1):
            squares.append(x ** 2)
            x += 1
        return num in squares
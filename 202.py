class Solution:
    def isHappy(self, n: int) -> bool:
        # time: O(n), space: O(n)
        seen = set()
        while True:
            if n == 1:
                return True
            n = sum([int(x) ** 2 for x in str(n)])
            if n in seen:
                return False
            seen.add(n)
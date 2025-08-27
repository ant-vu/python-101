class Solution:
    def numTilings(self, n: int) -> int:
        # time: O(n), space: O(n)
        @cache
        def solve(i, prevGap):
            if i > n:
                return 0
            elif i == n:
                return not prevGap
            elif prevGap:
                return solve(i + 1, False) + solve(i + 1, True)
            else:
                return solve(i + 1, False) + solve(i + 2, False) + 2 * solve(i + 2, True)
        
        return solve(0, False) % (10 ** 9 + 7)
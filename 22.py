class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # time: O(2^(2*n)), space: O(n)
        res = []

        def backtrack(left, right, cur):
            if left == right and left + right == n * 2:
                res.append(cur)
                return
            if left < n:
                backtrack(left + 1, right, cur + "(")
            if right < left:
                backtrack(left, right + 1, cur + ")")

        backtrack(0, 0, "")
        return res
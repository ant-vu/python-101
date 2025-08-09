class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # time: O(1), space: O(1)
        cnt = 0
        while left != right:
            left >>= 1
            right >>= 1
            cnt += 1
        return left << cnt
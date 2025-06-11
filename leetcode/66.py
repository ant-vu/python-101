class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # time: O(n), space: O(n)
        digits = digits[::-1]
        total = 1
        for idx in range(len(digits)):
            total += digits[idx] * (10 ** idx)
        res = []
        for num in str(total):
            res.append(int(num))
        return res
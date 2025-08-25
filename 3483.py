class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # time: O(n^3), space: O(n^3)
        n = len(digits)
        res = set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and i != k and j != k and digits[k] % 2 == 0 and digits[i] != 0:
                        res.add((digits[i], digits[j], digits[k]))
        return len(res)
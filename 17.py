class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # time: O(4^n), space: O(n)
        def backtrack(digits, comb):
            if not digits:
                res.append(comb)
            else:
                for letter in maps[digits[0]]:
                    backtrack(digits[1:], comb + letter)

        if not digits:
            return []
        maps = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        backtrack(digits, '')
        return res
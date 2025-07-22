class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # time: O(4^n), space: O(n)
        if not digits:
            return []
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []

        def backtrack(comb, idx):
            if len(comb) == len(digits):
                res.append(comb)
                return
            for letter in mapping[digits[idx]]:
                backtrack(comb + letter, idx + 1)
        
        backtrack("", 0)
        return res

        # time: O(4^n), space: O(n)
        # mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        # length = len(digits)
        # if length == 0:
        #     return []
        # res = []
        # def backtrack(digits, cur):
        #     if len(cur) == length:
        #         res.append("".join(cur))
        #     if digits:
        #         for i in mapping[digits[0]]:
        #             cur.append(i)
        #             backtrack(digits[1:], cur)
        #             cur.pop()
        # backtrack(digits, [])
        # return res
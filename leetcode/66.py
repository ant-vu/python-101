class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # time: O(n), space: O(1)
        digits = digits[::-1]
        for i in range(len(digits)):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                if i == len(digits) - 1:
                    digits.append(1)
            else:
                break
        return digits[::-1]

        # time: O(n), space: O(n)
        # digits = digits[::-1]
        # total = 1
        # for idx in range(len(digits)):
        #     total += digits[idx] * (10 ** idx)
        # res = []
        # for num in str(total):
        #     res.append(int(num))
        # return res
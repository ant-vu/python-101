class Solution:
    def addDigits(self, num: int) -> int:
        # time: O(1), space: O(1)
        if num == 0:
            return 0
        return num % 9 if num % 9 != 0 else 9

        # time: O(n), space: O(n)
        # if len(str(num)) == 1:
        #     return num
        # return self.addDigits(sum([int(x) for x in str(num)]))
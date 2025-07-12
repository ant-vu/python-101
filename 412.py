class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # time: O(n), space: O(n)
        res = []
        for i in range(1, n + 1):
            cur = ""
            if i % 3 == 0:
                cur += "Fizz"
            if i % 5 == 0:
                cur += "Buzz"
            res.append(cur if cur else str(i))
        return res
class Solution:
    def isHappy(self, n: int) -> bool:
        # time: O(logn), space: O(1)
        def getNextNumber(n):
            output = 0
            while n:
                digit = n % 10
                output += digit ** 2
                n //= 10
            return output
        
        slow = getNextNumber(n)
        fast = getNextNumber(getNextNumber(n))
        while slow != fast:
            if fast == 1:
                return True
            slow = getNextNumber(slow)
            fast = getNextNumber(getNextNumber(fast))
        return slow == 1

        # time: O(n), space: O(n)
        # seen = set()
        # while True:
        #     if n == 1:
        #         return True
        #     n = sum([int(x) ** 2 for x in str(n)])
        #     if n in seen:
        #         return False
        #     seen.add(n)
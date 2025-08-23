class Solution:
    def divisorGame(self, n: int) -> bool:
        # time: O(1), space: O(1)
        return n % 2 == 0

        # time: O(n), space: O(1)
        # moves = 0
        # while n > 1:
        #     for x in range(1, n):
        #         if n % x == 0:
        #             n -= x
        #             break
        #     moves += 1
        # return moves % 2 == 1
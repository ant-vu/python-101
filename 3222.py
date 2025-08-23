class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        # time: O(1), space: O(1)
        return 'Alice' if min(x, y // 4) % 2 == 1 else 'Bob'

        # time: O(n), space: O(1)
        # winner = 'Bob'
        # while x >= 1 and y >= 4:
        #     if winner == 'Alice':
        #         winner = 'Bob'
        #     else:
        #         winner = 'Alice'
        #     x -= 1
        #     y -= 4
        # return winner
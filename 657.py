class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # time: O(n), space: O(1)
        x, y = 0, 0
        for m in moves:
            if m == "L":
                x -= 1
            elif m == "R":
                x += 1
            elif m == "D":
                y -= 1
            elif m == "U":
                y += 1
        return x == y == 0
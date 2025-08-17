class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # time: O(n), space: O(1)
        x, y = 0, 0
        dx, dy = 0, 1
        for i in instructions:
            if i == "G":
                x += dx
                y += dy
            elif i == "L":
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # time: O(ROWS * COLS), space: O(ROWS * COLS)
        ROWS, COLS = len(maze), len(maze[0])
        directions = ([0, 1], [1, 0], [0, -1], [-1, 0])
        q = deque([entrance])
        visited = {tuple(entrance)}
        steps = 0
        while q:
            for _ in range(len(q)):
                xo, yo = q.popleft()
                if (0 in (xo, yo) or xo == ROWS - 1 or yo == COLS - 1) and [xo, yo] != entrance:
                    return steps
                for xn, yn in directions:
                    x, y = xo + xn, yo + yn
                    if 0 <= x < ROWS and 0 <= y < COLS and maze[x][y] == '.' and (x, y) not in visited:
                        visited.add((x, y))
                        q.append([x, y])
            steps += 1
        return -1

        # time: O(ROWS * COLS), space: O(ROWS * COLS)
        # ROWS, COLS = len(maze), len(maze[0])
        # directions = ([0, 1], [1, 0], [0, -1], [-1, 0])
        # q = deque([(entrance[0], entrance[1], 0)])
        # maze[entrance[0]][entrance[1]] = '+'
        # while q:
        #     xo, yo, steps = q.popleft()
        #     if (0 in (xo, yo) or xo == ROWS - 1 or yo == COLS - 1) and [xo, yo] != entrance:
        #         return steps
        #     for xn, yn in directions:
        #         x, y = xo + xn, yo + yn
        #         if 0 <= x < ROWS and 0 <= y < COLS and maze[x][y] == '.':
        #             maze[x][y] = '+'
        #             q.append([x, y, steps + 1])
        # return -1
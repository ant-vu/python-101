class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # time: O(n), space: O(1)
        (x1, y1), (x2, y2) = coordinates[:2]
        for x, y in coordinates[2:]:
            if (y - y1) * (x2 - x1) != (y2 - y1) * (x - x1):
                return False
        return True

        # time: O(nlogn), space: O(n)
        # x = coordinates[0][0]
        # y = coordinates[0][1]
        # sameX = True
        # sameY = True
        # for i in range(1, len(coordinates)):
        #     if coordinates[i][0] != x:
        #         sameX = False
        #     if coordinates[i][1] != y:
        #         sameY = False
        # if sameX or sameY:
        #     return True

        # coordinates.sort()
        # dx = coordinates[1][0] - coordinates[0][0]
        # dy = coordinates[1][1] - coordinates[0][1]
        # div = min(abs(dx), abs(dy))
        # if div == 0:
        #     return False
        # dx //= div
        # dy //= div
        # for i in range(1, len(coordinates) - 1):
        #     if (coordinates[i + 1][0] - coordinates[i][0]) // dx != (coordinates[i + 1][1] - coordinates[i][1]) // dy:
        #         return False
        # return True
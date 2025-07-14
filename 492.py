from typing import List

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = w = int(area ** 0.5)
        while True:
            if l * w == area:
                return [l, w]
            elif l * w < area:
                l += 1
            else:
                w -= 1
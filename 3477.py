class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # time: O(n^2), space: O(1)
        res = len(fruits)
        for i, fruit in enumerate(fruits):
            for j, basket in enumerate(baskets):
                if fruit <= basket:
                    res -= 1
                    baskets[j] = float('-inf')
                    break
        return res
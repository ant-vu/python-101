class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # time: O(n), space: O(n)
        diff = set(candyType)
        return min(len(diff), len(candyType) // 2)
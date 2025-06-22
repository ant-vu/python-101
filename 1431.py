class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # time: O(n), space: O(1)
        res = []
        maxi = max(candies)
        for c in candies:
            res.append(c + extraCandies >= maxi)
        return res
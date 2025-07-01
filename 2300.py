class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # time: O(mlogn), space: O(1)
        potions.sort()
        res = []
        for s in spells:
            l, r = 0, len(potions) - 1
            while l <= r:
                m = l + (r - l) // 2
                if s * potions[m] >= success:
                    r = m - 1
                elif s * potions[m] < success:
                    l = m + 1
            res.append(len(potions) - l)
        return res
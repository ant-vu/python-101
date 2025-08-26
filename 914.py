class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # time: O(nloglogn), space: O(n)
        counts = {}
        for card in deck:
            counts[card] = 1 + counts.get(card, 0)
        for i in counts.values():
            for j in counts.values():
                if gcd(i, j) <= 1:
                    return False
        return True
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # time: O(m + n), space: O(n)
        sortedScore = sorted(score)
        res = []
        for s in score:
            rank = len(score) - sortedScore.index(s)
            if rank == 1:
                res.append("Gold Medal")
            elif rank == 2:
                res.append("Silver Medal")
            elif rank == 3:
                res.append("Bronze Medal")
            else:
                res.append(str(rank))
        return res
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # time: O(nlogn), space: O(n)
        cnt = defaultdict(int)
        for n in nums:
            cnt[n] += 1
        res = 0
        sortedCnt = sorted(cnt.items())
        for i in range(len(sortedCnt) - 1):
            if sortedCnt[i][0] == sortedCnt[i + 1][0] - 1:
                res = max(res, sortedCnt[i][1] + sortedCnt[i + 1][1])
        return res
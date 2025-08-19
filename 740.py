class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # time: O(n), space: O(n)
        multis = defaultdict(int)
        for n in nums:
            multis[n] = multis.get(n, 0) + n
        prev, cur = 0, 0
        for val in range(max(multis) + 1):
            prev, cur = cur, max(cur, prev + multis[val])
        return cur
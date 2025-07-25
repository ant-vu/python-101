class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # time: O(n), space: O(1)
        n = len(nums)
        goalIdx = n - 1
        for curIdx in range(n - 2, -1, -1):
            if curIdx + nums[curIdx] >= goalIdx:
                goalIdx = curIdx
        return goalIdx == 0

        # time: O(n), space: O(1)
        # n = len(nums)
        # curIdx = n - 2
        # goalIdx = n - 1
        # while curIdx >= 0:
        #     if curIdx + nums[curIdx] >= goalIdx:
        #         goalIdx = curIdx
        #     curIdx -= 1
        # return goalIdx == 0

        # time: O(n^2), space: O(n)
        # n = len(nums)
        # jumpable = [False] * n
        # jumpable[0] = True
        # for i in range(n):
        #     if jumpable[i]:
        #         for j in range(i + 1, min(i + 1 + nums[i], n)):
        #             jumpable[j] = True
        # return jumpable[-1]
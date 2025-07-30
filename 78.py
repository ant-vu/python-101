class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # time: O(2^n), space: O(2^n)
        res = []
        subset = []

        def createSubset(i):
            if i == len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            createSubset(i + 1)
            subset.pop()
            createSubset(i + 1)
        
        createSubset(0)
        return res
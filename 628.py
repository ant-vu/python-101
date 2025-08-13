class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # time: O(n), space: O(n)
        copy = nums[:]
        a = max(nums)
        nums.remove(a)
        b = max(nums)
        nums.remove(b)
        c = max(nums)
        nums.remove(c)
        d = min(copy)
        copy.remove(d)
        e = min(copy)
        copy.remove(e)
        return max(a * b * c, a * d * e)
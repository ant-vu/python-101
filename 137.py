class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        ones = 0
        twos = 0
        for n in nums:
            ones ^= (n & ~twos)
            twos ^= (n & ~ones)
        return ones
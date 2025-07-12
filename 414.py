class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        if len(set(nums)) < 3:
            return max(nums)
        fst, snd, trd = -inf, -inf, -inf
        for n in set(nums):
            if n > fst:
                trd = snd
                snd = fst
                fst = n
            elif n > snd:
                trd = snd
                snd = n
            elif n > trd:
                trd = n
        return trd
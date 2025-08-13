class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # time: O(n), space: O(n)
        n = len(nums)
        sumToN = n * (n + 1) // 2
        seen = set()
        for n in nums:
            if n in seen:
                y = n
                break
            seen.add(n)
        return [y, y + sumToN - sum(nums)]
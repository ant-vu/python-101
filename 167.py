class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # time: O(n), space: O(1)
        l = 0
        r = len(numbers) - 1
        while True:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
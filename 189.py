class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # time: O(n), space: O(1)
        n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

        # time: O(n), space: O(n)
        # k %= len(nums)
        # if k != 0:
        #     nums[:k], nums[k:] = nums[-k:], nums[:-k]

        # time: O(n), space: O(n)
        # n = len(nums)
        # k %= n
        # rotated = [0] * n
        # for i in range(n):
        #     rotated[(i + k) % n] = nums[i]
        # for i in range(n):
        #     nums[i] = rotated[i]

        # time: O(n), space: O(n)
        # for _ in range(k):
        #     nums.insert(0, nums.pop())
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        k = 1
        for n in nums[1:]:
            if n != nums[k - 1]:
                nums[k] = n
                k += 1
        return k

        # time: O(n), space: O(1)
        # k = 0
        # for n in nums[1:]:
        #     if n != nums[k]:
        #         k += 1
        #         nums[k] = n
        # return k + 1

        # time: O(n), space: O(n)
        # seen = set()
        # k = 0
        # for n in nums:
        #     if n not in seen:
        #         nums[k] = n
        #         seen.add(n)
        #         k += 1
        # return k